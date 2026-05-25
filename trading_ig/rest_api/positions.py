from dataclasses import dataclass
from typing import Any

from trading_ig.rest_api.api_enums import IGRestAPIVersion, RequestType, Direction, OrderType, TimeInForce
from trading_ig.rest_api.base_rest_api_call import Arguments, RestApiCall, RequestData


@dataclass
class CreateOpenPositionData(RequestData):
    currencyCode: str
    direction: Direction
    epic: str
    expiry: str
    forceOpen: bool
    guaranteedStop: bool
    size: float

    level: float | None = None
    limitDistance: float | None = None
    limitLevel: float | None = None
    orderType: OrderType = OrderType.MARKET
    quoteId: str | None = None
    stopDistance: float | None = None
    stopLevel: float | None = None
    timeInForce: TimeInForce | None = None
    trailingStop: bool = False
    trailingStopIncrement: float | None = None


class CreateOpenPosition(RestApiCall):
    
    def __init__(self, create_open_position_data: CreateOpenPositionData):
        self.base_endpoint = "/positions/otc"
        self.request_type = RequestType.POST
        self.api_version = IGRestAPIVersion.TWO
    
        self.request_data = create_open_position_data

    def process_payload(self, payload: dict[str, Any]):
        return payload["dealReference"]


@dataclass
class CloseOpenPositionData(RequestData):
    dealId: str
    direction: Direction
    epic: str
    expiry: str
    size: float

    level: float | None = None
    orderType: OrderType = OrderType.MARKET
    quoteId: str | None = None
    timeInForce: TimeInForce | None = None


class CloseOpenPosition(RestApiCall):
    
    def __init__(self, close_open_position_data: CloseOpenPositionData):
        self.base_endpoint = "/positions/otc"
        self.request_type = RequestType.DELETE
        self.api_version = IGRestAPIVersion.ONE
    
        self.request_data = close_open_position_data

    def process_payload(self, payload: dict[str, Any]):
        return payload["dealReference"]
    
