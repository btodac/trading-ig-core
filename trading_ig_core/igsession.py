import json
import logging
import time
from dataclasses import dataclass
from typing import Any, Callable

from lightstreamer.client import LightstreamerClient
from requests import Session, Response

from trading_ig_core.rest_api.rest_api_enums import IGRestAPIVersion, Gateway, RequestType
from trading_ig_core.rest_api.login import (
    CreateSessionV2,
    GetSession,
    SwitchAccount,
    Logout,
    GetEncryptionKey,
)
from trading_ig_core.rest_api.responses.login import (
    SessionCreateV1Response,
    SessionDetailsResponse,
    SwitchAccountResponse,
    GetEncryptionKeyResponse,
)
from trading_ig_core.rest_api.base_rest_api_call import RestApiCall
from trading_ig_core.utils import api_limit_hit

logger = logging.getLogger(__name__)


class ApiExceededException(Exception):
    """Raised when our code hits the IG endpoint too often"""

    pass


class TokenInvalidException(ConnectionError):
    """Raised when the session token is invalid or expired"""

    pass


class IGException(Exception):
    pass


class KycRequiredException(Exception):
    """Raised when IG needs the user to confirm or re-confirm their KYC status"""

    pass


class IGInputError(ValueError):
    pass


@dataclass
class IGAccountDetails:
    username: str = "YOUR_USERNAME"
    password: str = "YOUR_PASSWORD"
    api_key: str = "YOUR_API_KEY"
    acc_type: Gateway = Gateway.DEMO
    acc_number: str = "ABC123"

    def __post_init__(self):
        if not isinstance(self.acc_type, Gateway):
            if self.acc_type in Gateway:
                self.acc_type = Gateway(self.acc_type)
            else:
                raise ValueError(
                    f"The value of acc_type, {self.acc_type} is not a valid Gateway value")



class IGStreamService(LightstreamerClient):
    def __init__(self, session_details: SessionDetailsResponse, ls_password: str):
        # Establishing a new connection to Lightstreamer Server
        logger.info("Starting connection with %s", session_details.lightstreamerEndpoint)

        super().__init__(session_details.lightstreamerEndpoint, None)
        self.connectionDetails.setUser(session_details.accountId)
        self.connectionDetails.setPassword(ls_password)

        try:
            self.connect()
        except Exception as e:
            logger.error("Unable to connect to Lightstreamer Server: %s", str(e))
        else:
            i = 0
            while i < 3:
                if self.getStatus().startswith("CONNECTED"):
                    logger.debug("Connected to lightstreamer server")
                    return
                else:
                    time.sleep(1)
                    i += 1
            status =  self.getStatus()
            logger.error("Lightstreamer Server connection failed with status: %s", status)

    def __del__(self):
        self.disconnect()

    def unsubscribe_all(self):
        for sub in self.getSubscriptions():
            self.unsubscribe(sub)

    def disconnect(self):
        self.unsubscribe_all()
        super().disconnect()


class IGSession:
    """Session with CRUD operation"""

    def __init__(
        self, ig_account_details: IGAccountDetails, encrypt_password: bool = True
    ):
        self.base_url = ig_account_details.acc_type.url
        self._account = ig_account_details
        self.username = ig_account_details.username
        self.api_key = ig_account_details.api_key
        self.acc_type = ig_account_details.acc_type
        self.acc_number = ig_account_details.acc_number

        self.session = Session()

        self.session.headers.update(
            {
                "X-IG-API-KEY": self._account.api_key,
                "Content-Type": "application/json",
                "Accept": "application/json; charset=UTF-8",
            }
        )
        if encrypt_password:
            encryption_data: GetEncryptionKeyResponse = self.request(GetEncryptionKey())

            self.account_details: SessionCreateV1Response = self.request(
                CreateSessionV2(
                    username=ig_account_details.username,
                    password=ig_account_details.password,
                    encryption_key=encryption_data.encryptionKey,
                    encryption_timestamp=encryption_data.timeStamp,
                )
            )
        else:
            self.account_details: SessionCreateV1Response  = self.request(
                CreateSessionV2(
                    username=ig_account_details.username,
                    password=ig_account_details.password,
                )
            )

        session_details = self.request(GetSession(fetch_session_tokens=False))    
        cst = self.session.headers["CST"]
        xsecuritytoken = self.session.headers["X-SECURITY-TOKEN"]
        ls_password = f"CST-{cst}|XST-{xsecuritytoken}"

        self.streamer = IGStreamService(session_details, ls_password)

    def __del__(self):
        self.streamer.disconnect()
        try:
            self.terminate_session()
        except Exception as e:
            logger.debug(str(e))

    def get_session(self):
        session_details: SessionDetailsResponse = self.request(GetSession(fetch_session_tokens=True))
        # self.account_details |= session_details
        return session_details

    def terminate_session(self):
        self.request(Logout())

    def _set_header_version(self, version: IGRestAPIVersion) -> Session:
        self.session.headers.update({"VERSION": str(version)})

    def _get_url(self, endpoint: str) -> str:
        """Returns url from endpoint and base url"""
        return self.base_url + endpoint

    def request(
        self,
        rest_api_call: RestApiCall,
        return_raw: bool = False,
    ) -> Response:
        self._set_header_version(rest_api_call.api_version)
        url = self._get_url(rest_api_call.endpoint)
        if (
            rest_api_call.request_type == RequestType.DELETE
            and rest_api_call.request_data is not None
        ):
            # The IG API shows a DELETE with a body, which is not allowed!
            self.session.headers.update({"_method": "DELETE"})
            request = getattr(self.session, RequestType.POST)
        else:
            request = getattr(self.session, rest_api_call.request_type)
        response: Response = request(url, data=json.dumps(rest_api_call.data))
        self.session.headers.pop("_method", None)
        logger.info(
            f"{rest_api_call.request_type.upper()} '{rest_api_call.endpoint}', resp {response.status_code}"
        )

        self.handle_session_tokens(response)

        if response.status_code == 200:
            if return_raw:
                return response
            payload = self.parse_response(response)
            return rest_api_call.process_payload(payload)
        if response.status_code == 204:
            return
        else:
            self.handle_request_error_code(response)

    def handle_session_tokens(self, response: Response):
        """
        Copy session tokens from response to headers, so they will be present for all
            future requests
        :param response: HTTP response object
        :type response: requests.Response
        :param session: HTTP session object
        :type session: requests.Session
        """
        if "CST" in response.headers:
            self.session.headers.update({"CST": response.headers["CST"]})
        if "X-SECURITY-TOKEN" in response.headers:
            self.session.headers.update(
                {"X-SECURITY-TOKEN": response.headers["X-SECURITY-TOKEN"]}
            )

    @staticmethod
    def parse_response(response: Response) -> dict[str:Any]:
        """Parses JSON response into dict
        exception raised when error occurs"""
        payload = json.loads(response.text)
        if "errorCode" in payload:
            raise Exception(payload["errorCode"])
        return payload

    def handle_request_error_code(self, response: Response):
        status_code: int = response.status_code
        match status_code:
            case 401 | 403:
                response.encoding = "UTF"
                if api_limit_hit(response.text):
                    raise ApiExceededException()
                if "error.public-api.failure.kyc.required" in response.text:
                    raise KycRequiredException(
                        "KYC issue: you need to login manually to the web interface and "
                        "complete IGs occasional Know Your Customer checks"
                    )
            case _:
                response_str = f"{response.status_code}, {response.reason}, {response.text}"
                if response.status_code >= 500:
                    raise IGException(
                        f"Server problem: status code: {response_str}"
                    )
                else:
                    raise IGException(
                        f"Client problem: status code: {response_str}"
                    )
            
