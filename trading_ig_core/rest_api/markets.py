from typing import Any

from pydantic.dataclasses import dataclass

from trading_ig_core.rest_api.rest_api_enums import (
    IGRestAPIVersion,
    RequestType,
    MarketFilter,
)
from trading_ig_core.rest_api.base_rest_api_call import Arguments, RestApiCall, RequestData


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


from enum import StrEnum

class DealingRulesUnits(StrEnum):
    PERCENTAGE = "PERCENTAGE" 	
    POINTS = "POINTS" 	


class TrailingStopsPreference(StrEnum):
    AVAILABLE = "AVAILABLE"
    NOT_AVAILABLE = "NOT_AVAILABLE"

@dataclass
class UnitValuePair:
    unit: DealingRulesUnits
    value: float


@dataclass
class DealingRules: 	
    controlledRiskSpacing: UnitValuePair
    maxStopOrLimitDistance 	: UnitValuePair
    minControlledRiskStopDistance: UnitValuePair
    minDealSize: UnitValuePair
    minNormalStopOrLimitDistance: UnitValuePair
    minStepDistance: UnitValuePair
    trailingStopsPreference: TrailingStopsPreference


@dataclass
class Currency:
    baseExchangeRate: float  # Base exchange rate
    code: str  # Code, to be used when placing orders
    exchangeRate: float  # Exchange rate.
    isDefault: bool  # True if this is the default currency
    symbol: str  # for display purposes


class InstrumentType(StrEnum):
    BINARY = "BINARY" 	
    BUNGEE_CAPPED = "BUNGEE_CAPPED" 	
    BUNGEE_COMMODITIES = "BUNGEE_COMMODITIES" 	
    BUNGEE_CURRENCIES = "BUNGEE_CURRENCIES" 	
    BUNGEE_INDICES = "BUNGEE_INDICES" 	
    COMMODITIES = "COMMODITIES" 	
    CURRENCIES = "CURRENCIES" 	
    INDICES = "INDICES" 	
    KNOCKOUTS_COMMODITIES = "KNOCKOUTS_COMMODITIES" 	
    KNOCKOUTS_CURRENCIES = "KNOCKOUTS_CURRENCIES" 	
    KNOCKOUTS_INDICES = "KNOCKOUTS_INDICES" 	
    KNOCKOUTS_SHARES = "KNOCKOUTS_SHARES" 	
    OPT_COMMODITIES = "OPT_COMMODITIES" 	
    OPT_CURRENCIES = "OPT_CURRENCIES" 	
    OPT_INDICES = "OPT_INDICES" 	
    OPT_RATES = "OPT_RATES" 	
    OPT_SHARES = "OPT_SHARES" 	
    RATES = "RATES" 	
    SECTORS = "SECTORS" 	
    SHARES = "SHARES" 	
    SPRINT_MARKET = "SPRINT_MARKET" 	
    TEST_MARKET = "TEST_MARKET" 	
    UNKNOWN = "UNKNOWN" 


class InstrumentUnit(StrEnum):
    AMOUNT = "AMOUNT" 	
    CONTRACTS = "CONTRACTS" 	
    SHARES = "SHARES" 	

@dataclass
class InstrumentDetails:
    chartCode: str  # Chart code
    contractSize: str  # Contract size
    country: str  # Country
    currencies: list[Currency]
    epic: str  # Instrument identifier
    expiry: str  # Expiry
    limitedRiskPremium: UnitValuePair  # The limited risk premium.
    lotSize: float  # Lot size
    marketId: str  # Market identifier
    name: str  # Name
    newsCode: str  # Reuters news code
    streamingPricesAvailable: bool  # True if streaming prices are available, i.e. the market is open and the client has appropriate permissions
    limitAllowed: bool  # True if streaming is allowed
    stopAllowed: bool  # True if stops is allowed
    type_: InstrumentType
    unit: InstrumentUnit  # Unit used to qualify the size of a trade
    valueOfOnePip: str  # Value of one pip 


class MarketStatus(StrEnum):
    """Describes the current status of a given market"""
    OFFLINE = "OFFLINE"  # Offline
    CLOSED = "CLOSED"  # Closed
    SUSPENDED = "SUSPENDED"  # Suspended
    ON_AUCTION = "ON_AUCTION"  # In auction mode
    ON_AUCTION_NO_EDITS = "ON_AUCTION_NO_EDITS"  # In no-edits mode
    EDITS_ONLY = "EDITS_ONLY"  # Open for edits
    CLOSINGS_ONLY = "CLOSINGS_ONLY"  # Closings only allowed
    DEAL_NO_EDIT = "DEAL_NO_EDIT"  # Deals but not edits allowed
    TRADEABLE = "TRADEABLE"  # Open for trades


@dataclass
class PriceRung:
    bid: float
    ask: float

@dataclass
class CurrencyRung:
    currency: str  # Currency
    bidSizes: list[float]  # List of bid prices orders
    askSizes: list[float]  # List of asking prices orders 


@dataclass
class MarketSnapshot:
    decimalPlacesFactor: float  # Number of decimal positions for market levels
    delayTime: float  # Price delay
    high: float  # Highest price on the day
    low: float  # Lowest price on the day
    marketStatus: MarketStatus
    netChange: float  # Net price change on the day
    percentageChange: float  # Percentage price change on the day
    scalingFactor: float  # Multiplying factor to determine actual pip value for the levels used by the instrument
    updateTimestampUTC: float  # Time (in seconds since 1970) of last price update
    priceLadder: list[PriceRung] 	
    currencyLadders: list[CurrencyRung]

@dataclass
class MarketDetailsV4:
    dealingRules: DealingRules
    instrument: InstrumentDetails
    snapshot: MarketSnapshot


class GetMarketDetailsV4(GetMarketDetails):
    def __init__(self, epic: str):
        super().__init__(epic)
        self.api_version = IGRestAPIVersion.FOUR

    def process_payload(self, payload: dict[str, Any]):
        return MarketDetailsV4(**payload)