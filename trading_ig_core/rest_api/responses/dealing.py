from pydantic.dataclasses import dataclass

from trading_ig_core.rest_api.base_rest_api_call import RestAPIResponse
from trading_ig_core.rest_api.rest_api_enums import Direction, RejectionReasons
from trading_ig_core.streaming_api.updates import (
    AffectedDealStatus,
    DealStatus,
    PositionStatus,
)


@dataclass
class DealConfirmation(RestAPIResponse):
    affectedDeals: list[AffectedDealStatus]
    date: str  # Transaction date
    dealId: str  # Deal identifier
    dealReference: str  # Deal reference
    dealStatus: DealStatus
    direction: Direction
    epic: str  # Instrument epic identifier
    guaranteedStop: bool  # True if guaranteed stop
    trailingStop: bool  # True if trailing stop
    reason: RejectionReasons  # Describes the error (or success) condition for the deal
    status: PositionStatus | None  # Position status
    size: float | None  # Size
    expiry: str | None  # Instrument expiry
    level: float | None  # Level
    limitLevel: float | None  # Limit level
    stopLevel: float | None  # Stop level
    profit: float | None  # Profit
    profitCurrency: str | None  # Profit currency
    limitDistance: float | None  # Limit distance
    stopDistance: float | None  # Stop distance
    
