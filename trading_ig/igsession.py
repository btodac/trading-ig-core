import json
import logging
from typing import Any

from requests import Session, Response

from trading_ig.rest_api.api_enums import IGRestAPIVersion, RequestType
from trading_ig.rest_api.base_rest_api_call import RestApiCall
from trading_ig.utils import api_limit_hit

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


class IGSession:
    """Session with CRUD operation"""

    def __init__(self, base_url: str, api_key: str, session: Session):
        self.base_url = base_url
        self.api_key = api_key
        self.session = session

        self.session.headers.update(
            {
                "X-IG-API-KEY": self.api_key,
                "Content-Type": "application/json",
                "Accept": "application/json; charset=UTF-8",
            }
        )

    def _get_session(
        self, session: Session | None = None, 
        version: IGRestAPIVersion | None = None
    ) -> Session:
        """Returns a Requests session if session is None
        or session if it's not None (cached session
        with requests-cache for example)

        :param session:
        :return:
        """
        if session is None:
            session = self.session 
        else:
            assert isinstance(session, Session), (
                f"session must be {type(Session)} not {type(session)}"
            )
            session = session
        if IGRestAPIVersion is not None:
            session.headers.update({"VERSION": str(version)})
        return session

    def _get_url(self, endpoint: str) -> str:
        """Returns url from endpoint and base url"""
        return self.base_url + endpoint

    def request(self, rest_api_call: RestApiCall, session: Session | None = None):
        session = self._get_session(session, rest_api_call.api_version)
        request = getattr(session, rest_api_call.request_type)
        response: Response = request(self._get_url(rest_api_call.endpoint), data=rest_api_call.data)
        logger.info(f"{rest_api_call.request_type.upper()} '{rest_api_call.endpoint}', resp {response.status_code}")

        if rest_api_call.request_type == RequestType.GET:
            self.handle_session_tokens(response, self._get_session(session))

        if response.status_code == 200:
            payload = self.parse_response(response)
            return rest_api_call.process_payload(payload)
        else:
            self.handle_request_error_code(response)

    def handle_session_tokens(self, response: Response, session: Session | None = None):
        """
        Copy session tokens from response to headers, so they will be present for all
            future requests
        :param response: HTTP response object
        :type response: requests.Response
        :param session: HTTP session object
        :type session: requests.Session
        """
        session = self._get_session(session)
        if "CST" in response.headers:
            session.headers.update({"CST": response.headers["CST"]})
        if "X-SECURITY-TOKEN" in response.headers:
            session.headers.update(
                {"X-SECURITY-TOKEN": response.headers["X-SECURITY-TOKEN"]}
            )

    @staticmethod
    def parse_response(response: Response) -> dict[str: Any]:
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
                response.encoding = 'UTF'
                if api_limit_hit(response.text):
                    raise ApiExceededException()
                if "error.public-api.failure.kyc.required" in response.text:
                    raise KycRequiredException(
                        "KYC issue: you need to login manually to the web interface and "
                        "complete IGs occasional Know Your Customer checks"
                    )
            case _ if response.status_code >= 500:
                raise (
                    IGException(
                        f"Server problem: status code: {response.status_code}, {response.reason}"
                    )
                )
        raise IGException(f"HTTP error: {response.status_code}, {response.text}")