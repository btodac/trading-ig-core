"""These are special methods connected to the session rather than used to get/put/post data by the user"""

import logging
from base64 import b64encode, b64decode
from dataclasses import dataclass
from typing import Any

from cryptography.hazmat.primitives.serialization import load_der_public_key
from cryptography.hazmat.primitives.asymmetric import padding

from trading_ig.rest_api.rest_api_enums import IGRestAPIVersion, RequestType
from trading_ig.rest_api.responses.login import SessionCreateV1Response, SessionCreateV3Response, SessionDetailsResponse, SwitchAccountResponse, GetEncryptionKeyResponse
from trading_ig.rest_api.base_rest_api_call import RestApiCall, RequestData

logger = logging.getLogger(__name__)


class GetEncryptionKey(RestApiCall):
    def __init__(self):
        self.base_endpoint = "/session/encryptionKey"
        self.request_type = RequestType.GET
        self.api_version = IGRestAPIVersion.ONE

    def process_payload(self, payload: dict[str, Any]):
        return GetEncryptionKeyResponse(**payload)


@dataclass
class CreateSessionData(RequestData):
    identifier: str
    password: str


@dataclass
class CreateSessionDataV1(CreateSessionData):
    identifier: str
    password: str
    encryptedPassword: bool = False


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
            self.request_data = CreateSessionDataV1(
                identifier=username,
                password=password,
                encryptedPassword=False,
            )
        elif (encryption_key is not None) and (encryption_timestamp is not None):
            encrypted_password = self.encrypt_password(
                password, encryption_key, encryption_timestamp
            )
            self.request_data = CreateSessionDataV1(
                identifier=username,
                password=encrypted_password,
                encryptedPassword=True,
            )
        else:
            raise ValueError(
                "Either both 'encryption_key' and 'encryption_timestamp' must be provided or neither"
            )

    def encrypt_password(self, password: str, key: str, timestamp: str):
        """Encrypt password for login"""
        public_key = load_der_public_key(b64decode(key))
        string = password + "|" + str(int(timestamp))
        message = b64encode(string.encode())
        encrypted_bytes = public_key.encrypt(message, padding.PKCS1v15())
        return b64encode(encrypted_bytes).decode()
    
    def process_payload(self, payload: dict):
        return SessionCreateV1Response(**payload)


class CreateSessionV2(CreateSessionV1):
    def __init__(
        self,
        username: str,
        password: str,
        encryption_key: str | None = None,
        encryption_timestamp: str | None = None,
    ):
        super().__init__(username, password, encryption_key, encryption_timestamp)
        self.api_version = IGRestAPIVersion.TWO


class CreateSessionV3(RestApiCall):
    def __init__(
        self,
        username: str,
        password: str,
    ):
        self.base_endpoint = "/session"
        self.request_type = RequestType.POST
        self.api_version = IGRestAPIVersion.THREE

        self.request_data = CreateSessionData(identifier=username, password=password)

    def process_payload(self, payload: dict):
        return SessionCreateV3Response(**payload)


@dataclass
class RefreshSessionData(RequestData):
    refreshToken: str


class RefreshSession(RestApiCall):
    def __init__(self, refresh_token: str):
        self.base_endpoint = "/session/refresh-token"
        self.request_type = RequestType.POST
        self.api_version = IGRestAPIVersion.ONE
        self.request_data = RefreshSessionData(refreshToken=refresh_token)


class Logout(RestApiCall):
    def __init__(self):
        self.base_endpoint = "/session"
        self.request_type = RequestType.DELETE
        self.api_version = IGRestAPIVersion.ONE


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

    def process_payload(self, payload: dict):
        return SwitchAccountResponse(**payload)


@dataclass
class GetSessionData(RequestData):
    fetchSessionTokens: bool


class GetSession(RestApiCall):
    def __init__(self, fetch_session_tokens: bool = False):
        self.base_endpoint = "/session"
        self.request_type = RequestType.GET
        self.api_version = IGRestAPIVersion.ONE

        self.request_data = GetSessionData(fetchSessionTokens=fetch_session_tokens)

    def process_payload(self, payload: dict):
        return SessionDetailsResponse(**payload)
