import logging
from base64 import b64encode, b64decode
from dataclasses import dataclass
from datetime import datetime
from typing import Any

from cryptography.hazmat.primitives.serialization import load_der_public_key
from cryptography.hazmat.primitives.asymmetric import padding

from trading_ig.rest_api.api_enums import IGRestAPIVersion, RequestType
from trading_ig.rest_api.base_rest_api_call import Arguments, RestApiCall, RequestData

logger = logging.getLogger(__name__)

class GetEncryptionKey(RestApiCall):
    def __init__(self):
        self.base_endpoint = "/session/encryptionKey"  
        self.request_type = RequestType.GET
        self.api_version = IGRestAPIVersion.ONE

    def process_payload(self, payload: dict[str, Any]):
        return payload["encryptionKey"], payload["timeStamp"]


@dataclass
class CreateSessionData(RequestData):
    
    identifier: str  # IG username
    password: str  # IG password/encrypted IG password
    encryptedPassword: bool = False  # Is the password encrypted


class CreateSessionV1(RestApiCall):
    def __init__(
        self, 
        username: str, 
        password: str, 
        encryption_key: str | None = None, 
        encryption_timestamp: str | None = None,
    ):
        self.base_endpoint = "/session"
        self.request_type = RequestType.POST
        self.api_version = IGRestAPIVersion.ONE
        if (encryption_key is None) and (encryption_timestamp is None):
            self.data = CreateSessionData(username, password, encryptedPassword=False) 
        elif (encryption_key is not None) and (encryption_timestamp is not None):
            encrypted_password = self.encrypt_password(password, encryption_key, encryption_timestamp)
            self.data = CreateSessionData(username, encrypted_password, encryptedPassword=True) 
        else:
            raise ValueError("Either both 'encryption_key' and 'encryption_timestamp must be provided or neither")
        """
        self._manage_headers(response) -> Headers con
        data = self.parse_response(response.text)
        """
    
    def encrypt_password(self, password: str, key: str, timestamp: str):
        """Encrypt password for login"""
        public_key = load_der_public_key(b64decode(key))
        string = password + "|" + str(int(timestamp))
        message = b64encode(string.encode())  # string -> bytes -> b64 bytes
        encrypted_bytes = public_key.encrypt(message, padding.PKCS1v15())
        return b64encode(encrypted_bytes).decode()  # bytes -> b64 bytes -> b64 string
    

def create_session(self, session=None, encryption=False, version="2"):
        """
        Creates a session, obtaining tokens for subsequent API access

        ** April 2021 v3 has been implemented, but is not the default for now

        :param session: HTTP session
        :type session: requests.Session
        :param encryption: whether or not the password should be encrypted.
            Required for some regions
        :type encryption: Boolean
        :param version: API method version
        :type version: str
        :return: JSON response body, parsed into dict
        :rtype: dict
        """
        if version == "3" and self.ACC_NUMBER is None:
            raise IGException("Account number must be set for v3 sessions")

        logger.info(
            f"Creating new v{version} session for user '{self.IG_USERNAME}' at "
            f"'{self.BASE_URL}'"
        )
        password = self.encrypted_password(session) if encryption else self.IG_PASSWORD
        params = {"identifier": self.IG_USERNAME, "password": password}
        if encryption:
            params["encryptedPassword"] = True
        endpoint = "/session"
        action = "create"
        response = self._req(action, endpoint, params, session, version, check=False)
        self._manage_headers(response)
        data = self.parse_response(response.text)

        if self._use_rate_limiter:
            self.setup_rate_limiter()

        return data

@dataclass
class SwitchAccountData(RequestData):
    accountId: str
    defaultAccount: str


class SwitchAccount(RestApiCall):
        
    def __init__(self, account_id, default_account):
        self.base_endpoint = "/session"
        self.request_type = RequestType.PUT
        self.api_version = IGRestAPIVersion.ONE
    
        self.request_data = SwitchAccountData(
            accountId=account_id,
            defaultAccount=default_account,
        )


@dataclass
class ReadSessionData(RequestData):
    fetchSessionTokens: bool


class ReadSession(RestApiCall):

    def __init__(self, fetch_session_tokens: bool=False):
        self.base_endpoint = "/session"
        self.request_type = RequestType.GET
        self.api_version = IGRestAPIVersion.ONE
    
        self.request_data = ReadSessionData(fetchSessionTokens=fetch_session_tokens)

