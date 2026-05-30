from dataclasses import dataclass

from trading_ig.rest_api.rest_api_enums import (
    IGRestAPIVersion,
    RequestType,
    MarketFilter,
)
from trading_ig.rest_api.base_rest_api_call import Arguments, RestApiCall, RequestData


class FetchTopLevelNavigationNodes(RestApiCall):
    def __init__(self):
        self.base_endpoint = "/marketnavigation"
        self.request_type = RequestType.GET
        self.api_version = IGRestAPIVersion.ONE


@dataclass
class GetMarketDetailsArguments(Arguments):
    epic: str

    def as_string(self):
        return f"/{self.epic}"


class GetMarketDetails(RestApiCall):
    def __init__(self, epic: str):
        self.base_endpoint = "/markets"
        self.request_type = RequestType.GET
        self.api_version = IGRestAPIVersion.ONE
        self.arguments = GetMarketDetailsArguments(epic=epic)


class GetMarketDetailsV2(GetMarketDetails):
    def __init__(self, epic: str):
        super().__init__(epic)
        self.api_version = IGRestAPIVersion.TWO


class GetMarketDetailsV3(GetMarketDetails):
    def __init__(self, epic: str):
        super().__init__(epic)
        self.api_version = IGRestAPIVersion.THREE


class GetMarketDetailsV4(GetMarketDetails):
    def __init__(self, epic: str):
        super().__init__(epic)
        self.api_version = IGRestAPIVersion.FOUR


@dataclass
class FetchMarketsByEpicsData(RequestData):
    epics: str
    filter: str | None = None


class FetchMarketsByEpics(RestApiCall):
    def __init__(self, epics: str, detailed: bool = True):
        self.base_endpoint = "/markets"
        self.request_type = RequestType.GET
        self.api_version = IGRestAPIVersion.TWO
        self.request_data = FetchMarketsByEpicsData(
            epics=epics,
            filter="ALL" if detailed else "SNAPSHOT_ONLY",
        )


@dataclass
class SearchMarketsData(RequestData):
    epics: str


class SearchMarkets(RestApiCall):
    def __init__(self, epics: str):
        self.base_endpoint = "/markets"
        self.request_type = RequestType.GET
        self.api_version = IGRestAPIVersion.ONE
        self.request_data = SearchMarketsData(epics=epics)


@dataclass
class SearchMarketsV2Data(RequestData):
    epics: str
    filter: MarketFilter | None = None


class SearchMarketsV2(RestApiCall):
    def __init__(self, epics: str):
        self.base_endpoint = "/markets"
        self.request_type = RequestType.GET
        self.api_version = IGRestAPIVersion.TWO
        self.request_data = SearchMarketsV2Data(epics=epics)
