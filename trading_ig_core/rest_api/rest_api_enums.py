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


class AccountStatus(StrEnum):
    DISABLED = "DISABLED"  # Disabled
    ENABLED = "ENABLED"  # Enabled
    SUSPENDED_FROM_DEALING = "SUSPENDED_FROM_DEALING"  # Suspended from dealing


class ReroutingEnvironment(StrEnum):
    DEMO = "DEMO"
    LIVE = "LIVE"
    TEST = "TEST"
    UAT = "UAT"


class RejectionReasons(StrEnum):
    # The account is not enabled to trade
    ACCOUNT_NOT_ENABLED_TO_TRADING = "ACCOUNT_NOT_ENABLED_TO_TRADING"
    # The level of the attached stop or limit is not valid
    ATTACHED_ORDER_LEVEL_ERROR = "ATTACHED_ORDER_LEVEL_ERROR"
    # The trailing stop value is invalid
    ATTACHED_ORDER_TRAILING_STOP_ERROR = "ATTACHED_ORDER_TRAILING_STOP_ERROR"
    # Cannot change the stop type.
    CANNOT_CHANGE_STOP_TYPE = "CANNOT_CHANGE_STOP_TYPE"
    # Cannot remove the stop.
    CANNOT_REMOVE_STOP = "CANNOT_REMOVE_STOP"
    # We are not taking opening deals on a Controlled Risk basis on this market
    CLOSING_ONLY_TRADES_ACCEPTED_ON_THIS_MARKET = "CLOSING_ONLY_TRADES_ACCEPTED_ON_THIS_MARKET"
    # You are currently restricted from opening any new positions on your account.
    CLOSINGS_ONLY_ACCOUNT = "CLOSINGS_ONLY_ACCOUNT"
    # Resubmitted request does not match the original order.
    CONFLICTING_ORDER = "CONFLICTING_ORDER"
    # Instrument has an error - check the order's currency is the instrument's currency (see the 
    # market's details); otherwise please contact support.
    CONTACT_SUPPORT_INSTRUMENT_ERROR = "CONTACT_SUPPORT_INSTRUMENT_ERROR"
    # Sorry we are unable to process this order. The stop or limit level you have requested is not a
    # valid trading level in the underlying market.
    CR_SPACING = "CR_SPACING"
    # The order has been rejected as it is a duplicate of a previously issued order
    DUPLICATE_ORDER_ERROR = "DUPLICATE_ORDER_ERROR"
    # Exchange check failed. Please call in for assistance.
    EXCHANGE_MANUAL_OVERRIDE = "EXCHANGE_MANUAL_OVERRIDE"
    # Order expiry is less than the sprint market's minimum expiry. Check the sprint market's market
    # details for the allowable expiries.
    EXPIRY_LESS_THAN_SPRINT_MARKET_MIN_EXPIRY = "EXPIRY_LESS_THAN_SPRINT_MARKET_MIN_EXPIRY"
    # The total size of deals placed on this market in a short period has exceeded our limits. 
    # Please wait before attempting to open further positions on this market.
    FINANCE_REPEAT_DEALING = "FINANCE_REPEAT_DEALING"
    # Ability to force open in different currencies on same market not allowed
    FORCE_OPEN_ON_SAME_MARKET_DIFFERENT_CURRENCY = "FORCE_OPEN_ON_SAME_MARKET_DIFFERENT_CURRENCY"
    # an error has occurred but no detailed information is available. Check transaction history or 
    # contact support for further information
    GENERAL_ERROR = "GENERAL_ERROR"
    # The working order has been set to expire on a past date
    GOOD_TILL_DATE_IN_THE_PAST = "GOOD_TILL_DATE_IN_THE_PAST"
    # The requested market was not found
    INSTRUMENT_NOT_FOUND = "INSTRUMENT_NOT_FOUND"
    # Instrument not tradeable in this currency.
    INSTRUMENT_NOT_TRADEABLE_IN_THIS_CURRENCY = "INSTRUMENT_NOT_TRADEABLE_IN_THIS_CURRENCY"
    # The account has not enough funds available for the requested trade
    INSUFFICIENT_FUNDS = "INSUFFICIENT_FUNDS"
    # The market level has moved and has been rejected
    LEVEL_TOLERANCE_ERROR = "LEVEL_TOLERANCE_ERROR"
    # The deal has been rejected because the limit level is inconsistent with current market price 
    # given the direction.
    LIMIT_ORDER_WRONG_SIDE_OF_MARKET = "LIMIT_ORDER_WRONG_SIDE_OF_MARKET"
    # The manual order timeout limit has been reached
    MANUAL_ORDER_TIMEOUT = "MANUAL_ORDER_TIMEOUT"
    # Order declined during margin checks Check available funds.
    MARGIN_ERROR = "MARGIN_ERROR"
    # The market is currently closed
    MARKET_CLOSED = "MARKET_CLOSED"
    # The market is currently closed with edits
    MARKET_CLOSED_WITH_EDITS = "MARKET_CLOSED_WITH_EDITS"
    # The epic is due to expire shortly, client should deal in the next available contract.
    MARKET_CLOSING = "MARKET_CLOSING"
    # The market does not allow opening shorting positions
    MARKET_NOT_BORROWABLE = "MARKET_NOT_BORROWABLE"
    # The market is currently offline
    MARKET_OFFLINE = "MARKET_OFFLINE"
    # The epic does not support 'Market' order type
    MARKET_ORDERS_NOT_ALLOWED_ON_INSTRUMENT = "MARKET_ORDERS_NOT_ALLOWED_ON_INSTRUMENT"
    # The market can only be traded over the phone
    MARKET_PHONE_ONLY = "MARKET_PHONE_ONLY"
    # The market has been rolled to the next period
    MARKET_ROLLED = "MARKET_ROLLED"
    # The requested market is not allowed to this account
    MARKET_UNAVAILABLE_TO_CLIENT = "MARKET_UNAVAILABLE_TO_CLIENT"
    # The order size exceeds the instrument's maximum configured value for auto-hedging the exposure
    # of a deal
    MAX_AUTO_SIZE_EXCEEDED = "MAX_AUTO_SIZE_EXCEEDED"
    # The order size is too small
    MINIMUM_ORDER_SIZE_ERROR = "MINIMUM_ORDER_SIZE_ERROR"
    # The limit level you have requested is closer to the market level than the existing stop. When 
    # the market is closed you can only move the limit order further away from the current market 
    # level.
    MOVE_AWAY_ONLY_LIMIT = "MOVE_AWAY_ONLY_LIMIT"
    # The stop level you have requested is closer to the market level than the existing stop level. 
    # When the market is closed you can only move the stop level further away from the current 
    # market level
    MOVE_AWAY_ONLY_STOP = "MOVE_AWAY_ONLY_STOP"
    # The order level you have requested is moving closer to the market level than the exisiting 
    # order level. When the market is closed you can only move the order further away from the 
    # current market level.
    MOVE_AWAY_ONLY_TRIGGER_LEVEL = "MOVE_AWAY_ONLY_TRIGGER_LEVEL"
    # You are not permitted to open a non-controlled risk position on this account.
    NCR_POSITIONS_ON_CR_ACCOUNT = "NCR_POSITIONS_ON_CR_ACCOUNT"
    # Opening CR position in opposite direction to existing CR position not allowed.
    OPPOSING_DIRECTION_ORDERS_NOT_ALLOWED = "OPPOSING_DIRECTION_ORDERS_NOT_ALLOWED"
    # The deal has been rejected to avoid having long and short open positions on the same market or
    # having long and short open positions and working orders on the same epic
    OPPOSING_POSITIONS_NOT_ALLOWED = "OPPOSING_POSITIONS_NOT_ALLOWED"
    # Order declined; please contact Support
    ORDER_DECLINED = "ORDER_DECLINED"
    # The order is locked and cannot be edited by the user
    ORDER_LOCKED = "ORDER_LOCKED"
    # The order has not been found
    ORDER_NOT_FOUND = "ORDER_NOT_FOUND"
    # The order size cannot be filled at this price at the moment.
    ORDER_SIZE_CANNOT_BE_FILLED = "ORDER_SIZE_CANNOT_BE_FILLED"
    # The total position size at this stop level is greater than the size allowed on this market. 
    # Please reduce the size of the order.
    OVER_NORMAL_MARKET_SIZE = "OVER_NORMAL_MARKET_SIZE"
    # Position cannot be deleted as it has been partially closed.
    PARTIALY_CLOSED_POSITION_NOT_DELETED = "PARTIALY_CLOSED_POSITION_NOT_DELETED"
    # The deal has been rejected because of an existing position. Either set the 'force open' to be 
    # true or cancel opposing position
    POSITION_ALREADY_EXISTS_IN_OPPOSITE_DIRECTION = "POSITION_ALREADY_EXISTS_IN_OPPOSITE_DIRECTION"
    # Position cannot be cancelled. Check transaction history or contact support for further 
    # information.
    POSITION_NOT_AVAILABLE_TO_CANCEL = "POSITION_NOT_AVAILABLE_TO_CANCEL"
    # Cannot close this position. Either the position no longer exists, or the size available to 
    # close is less than the size specified.
    POSITION_NOT_AVAILABLE_TO_CLOSE = "POSITION_NOT_AVAILABLE_TO_CLOSE"
    # The position has not been found
    POSITION_NOT_FOUND = "POSITION_NOT_FOUND"
    # Invalid attempt to submit a CFD trade on a spreadbet account
    REJECT_CFD_ORDER_ON_SPREADBET_ACCOUNT = "REJECT_CFD_ORDER_ON_SPREADBET_ACCOUNT"
    # Invalid attempt to submit a spreadbet trade on a CFD account
    REJECT_SPREADBET_ORDER_ON_CFD_ACCOUNT = "REJECT_SPREADBET_ORDER_ON_CFD_ACCOUNT"
    # Order size is not an increment of the value specified for the market.
    SIZE_INCREMENT = "SIZE_INCREMENT"
    # The expiry of the position would have fallen after the closing time of the market
    SPRINT_MARKET_EXPIRY_AFTER_MARKET_CLOSE = "SPRINT_MARKET_EXPIRY_AFTER_MARKET_CLOSE"
    # The market does not allow stop or limit attached orders
    STOP_OR_LIMIT_NOT_ALLOWED = "STOP_OR_LIMIT_NOT_ALLOWED"
    # The order requires a stop
    STOP_REQUIRED_ERROR = "STOP_REQUIRED_ERROR"
    # The submitted strike level is invalid
    STRIKE_LEVEL_TOLERANCE = "STRIKE_LEVEL_TOLERANCE"
    # The operation completed successfully
    SUCCESS = "SUCCESS"
    # The market or the account do not allow for trailing stops
    TRAILING_STOP_NOT_ALLOWED = "TRAILING_STOP_NOT_ALLOWED"
    # The operation resulted in an unknown result condition. Check transaction history or contact 
    # support for further information
    UNKNOWN = "UNKNOWN"
    # The requested operation has been attempted on the wrong direction
    WRONG_SIDE_OF_MARKET = "WRONG_SIDE_OF_MARKET"