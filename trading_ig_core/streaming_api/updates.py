from pydantic.dataclasses import dataclass

from trading_ig_core.rest_api.rest_api_enums import Direction, OrderType
from trading_ig_core.streaming_api.streaming_enums import PositionStatus, DealStatus, OpenPositionStatus, TimeInForce, TradeSubscriptionFields


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
    limitLevel: float  # Number Limit level
    dealId: str  # String Deal identifier
    affectedDeals: list[AffectedDealStatus]
    stopLevel: float  # Stop level
    expiry: str  # Instrument expiry
    size: float  # Trade size
    status: PositionStatus
    epic: str  # String Instrument EPIC identifier
    level: float  # Number Trade level
    guaranteedStop: bool  # Boolean True if a guaranteed stop is in place
    dealReference: str  # String Deal reference
    dealStatus: DealStatus 	# Accepted/rejected
    repeatDealingWindow: RepeatDealingWindows


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
    channel: str  # String User channel (do not bind to this value - it will be converted to a constant enum)
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
    channel: str  # String User channel (do not bind to this value - it will be converted to a constant enum)


@dataclass
class TradeUpdate:
    CONFIRMS: TradeUpdateConfirms | None = None
    OPU: TradeUpdateOPU | None = None
    WOU: TradeUpdateWOU | None = None
