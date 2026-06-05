from enum import StrEnum

class StreamModes(StrEnum):
    MERGE = "MERGE"
    DISTINCT = "DISTINCT"


class PriceSubscriptionFields:
    MID_OPEN = "MID_OPEN"  # Opening mid price
    HIGH = "HIGH"  # Intraday high price
    LOW = "LOW"  # Intraday low price
    BIDQUOTEID = "BIDQUOTEID"  # ID of bid quote to reference when trading
    ASKQUOTEID = "ASKQUOTEID"  # ID of ask quote to reference when trading
    BIDPRICE1 = "BIDPRICE1"  # The bid price of the top tier of the ladder
    BIDPRICE2 = "BIDPRICE2"  # Ladder tier prices
    BIDPRICE3 = "BIDPRICE3"    	
    BIDPRICE4 = "BIDPRICE4"    	
    BIDPRICE5 = "BIDPRICE5"    	
    ASKPRICE1 = "ASKPRICE1"  # The ask price of the top tier of the ladder
    ASKPRICE2 = "ASKPRICE2"  # Ladder tier prices
    ASKPRICE3 = "ASKPRICE3"    	
    ASKPRICE4 = "ASKPRICE4"    	
    ASKPRICE5 = "ASKPRICE5"    	
    BIDSIZE1 = "BIDSIZE1"  # Size available at the 1st tier price
    # If not present then the ladder is not configured for this instrument.
    BIDSIZE2 = "BIDSIZE2" 	# Ladder tier sizes
    BIDSIZE3 = "BIDSIZE3" 	
    BIDSIZE4 = "BIDSIZE4" 	
    BIDSIZE5 = "BIDSIZE5" 	
    ASKSIZE1 = "ASKSIZE1"  # Size available at the 1st tier price
    # If not present then the ladder is not configured for this instrument.
    ASKSIZE2 = "ASKSIZE2" 	# Ladder tier sizes
    ASKSIZE3 = "ASKSIZE3" 	
    ASKSIZE4 = "ASKSIZE4" 	
    ASKSIZE5 = "ASKSIZE5" 	
    CURRENCY0 = "CURRENCY0"  # The currency of the default ladder
    CURRENCY1 = "CURRENCY1"  # Currency for the ladder fields prefixed C1
    CURRENCY2 = "CURRENCY2"  # Currency for the ladder fields prefixed C2
    CURRENCY3 = "CURRENCY3"  # Currency for the ladder fields prefixed C3
    CURRENCY4 = "CURRENCY4"  # Currency for the ladder fields prefixed C4
    CURRENCY5 = "CURRENCY5"  # Currency for the ladder fields prefixed C5
    # This is only guaranteed to be populated if there is a ladder, ie one or more ASKSIZE1-5 and BIDSIZE1-5 is populated
    C1BIDSIZE1 = "C1BIDSIZE1"  # The bid trading size threshold
    C1ASKSIZE1 = "C1ASKSIZE1"  # The ask trading size threshold
    C2BIDSIZE1 = "C2BIDSIZE1"  # The bid trading size threshold
    C2ASKSIZE1 = "C2ASKSIZE1"  # The ask trading size threshold
    C3BIDSIZE1 = "C3BIDSIZE1"  # The bid trading size threshold
    C3ASKSIZE1 = "C3ASKSIZE1"  # The ask trading size threshold
    C4BIDSIZE1 = "C4BIDSIZE1"  # The bid trading size threshold
    C4ASKSIZE1 = "C4ASKSIZE1"  # The ask trading size threshold
    C5BIDSIZE1 = "C5BIDSIZE1"  # The bid trading size threshold
    C5ASKSIZE1 = "C5ASKSIZE1"  # The ask trading size threshold
    C1BIDSIZE2 = "C1BIDSIZE2"  # The bid trading size threshold
    C1ASKSIZE2 = "C1ASKSIZE2"  # The ask trading size threshold
    C2BIDSIZE2 = "C2BIDSIZE2"  # The bid trading size threshold
    C2ASKSIZE2 = "C2ASKSIZE2"  # The ask trading size threshold
    C3BIDSIZE2 = "C3BIDSIZE2"  # The bid trading size threshold
    C3ASKSIZE2 = "C3ASKSIZE2"  # The ask trading size threshold
    C4BIDSIZE2 = "C4BIDSIZE2"  # The bid trading size threshold
    C4ASKSIZE2 = "C4ASKSIZE2"  # The ask trading size threshold
    C5BIDSIZE2 = "C5BIDSIZE2"  # The bid trading size threshold
    C5ASKSIZE2 = "C5ASKSIZE2"  # The ask trading size threshold
    C1BIDSIZE3 = "C1BIDSIZE3"  # The bid trading size threshold
    C1ASKSIZE3 = "C1ASKSIZE3"  # The ask trading size threshold
    C2BIDSIZE3 = "C2BIDSIZE3"  # The bid trading size threshold
    C2ASKSIZE3 = "C2ASKSIZE3"  # The ask trading size threshold
    C3BIDSIZE3 = "C3BIDSIZE3"  # The bid trading size threshold
    C3ASKSIZE3 = "C3ASKSIZE3"  # The ask trading size threshold
    C4BIDSIZE3 = "C4BIDSIZE3"  # The bid trading size threshold
    C4ASKSIZE3 = "C4ASKSIZE3"  # The ask trading size threshold
    C5BIDSIZE3 = "C5BIDSIZE3"  # The bid trading size threshold
    C5ASKSIZE3 = "C5ASKSIZE3"  # The ask trading size threshold
    C1BIDSIZE4 = "C1BIDSIZE4"  # The bid trading size threshold
    C1ASKSIZE4 = "C1ASKSIZE4"  # The ask trading size threshold
    C2BIDSIZE4 = "C2BIDSIZE4"  # The bid trading size threshold
    C2ASKSIZE4 = "C2ASKSIZE4"  # The ask trading size threshold
    C3BIDSIZE4 = "C3BIDSIZE4"  # The bid trading size threshold
    C3ASKSIZE4 = "C3ASKSIZE4"  # The ask trading size threshold
    C4BIDSIZE4 = "C4BIDSIZE4"  # The bid trading size threshold
    C4ASKSIZE4 = "C4ASKSIZE4"  # The ask trading size threshold
    C5BIDSIZE4 = "C5BIDSIZE4"  # The bid trading size threshold
    C5ASKSIZE4 = "C5ASKSIZE4"  # The ask trading size threshold
    C1BIDSIZE5 = "C1BIDSIZE5"  # The bid trading size threshold
    C1ASKSIZE5 = "C1ASKSIZE5"  # The ask trading size threshold
    C2BIDSIZE5 = "C2BIDSIZE5"  # The bid trading size threshold
    C2ASKSIZE5 = "C2ASKSIZE5"  # The ask trading size threshold
    C3BIDSIZE5 = "C3BIDSIZE5"  # The bid trading size threshold
    C3ASKSIZE5 = "C3ASKSIZE5"  # The ask trading size threshold
    C4BIDSIZE5 = "C4BIDSIZE5"  # The bid trading size threshold
    C4ASKSIZE5 = "C4ASKSIZE5"  # The ask trading size threshold
    C5BIDSIZE5 = "C5BIDSIZE5"  # The bid trading size threshold
    C5ASKSIZE5 = "C5ASKSIZE5"  # The ask trading size threshold
    TIMESTAMP = "TIMESTAMP"  # The timestamp in UTC millis
    DLG_FLAG = "DLG_FLAG"	
    NET_CHG = "NET_CHG"  # Price change vs open
    NET_CHG_PCT = "NET_CHG_PCT"  # Percentage change vs open
    DELAY = "DELAY"  # Delayed price flag (0=false, 1=true) 


class DLGFlag(StrEnum):
    CLOSED = "CLOSED "
    CALL = "CALL "
    DEAL = "DEAL "
    EDIT = "EDIT "
    CLOSINGSONLY = "CLOSINGSONLY "
    DEALNOEDIT = "DEALNOEDIT "
    AUCTION = "AUCTION "
    AUCTIONNOEDIT = "AUCTIONNOEDIT"
    SUSPEND = "SUSPEND "


class AccountSubscriptionFields(StrEnum):
    PNL = "PNL"  # Account profit and loss value
    DEPOSIT = "DEPOSIT"  # Account minimum deposit value required for margins
    AVAILABLE_CASH = "AVAILABLE_CASH"  # Amount cash available to trade value, after account balance, profit and loss and minimum deposit amount have been considered
    PNL = "PNL"  # Profit/Loss
    PNL_LR = "PNL_LR"  # Profit/Loss Limited Risk
    PNL_NLR = "PNL_NLR"  # Profit/Loss Non-limited Risk
    FUNDS = "FUNDS"  # Funds
    MARGIN = "MARGIN"  # Margin
    MARGIN_LR = "MARGIN_LR"  # Margin Limited Risk
    MARGIN_NLR = "MARGIN_NLR"  # Margin Non-limited Risk
    AVAILABLE_TO_DEAL = "AVAILABLE_TO_DEAL"  # Available to Trade
    EQUITY = "EQUITY"  # Equity
    EQUITY_USED = "EQUITY_USED"  # 


class TradeSubscriptionFields(StrEnum):
    CONFIRMS = "CONFIRMS"  # Trade confirmations for an account
    OPU = "OPU"  # Open position updates for an account
    WOU = "WOU"  # Working order updates for an account


class ConsolidatedChartSubscriptionScale(StrEnum):
    SECOND = "SECOND" 
    MINUTE1 = "1MINUTE"
    MINUTE5 = "5MINUTE" 
    HOUR = "HOUR"  

class ConsolidatedChartSubscriptionFields(StrEnum):  
    LTV = "LTV"  # Last traded volume
    TTV = "TTV"  # Incremental volume
    UTM = "UTM"  # Update time (as milliseconds from the Epoch)
    DAY_OPEN_MID = "DAY_OPEN_MID"  # Mid open price for the day
    DAY_NET_CHG_MID = "DAY_NET_CHG_MID"  # Change from open price to current (MID price)
    DAY_PERC_CHG_MID = "DAY_PERC_CHG_MID"  # Daily percentage change (MID price)
    DAY_HIGH = "DAY_HIGH"  # Daily high price (MID)
    DAY_LOW = "DAY_LOW"  # Daily low price (MID)
    OFR_OPEN = "OFR_OPEN"  # Candle open price (OFR)
    OFR_HIGH = "OFR_HIGH"  # Candle high price (OFR)
    OFR_LOW = "OFR_LOW"  # Candle low price (OFR)
    OFR_CLOSE = "OFR_CLOSE"  # Candle close price (OFR)
    BID_OPEN = "BID_OPEN"  # Candle open price (BID)
    BID_HIGH = "BID_HIGH"  # Candle high price (BID)
    BID_LOW = "BID_LOW"  # Candle low price (BID)
    BID_CLOSE = "BID_CLOSE"  # Candle close price (BID)
    LTP_OPEN = "LTP_OPEN"  # Candle open price (Last Traded Price)
    LTP_HIGH = "LTP_HIGH"  # Candle high price (Last Traded Price)
    LTP_LOW = "LTP_LOW"  # Candle low price (Last Traded Price)
    LTP_CLOSE = "LTP_CLOSE"  # Candle close price (Last Traded Price)
    CONS_END = "CONS_END"  # 1 when candle ends, otherwise 0
    CONS_TICK_COUNT = "CONS_TICK_COUNT"  # Number of ticks in candle


class ChartSubscriptionsFields(StrEnum):
    BID = "BID"  # Bid price
    OFR = "OFR"  # Offer price
    LTP = "LTP"  # Last traded price
    LTV = "LTV"  # Last traded volume
    TTV = "TTV"  # Incremental trading volume
    UTM = "UTM"  # Update time (as milliseconds from the Epoch)
    DAY_OPEN_MID = "DAY_OPEN_MID"  # Mid open price for the day
    DAY_NET_CHG_MID = "DAY_NET_CHG_MID"  # Change from open price to current (MID price)
    DAY_PERC_CHG_MID = "DAY_PERC_CHG_MID"  # Daily percentage change (MID price)
    DAY_HIGH = "DAY_HIGH"  # Daily high price (MID)
    DAY_LOW = "DAY_LOW"  # Daily low price (MID)


class PositionStatus(StrEnum):
    AMENDED = "AMENDED"
    DELETED = "DELETED"
    FULLY_CLOSED = "FULLY_CLOSED"
    OPENED = "OPENED"
    PARTIALLY_CLOSED = "PARTIALLY_CLOSED"
    CLOSED = "CLOSED"


class DealStatus(StrEnum):
    ACCEPTED = "ACCEPTED"
    REJECTED = "REJECTED"


class OpenPositionStatus(StrEnum):
    OPEN = "OPEN"
    UPDATED = "UPDATED"
    DELETED = "DELETED"


class TimeInForce(StrEnum):
    GOOD_TILL_CANCELLED = "GOOD_TILL_CANCELLED"
    GOOD_TILL_DATE = "GOOD_TILL_DATE"
    

# DEPRECATED
class MarketFields(StrEnum):
    MID_OPEN = "MID_OPEN"  # Opening mid price
    HIGH = "HIGH"  # Intraday high price
    LOW = "LOW"  # Intraday low price
    CHANGE = "CHANGE"  # Price change compared with open value
    CHANGE_PCT = "CHANGE_PCT"  # Price percent change compared with open value
    UPDATE_TIME = "UPDATE_TIME"  # Publish time of last price update (UK local time, i.e. GMT or BST)
    MARKET_DELAY = "MARKET_DELAY"  # Delayed price (0=false, 1=true)
    MARKET_STATE = "MARKET_STATE"  # Market status: CLOSED, OFFLINE, TRADEABLE, EDIT, AUCTION, AUCTION_NO_EDIT, SUSPENDED
    BID = "BID"  # Bid price
    OFFER = "OFFER"  # Offer price
    STRIKE_PRICE = "STRIKE_PRICE"  # Strike price (Sprint markets)
    ODDS = "ODDS"  # Trade odds (Sprint markets) 


class MarketStatus(StrEnum):
    CLOSED = "CLOSED"
    OFFLINE = "OFFLINE"
    TRADEABLE = "TRADEABLE"
    EDIT = "EDIT"
    AUCTION = "AUCTION"
    AUCTION_NO_EDIT = "AUCTION_NO_EDIT"
    SUSPENDED = "SUSPENDED"

# DEPRECATED END