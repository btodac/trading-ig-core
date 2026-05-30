from dataclasses import dataclass, field

from trading_ig.rest_api.rest_api_enums import IGRestAPIVersion, RequestType, PriceResolution
from trading_ig.rest_api.base_rest_api_call import Arguments, RestApiCall, RequestData

@dataclass
class FetchHistoricalPricesByEpicArguments(Arguments):
    epic: str

    def as_string(self):
        return f"/{self.epic}"


@dataclass
class FetchHistoricalPricesByEpicData(RequestData):
    resolution: PriceResolution | None = None
    from_: str | None = field(default=None, metadata={"json_name": "from"})
    to: str | None = None
    max: int | None = None
    pageSize: int = 20
    pageNumber: int | None = None


class FetchHistoricalPricesByEpic(RestApiCall):

    def __init__(
        self,
        epic: str,
        resolution: PriceResolution | None = None,
        start_date: str | None = None,
        end_date: str | None = None,
        numpoints: int | None = None,
        pagesize: int = 20,
        page_number: int | None = None,
    ):
        self.base_endpoint = "/prices"
        self.request_type = RequestType.GET
        self.api_version = IGRestAPIVersion.THREE
        self.arguments = FetchHistoricalPricesByEpicArguments(epic=epic)
        self.request_data = FetchHistoricalPricesByEpicData(
            resolution=resolution,
            from_=start_date,
            to=end_date,
            max=numpoints,
            pageSize=pagesize,
            pageNumber=page_number,
        )


@dataclass
class FetchHistoricalPricesByEpicAndNumPointsArguments(Arguments):
    epic: str
    resolution: PriceResolution
    numpoints: int

    def as_string(self):
        return f"/{self.epic}/{self.resolution}/{self.numpoints}"


class FetchHistoricalPricesByEpicAndNumPoints(RestApiCall):

    def __init__(self, epic: str, resolution: PriceResolution, numpoints: int):
        self.base_endpoint = "/prices"
        self.request_type = RequestType.GET
        self.api_version = IGRestAPIVersion.TWO
        self.arguments = FetchHistoricalPricesByEpicAndNumPointsArguments(
            epic=epic,
            resolution=resolution,
            numpoints=numpoints,
        )
        


@dataclass
class FetchHistoricalPricesByEpicAndDateRangeV1Data(RequestData):
    startdate: str
    enddate: str


@dataclass
class FetchHistoricalPricesByEpicAndDateRangeV1Arguments(Arguments):
    epic: str
    resolution: PriceResolution

    def as_string(self):
        return f"/{self.epic}/{self.resolution}"


class FetchHistoricalPricesByEpicAndDateRangeV1(RestApiCall):

    def __init__(
        self,
        epic: str,
        resolution: PriceResolution,
        start_date: str,
        end_date: str,
    ):
        self.base_endpoint = "/prices"
        self.request_type = RequestType.GET
        self.api_version = IGRestAPIVersion.ONE
        self.arguments = FetchHistoricalPricesByEpicAndDateRangeV1Arguments(
            epic=epic,
            resolution=resolution,
        )
        self.request_data = FetchHistoricalPricesByEpicAndDateRangeV1Data(
            startdate=start_date,
            enddate=end_date,
        )


@dataclass
class FetchHistoricalPricesByEpicAndDateRangeV2Arguments(Arguments):
    epic: str
    resolution: PriceResolution
    start_date: str
    end_date: str

    def as_string(self):
        return f"/{self.epic}/{self.resolution}/{self.start_date}/{self.end_date}"


class FetchHistoricalPricesByEpicAndDateRangeV2(RestApiCall):

    def __init__(
        self,
        epic: str,
        resolution: PriceResolution,
        start_date: str,
        end_date: str,
    ):
        self.base_endpoint = "/prices"
        self.request_type = RequestType.GET
        self.api_version = IGRestAPIVersion.TWO
        self.arguments = FetchHistoricalPricesByEpicAndDateRangeV2Arguments(
            epic=epic,
            resolution=resolution,
            start_date=start_date,
            end_date=end_date,
        )
        
