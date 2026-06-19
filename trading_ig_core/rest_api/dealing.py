from dataclasses import dataclass
from typing import Any

from trading_ig_core.rest_api.rest_api_enums import (
    IGRestAPIVersion,
    RequestType,
    Direction,
    OrderType,
    TimeInForce,
)
from trading_ig_core.rest_api.base_rest_api_call import Arguments, RestApiCall, RequestData


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
    dealId: str | None  # MUST SET EPIC + EXPIRY IF NONE
    direction: Direction
    size: float

    epic: str | None = None
    expiry: str | None = None

    orderType: OrderType = OrderType.MARKET
    level: float | None = None  # Do not set if orderType = MARKET
    quoteId: str | None = None  # Do not set if orderType = MARKET
    timeInForce: TimeInForce | None = None


class CloseOpenPosition(RestApiCall):
    def __init__(self, close_open_position_data: CloseOpenPositionData):
        self.base_endpoint = "/positions/otc"
        self.request_type = RequestType.DELETE
        self.api_version = IGRestAPIVersion.ONE

        self.request_data = close_open_position_data

    def process_payload(self, payload: dict[str, Any]):
        return payload["dealReference"]


@dataclass
class FetchDealByDealReferenceArguments(Arguments):
    deal_reference: str

    def as_string(self):
        return f"/{self.deal_reference}"


class FetchDealByDealReference(RestApiCall):
    def __init__(self, deal_reference: str):
        self.base_endpoint = "/confirms"
        self.request_type = RequestType.GET
        self.api_version = IGRestAPIVersion.ONE
        self.arguments = FetchDealByDealReferenceArguments(
            deal_reference=deal_reference
        )


@dataclass
class FetchOpenPositionByDealIdArguments(Arguments):
    deal_id: str

    def as_string(self):
        return f"/{self.deal_id}"


class FetchOpenPositionByDealId(RestApiCall):
    def __init__(self, deal_id: str):
        self.base_endpoint = "/positions"
        self.request_type = RequestType.GET
        self.api_version = IGRestAPIVersion.TWO
        self.arguments = FetchOpenPositionByDealIdArguments(deal_id=deal_id)


class FetchOpenPositions(RestApiCall):
    def __init__(self):
        self.base_endpoint = "/positions"
        self.request_type = RequestType.GET
        self.api_version = IGRestAPIVersion.TWO


class FetchWorkingOrders(RestApiCall):
    def __init__(self):
        self.base_endpoint = "/workingorders"
        self.request_type = RequestType.GET
        self.api_version = IGRestAPIVersion.TWO


@dataclass
class UpdateOpenPositionData(RequestData):
    limitLevel: float | None = None
    stopLevel: float | None = None
    guaranteedStop: bool = False
    trailingStop: bool = False
    trailingStopDistance: float | None = None
    trailingStopIncrement: float | None = None


@dataclass
class UpdateOpenPositionArguments(Arguments):
    deal_id: str

    def as_string(self):
        return f"/{self.deal_id}"


class UpdateOpenPosition(RestApiCall):
    def __init__(
        self,
        deal_id: str,
        limit_level: float | None = None,
        stop_level: float | None = None,
        guaranteed_stop: bool = False,
        trailing_stop: bool = False,
        trailing_stop_distance: float | None = None,
        trailing_stop_increment: float | None = None,
    ):
        self.base_endpoint = "/positions/otc"
        self.request_type = RequestType.PUT
        self.api_version = IGRestAPIVersion.TWO
        self.arguments = UpdateOpenPositionArguments(deal_id=deal_id)
        self.request_data = UpdateOpenPositionData(
            limitLevel=limit_level,
            stopLevel=stop_level,
            guaranteedStop=guaranteed_stop,
            trailingStop=trailing_stop,
            trailingStopDistance=trailing_stop_distance,
            trailingStopIncrement=trailing_stop_increment,
        )


@dataclass
class CreateWorkingOrderData(RequestData):
    currencyCode: str
    direction: Direction
    epic: str
    expiry: str
    guaranteedStop: bool
    level: float
    size: float
    type: OrderType
    timeInForce: TimeInForce | None = None
    forceOpen: bool = False
    limitDistance: float | None = None
    limitLevel: float | None = None
    stopDistance: float | None = None
    stopLevel: float | None = None
    goodTillDate: str | None = None
    dealReference: str | None = None


class CreateWorkingOrder(RestApiCall):
    def __init__(
        self,
        request_data: CreateWorkingOrderData,
    ):
        self.base_endpoint = "/working-orders/otc"
        self.request_type = RequestType.POST
        self.api_version = IGRestAPIVersion.TWO
        self.request_data = request_data


@dataclass
class DeleteWorkingOrderArguments(Arguments):
    deal_id: str

    def as_string(self):
        return f"/{self.deal_id}"


class DeleteWorkingOrder(RestApiCall):
    def __init__(self, deal_id: str):
        self.base_endpoint = "/working-orders/otc"
        self.request_type = RequestType.DELETE
        self.api_version = IGRestAPIVersion.TWO
        self.arguments = DeleteWorkingOrderArguments(deal_id=deal_id)


@dataclass
class UpdateWorkingOrderData(RequestData):
    goodTillDate: str | None = None
    limitDistance: float | None = None
    level: float | None = None
    limitLevel: float | None = None
    stopDistance: float | None = None
    stopLevel: float | None = None
    guaranteedStop: bool = False
    timeInForce: TimeInForce | None = None
    type: OrderType | None = None


@dataclass
class UpdateWorkingOrderArguments(Arguments):
    deal_id: str

    def as_string(self):
        return f"/{self.deal_id}"


class UpdateWorkingOrder(RestApiCall):
    def __init__(
        self,
        deal_id: str,
        good_till_date: str | None = None,
        level: float | None = None,
        limit_distance: float | None = None,
        limit_level: float | None = None,
        stop_distance: float | None = None,
        stop_level: float | None = None,
        guaranteed_stop: bool = False,
        time_in_force: str | None = None,
        order_type: str | None = None,
    ):
        self.base_endpoint = "/working-orders/otc"
        self.request_type = RequestType.PUT
        self.api_version = IGRestAPIVersion.TWO
        self.arguments = UpdateWorkingOrderArguments(deal_id=deal_id)
        self.request_data = UpdateWorkingOrderData(
            goodTillDate=good_till_date,
            level=level,
            limitDistance=limit_distance,
            limitLevel=limit_level,
            stopDistance=stop_distance,
            stopLevel=stop_level,
            guaranteedStop=guaranteed_stop,
            timeInForce=time_in_force,
            type=order_type,
        )


@dataclass
class FetchRepeatDealingWindowData(RequestData):
    epic: str | None = None


class FetchRepeatDealingWindow(RestApiCall):
    def __init__(self, epic: str | None = None):
        self.base_endpoint = "/repeat-dealing-window"
        self.request_type = RequestType.GET
        self.api_version = IGRestAPIVersion.ONE
        self.request_data = FetchRepeatDealingWindowData(epic=epic)
