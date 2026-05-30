from dataclasses import dataclass, field
from datetime import datetime
from typing import Any

from trading_ig.rest_api.rest_api_enums import (
    IGRestAPIVersion,
    RequestType,
    TransactionType,
)
from trading_ig.rest_api.base_rest_api_call import Arguments, RestApiCall, RequestData
from trading_ig.utils import _HAS_PANDAS

if _HAS_PANDAS:
    import pandas as pd


class FetchAccounts(RestApiCall):
    def __init__(self):
        self.base_endpoint = "/accounts"
        self.request_type = RequestType.GET
        self.api_version = IGRestAPIVersion.ONE


class FetchAccountPreferences(RestApiCall):
    def __init__(self):
        self.base_endpoint = "/accounts/preferences"
        self.request_type = RequestType.GET
        self.api_version = IGRestAPIVersion.ONE


@dataclass
class UpdateAccountPreferencesData(RequestData):
    trailingStopsEnabled: bool


class UpdateAccountPreferences(RestApiCall):
    def __init__(self, trailing_stops_enabled: bool):
        self.base_endpoint = "/accounts/preferences"
        self.request_type = RequestType.PUT
        self.api_version = IGRestAPIVersion.ONE
        self.request_data = UpdateAccountPreferencesData(
            trailingStopsEnabled=trailing_stops_enabled
        )


@dataclass
class FetchAccountActivityByPeriodArguments(Arguments):
    milliseconds: int

    def as_string(self):
        return f"/{self.milliseconds}"


class FetchAccountActivityByPeriod(RestApiCall):
    def __init__(self, milliseconds: int):
        self.base_endpoint = "/history/activity"
        self.request_type = RequestType.GET
        self.api_version = IGRestAPIVersion.ONE
        self.arguments = FetchAccountActivityByPeriodArguments(
            milliseconds=milliseconds
        )


@dataclass
class FetchAccountActivityV2Data(RequestData):
    from_: str | None = field(default=None, metadata={"json_name": "from"})
    to: str | None = None
    maxSpanSeconds: int | None = None
    pageSize: int = 20
    pageNumber: int | None = None


class FetchAccountActivityV2(RestApiCall):
    def __init__(
        self,
        from_date: str | None = None,
        to_date: str | None = None,
        max_span_seconds: int | None = None,
        page_size: int = 20,
        page_number: int | None = None,
    ):
        self.base_endpoint = "/history/activity/"
        self.request_type = RequestType.GET
        self.api_version = IGRestAPIVersion.TWO
        self.request_data = FetchAccountActivityV2Data(
            from_=from_date,
            to=to_date,
            maxSpanSeconds=max_span_seconds,
            pageSize=page_size,
            pageNumber=page_number,
        )


@dataclass
class FetchAccountActivityData(RequestData):
    from_: str | None = field(default=None, metadata={"json_name": "from"})
    to: str | None = None
    detailed: bool | None = None
    dealId: str | None = None
    filter: str | None = None
    pageSize: int = 50


class FetchAccountActivity(RestApiCall):
    def __init__(
        self,
        from_date: str | None = None,
        to_date: str | None = None,
        detailed: bool = False,
        deal_id: str | None = None,
        fiql_filter: str | None = None,
        page_size: int = 50,
    ):
        self.base_endpoint = "/history/activity/"
        self.request_type = RequestType.GET
        self.api_version = IGRestAPIVersion.THREE
        self.request_data = FetchAccountActivityData(
            from_=from_date,
            to=to_date,
            detailed="true" if detailed else None,
            dealId=deal_id,
            filter=fiql_filter,
            pageSize=page_size,
        )


@dataclass
class FetchTransactionHistoryByTypeAndPeriodArguments(Arguments):
    trans_type: TransactionType
    milliseconds: int

    def as_string(self):
        return f"/{self.trans_type}/{self.milliseconds}"


class FetchTransactionHistoryByTypeAndPeriod(RestApiCall):
    def __init__(self, trans_type: TransactionType, milliseconds: int):
        self.base_endpoint = "/history/transactions"
        self.request_type = RequestType.GET
        self.api_version = IGRestAPIVersion.ONE
        self.arguments = FetchTransactionHistoryByTypeAndPeriodArguments(
            trans_type=trans_type,
            milliseconds=milliseconds,
        )


@dataclass
class FetchTransactionHistoryData(RequestData):
    type: TransactionType | None = None
    from_: str | None = field(default=None, metadata={"json_name": "from"})
    to: str | None = None
    maxSpanSeconds: int | None = None
    pageSize: int | None = None
    pageNumber: int | None = None


class FetchTransactionHistory(RestApiCall):
    def __init__(
        self,
        trans_type: TransactionType | None = None,
        from_date: str | None = None,
        to_date: str | None = None,
        max_span_seconds: int | None = None,
        page_size: int | None = None,
        page_number: int | None = None,
    ):
        self.base_endpoint = "/history/transactions"
        self.request_type = RequestType.GET
        self.api_version = IGRestAPIVersion.TWO
        self.request_data = FetchTransactionHistoryData(
            type=trans_type,
            from_=from_date,
            to=to_date,
            maxSpanSeconds=max_span_seconds,
            pageSize=page_size,
            pageNumber=page_number,
        )


@dataclass
class FetchAccountActivityByDateArguments(Arguments):
    fromDate: datetime
    toDate: datetime

    def as_string(self):
        fmt = "%d-%m-%Y"
        return f"/{self.fromDate.strftime(fmt)}/{self.toDate.strftime(fmt)}"


class FetchAccountActivityByDate(RestApiCall):
    def __init__(
        self,
        fetch_account_acitvity_by_date_arguments: FetchAccountActivityByDateArguments,
    ):
        self.base_endpoint = "/history/activity"
        self.request_type = RequestType.GET
        self.api_version = IGRestAPIVersion.ONE

        self.arguments = fetch_account_acitvity_by_date_arguments

    def process_payload(self, payload: dict[str, Any]):
        if _HAS_PANDAS:
            return pd.DataFrame(payload["activities"])
        else:
            return payload
