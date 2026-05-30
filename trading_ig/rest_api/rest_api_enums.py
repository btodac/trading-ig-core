from enum import IntEnum, StrEnum


class AccountTypeBaseURL(StrEnum):
    LIVE = "https://api.ig.com/gateway/deal"
    DEMO = "https://demo-api.ig.com/gateway/deal"
    

class IGRestAPIVersion(IntEnum):
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4


class RequestType(StrEnum):
    PUT = "put"
    POST = "post"
    GET = "get"
    DELETE = "delete"


class Direction(StrEnum):
    BUY = "BUY"
    SELL = "SELL"


class OrderType(StrEnum):
    MARKET = "MARKET"
    LIMIT = "LIMIT"
    QUOTE = "QUOTE"


class TimeInForce(StrEnum):
    EXECUTE_AND_ELIMINATE = "EXECUTE_AND_ELIMINATE"
    FILL_OR_KILL = "FILL_OR_KILL"
    

class TransactionType(StrEnum):
    ALL = "ALL"
    ALL_DEAL = "ALL_DEAL"
    DEPOSIT = "DEPOSIT"
    WITHDRAWAL = "WITHDRAWAL" 


class ApplicationStatus(StrEnum):
    DISABLED = "DISABLED" 	
    ENABLED = "ENABLED" 	
    REVOKED = "REVOKED"


class PriceResolution(StrEnum):
    DAY = "DAY"
    HOUR = "HOUR"
    HOUR_2 = "HOUR_2"
    HOUR_3 = "HOUR_3"
    HOUR_4 = "HOUR_4"
    MINUTE = "MINUTE"
    MINUTE_10 = "MINUTE_10"
    MINUTE_15 = "MINUTE_15"
    MINUTE_2 = "MINUTE_2"
    MINUTE_3 = "MINUTE_3"
    MINUTE_30 = "MINUTE_30"
    MINUTE_5 = "MINUTE_5"
    MONTH = "MONTH"
    SECOND = "SECOND"
    WEEK = "WEEK"


class MarketFilter(StrEnum):
    ALL = "ALL"
    SNAPSHOT_ONLY = "SNAPSHOT_ONLY"