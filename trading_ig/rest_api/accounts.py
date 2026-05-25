from dataclasses import dataclass
from datetime import datetime
from typing import Any

from trading_ig.rest_api.api_enums import IGRestAPIVersion, RequestType
from trading_ig.rest_api.base_rest_api_call import Arguments, RestApiCall, RequestData
from trading_ig.utils import _HAS_PANDAS

if _HAS_PANDAS:
    import pandas as pd

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


@dataclass
class FetchAccountActivityByDateArguments(Arguments):
    fromDate: datetime
    toDate: datetime

    def as_string(self):
        fmt = "%d-%m-%Y"
        return f"/{self.fromDate.strftime(fmt)}/{self.toDate.strftime(fmt)}"


class FetchAccountActivityByDate(RestApiCall):

    def __init__(self, fetch_account_acitvity_by_date_arguments: FetchAccountActivityByDateArguments):
        self.base_endpoint = "/history/activity"
        self.request_type = RequestType.GET
        self.api_version = IGRestAPIVersion.ONE
    
        self.arguments = fetch_account_acitvity_by_date_arguments

    def process_payload(self, payload: dict[str, Any]):
        if _HAS_PANDAS:
            return pd.DataFrame(payload["activities"])
        else:
            return payload
