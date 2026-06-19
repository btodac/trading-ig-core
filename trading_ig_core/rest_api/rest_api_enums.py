from enum import IntEnum, StrEnum


class Gateway(StrEnum):
    LIVE = "LIVE" 
    DEMO = "DEMO"
    
    @property
    def url(self):
        match self.value:
            case Gateway.LIVE:
                url = "https://api.ig.com/gateway/deal"
            case Gateway.DEMO:
                url = "https://demo-api.ig.com/gateway/deal"
        return url


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
    STOP = "STOP"


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


class AccountType(StrEnum):
    CFD = "CFD"
    PHYSICAL = "PHYSICAL"
    SPREADBET = "SPREADBET"


class ReroutingEnvironment(StrEnum):
    DEMO = "DEMO"
    LIVE = "LIVE"
    TEST = "TEST"
    UAT = "UAT"


class RejectionReasons(StrEnum):
    ACCOUNT_NOT_ENABLED_TO_TRADING = "ACCOUNT_NOT_ENABLED_TO_TRADING"  # The account is not enabled to trade
    ATTACHED_ORDER_LEVEL_ERROR = "ATTACHED_ORDER_LEVEL_ERROR"  # The level of the attached stop or limit is not valid
    ATTACHED_ORDER_TRAILING_STOP_ERROR = "ATTACHED_ORDER_TRAILING_STOP_ERROR"  # The trailing stop value is invalid
    CANNOT_CHANGE_STOP_TYPE = "CANNOT_CHANGE_STOP_TYPE"  # Cannot change the stop type.
    CANNOT_REMOVE_STOP = "CANNOT_REMOVE_STOP"  # Cannot remove the stop.
    CLOSING_ONLY_TRADES_ACCEPTED_ON_THIS_MARKET = "CLOSING_ONLY_TRADES_ACCEPTED_ON_THIS_MARKET"  # We are not taking opening deals on a Controlled Risk basis on this market
    CLOSINGS_ONLY_ACCOUNT = "CLOSINGS_ONLY_ACCOUNT"  # You are currently restricted from opening any new positions on your account.
    CONFLICTING_ORDER = "CONFLICTING_ORDER"  # Resubmitted request does not match the original order.
    CONTACT_SUPPORT_INSTRUMENT_ERROR = "CONTACT_SUPPORT_INSTRUMENT_ERROR"  # Instrument has an error - check the order's currency is the instrument's currency (see the market's details); otherwise please contact support.
    CR_SPACING = "CR_SPACING"  # Sorry we are unable to process this order. The stop or limit level you have requested is not a valid trading level in the underlying market.
    DUPLICATE_ORDER_ERROR = "DUPLICATE_ORDER_ERROR"  # The order has been rejected as it is a duplicate of a previously issued order
    EXCHANGE_MANUAL_OVERRIDE = "EXCHANGE_MANUAL_OVERRIDE"  # Exchange check failed. Please call in for assistance.
    EXPIRY_LESS_THAN_SPRINT_MARKET_MIN_EXPIRY = "EXPIRY_LESS_THAN_SPRINT_MARKET_MIN_EXPIRY"  # Order expiry is less than the sprint market's minimum expiry. Check the sprint market's market details for the allowable expiries.
    FINANCE_REPEAT_DEALING = "FINANCE_REPEAT_DEALING"  # The total size of deals placed on this market in a short period has exceeded our limits. Please wait before attempting to open further positions on this market.
    FORCE_OPEN_ON_SAME_MARKET_DIFFERENT_CURRENCY = "FORCE_OPEN_ON_SAME_MARKET_DIFFERENT_CURRENCY"  # Ability to force open in different currencies on same market not allowed
    GENERAL_ERROR = "GENERAL_ERROR"  # an error has occurred but no detailed information is available. Check transaction history or contact support for further information
    GOOD_TILL_DATE_IN_THE_PAST = "GOOD_TILL_DATE_IN_THE_PAST"  # The working order has been set to expire on a past date
    INSTRUMENT_NOT_FOUND = "INSTRUMENT_NOT_FOUND"  # The requested market was not found
    INSTRUMENT_NOT_TRADEABLE_IN_THIS_CURRENCY = "INSTRUMENT_NOT_TRADEABLE_IN_THIS_CURRENCY"  # Instrument not tradeable in this currency.
    INSUFFICIENT_FUNDS = "INSUFFICIENT_FUNDS"  # The account has not enough funds available for the requested trade
    LEVEL_TOLERANCE_ERROR = "LEVEL_TOLERANCE_ERROR"  # The market level has moved and has been rejected
    LIMIT_ORDER_WRONG_SIDE_OF_MARKET = "LIMIT_ORDER_WRONG_SIDE_OF_MARKET"  # The deal has been rejected because the limit level is inconsistent with current market price given the direction.
    MANUAL_ORDER_TIMEOUT = "MANUAL_ORDER_TIMEOUT"  # The manual order timeout limit has been reached
    MARGIN_ERROR = "MARGIN_ERROR"  # Order declined during margin checks Check available funds.
    MARKET_CLOSED = "MARKET_CLOSED"  # The market is currently closed
    MARKET_CLOSED_WITH_EDITS = "MARKET_CLOSED_WITH_EDITS"  # The market is currently closed with edits
    MARKET_CLOSING = "MARKET_CLOSING"  # The epic is due to expire shortly, client should deal in the next available contract.
    MARKET_NOT_BORROWABLE = "MARKET_NOT_BORROWABLE"  # The market does not allow opening shorting positions
    MARKET_OFFLINE = "MARKET_OFFLINE"  # The market is currently offline
    MARKET_ORDERS_NOT_ALLOWED_ON_INSTRUMENT = "MARKET_ORDERS_NOT_ALLOWED_ON_INSTRUMENT"  # The epic does not support 'Market' order type
    MARKET_PHONE_ONLY = "MARKET_PHONE_ONLY"  # The market can only be traded over the phone
    MARKET_ROLLED = "MARKET_ROLLED"  # The market has been rolled to the next period
    MARKET_UNAVAILABLE_TO_CLIENT = "MARKET_UNAVAILABLE_TO_CLIENT"  # The requested market is not allowed to this account
    MAX_AUTO_SIZE_EXCEEDED = "MAX_AUTO_SIZE_EXCEEDED"  # The order size exceeds the instrument's maximum configured value for auto-hedging the exposure of a deal
    MINIMUM_ORDER_SIZE_ERROR = "MINIMUM_ORDER_SIZE_ERROR"  # The order size is too small
    MOVE_AWAY_ONLY_LIMIT = "MOVE_AWAY_ONLY_LIMIT"  # The limit level you have requested is closer to the market level than the existing stop. When the market is closed you can only move the limit order further away from the current market level.
    MOVE_AWAY_ONLY_STOP = "MOVE_AWAY_ONLY_STOP"  # The stop level you have requested is closer to the market level than the existing stop level. When the market is closed you can only move the stop level further away from the current market level
    MOVE_AWAY_ONLY_TRIGGER_LEVEL = "MOVE_AWAY_ONLY_TRIGGER_LEVEL"  # The order level you have requested is moving closer to the market level than the exisiting order level. When the market is closed you can only move the order further away from the current market level.
    NCR_POSITIONS_ON_CR_ACCOUNT = "NCR_POSITIONS_ON_CR_ACCOUNT"  # You are not permitted to open a non-controlled risk position on this account.
    OPPOSING_DIRECTION_ORDERS_NOT_ALLOWED = "OPPOSING_DIRECTION_ORDERS_NOT_ALLOWED"  # Opening CR position in opposite direction to existing CR position not allowed.
    OPPOSING_POSITIONS_NOT_ALLOWED = "OPPOSING_POSITIONS_NOT_ALLOWED"  # The deal has been rejected to avoid having long and short open positions on the same market or having long and short open positions and working orders on the same epic
    ORDER_DECLINED = "ORDER_DECLINED"  # Order declined; please contact Support
    ORDER_LOCKED = "ORDER_LOCKED"  # The order is locked and cannot be edited by the user
    ORDER_NOT_FOUND = "ORDER_NOT_FOUND"  # The order has not been found
    ORDER_SIZE_CANNOT_BE_FILLED = "ORDER_SIZE_CANNOT_BE_FILLED"  # The order size cannot be filled at this price at the moment.
    OVER_NORMAL_MARKET_SIZE = "OVER_NORMAL_MARKET_SIZE"  # The total position size at this stop level is greater than the size allowed on this market. Please reduce the size of the order.
    PARTIALY_CLOSED_POSITION_NOT_DELETED = "PARTIALY_CLOSED_POSITION_NOT_DELETED"  # Position cannot be deleted as it has been partially closed.
    POSITION_ALREADY_EXISTS_IN_OPPOSITE_DIRECTION = "POSITION_ALREADY_EXISTS_IN_OPPOSITE_DIRECTION"  # The deal has been rejected because of an existing position. Either set the 'force open' to be true or cancel opposing position
    POSITION_NOT_AVAILABLE_TO_CANCEL = "POSITION_NOT_AVAILABLE_TO_CANCEL"  # Position cannot be cancelled. Check transaction history or contact support for further information.
    POSITION_NOT_AVAILABLE_TO_CLOSE = "POSITION_NOT_AVAILABLE_TO_CLOSE"  # Cannot close this position. Either the position no longer exists, or the size available to close is less than the size specified.
    POSITION_NOT_FOUND = "POSITION_NOT_FOUND"  # The position has not been found
    REJECT_CFD_ORDER_ON_SPREADBET_ACCOUNT = "REJECT_CFD_ORDER_ON_SPREADBET_ACCOUNT"  # Invalid attempt to submit a CFD trade on a spreadbet account
    REJECT_SPREADBET_ORDER_ON_CFD_ACCOUNT = "REJECT_SPREADBET_ORDER_ON_CFD_ACCOUNT"  # Invalid attempt to submit a spreadbet trade on a CFD account
    SIZE_INCREMENT = "SIZE_INCREMENT"  # Order size is not an increment of the value specified for the market.
    SPRINT_MARKET_EXPIRY_AFTER_MARKET_CLOSE = "SPRINT_MARKET_EXPIRY_AFTER_MARKET_CLOSE"  # The expiry of the position would have fallen after the closing time of the market
    STOP_OR_LIMIT_NOT_ALLOWED = "STOP_OR_LIMIT_NOT_ALLOWED"  # The market does not allow stop or limit attached orders
    STOP_REQUIRED_ERROR = "STOP_REQUIRED_ERROR"  # The order requires a stop
    STRIKE_LEVEL_TOLERANCE = "STRIKE_LEVEL_TOLERANCE"  # The submitted strike level is invalid
    SUCCESS = "SUCCESS"  # The operation completed successfully
    TRAILING_STOP_NOT_ALLOWED = "TRAILING_STOP_NOT_ALLOWED"  # The market or the account do not allow for trailing stops
    UNKNOWN = "UNKNOWN"  # The operation resulted in an unknown result condition. Check transaction history or contact support for further information
    WRONG_SIDE_OF_MARKET = "WRONG_SIDE_OF_MARKET"  # The requested operation has been attempted on the wrong direction