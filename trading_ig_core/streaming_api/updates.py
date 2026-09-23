from pydantic.dataclasses import dataclass

from trading_ig_core.rest_api import Direction, OrderType
from trading_ig_core.streaming_api.streaming_enums import (
    DealStatus,
    OpenPositionStatus,
    PositionStatus,
    TimeInForce,
)


@dataclass
class AffectedDealStatus:
    dealId: str
    status: PositionStatus


@dataclass
class RepeatDealingWindow:
    size: float
    expiry: int  # Timestamp


@dataclass
class RepeatDealingWindows:
    entries: list[RepeatDealingWindow]


@dataclass
class TradeUpdateConfirms:
    direction: Direction  # Constant BUY, SELL
    limitLevel: float | None  # Number Limit level
    dealId: str  # String Deal identifier
    affectedDeals: list[AffectedDealStatus]
    stopLevel: float | None  # Stop level
    expiry: str | None  # Instrument expiry
    size: float | None  # Trade size
    status: PositionStatus | None
    epic: str  # String Instrument EPIC identifier
    level: float | None  # Number Trade level
    guaranteedStop: bool  # Boolean True if a guaranteed stop is in place
    dealReference: str  # String Deal reference
    dealStatus: DealStatus 	# Accepted/rejected
    repeatDealingWindow: RepeatDealingWindows | None = None


@dataclass
class TradeUpdateOPU:
    """Openposition updates for an account"""
    dealReference: str  # String Deal reference
    dealId: str  # String Deal identifier
    direction: Direction  # Constant BUY, SELL
    epic: str  # String Instrument EPIC identifier
    status: OpenPositionStatus
    dealStatus: DealStatus
    level: float  # Number Trade level
    size: float  # Number Trade size
    currency: str  # String Currency
    timestamp: str  # Date Event date and time
    # String User channel (do not bind to this value - it will be converted to a constant enum)
    channel: str  
    dealIdOrigin: str  # String Deal identifier of the originating deal    
    expiry: str  # String Instrument expiry
    openLevel: float
    stopLevel: float  # Number Stop level
    limitLevel: float  # Number Limit level
    guaranteedStop: bool  # Boolean True if a guaranteed stop is in place
    trailingStopDistance: float | None = None  # Number Trailing stop distance
    trailingStep: float | None = None  # Number Trailing stop increment


@dataclass
class TradeUpdateWOU:
    """Working order updates for an account"""
    direction: Direction  # Constant BUY, SELL
    limitDistance: float  # Number Limit distance
    dealId: str  # String Deal identifier
    stopDistance: float  # Number Stop distance
    expiry: str  # String Instrument expiry
    timestamp: str  # Date Event date and time
    size: float  # Number Trade size
    status: OpenPositionStatus  # Working order status
    epic: str  # String Instrument EPIC identifier
    level: float  # Number Trade level
    guaranteedStop: bool  # Boolean True if a guaranteed stop is in place
    dealReference: str  # String Deal reference
    dealStatus: DealStatus  
    currency: str  # String Currency
    orderType: OrderType  # LiMIT or STOP
    timeInForce: TimeInForce
    goodTillDate: str  # Date Good until specified date
    # String User channel (do not bind to this value - it will be converted to a constant enum)
    channel: str  


@dataclass
class TradeUpdate:
    CONFIRMS: TradeUpdateConfirms | None = None
    OPU: TradeUpdateOPU | None = None
    WOU: TradeUpdateWOU | None = None
