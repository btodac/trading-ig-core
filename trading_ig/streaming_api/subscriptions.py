from lightstreamer.client import Subscription

from trading_ig.streaming_api.streaming_enums import (
    StreamModes, 
    AccountSubscriptionFields, 
    PriceSubscriptionFields, 
    TradeSubscriptionFields,
    ChartSubscriptionsFields, 
    ConsolidatedChartSubscriptionFields,
    ConsolidatedChartSubscriptionScale,
)

class PriceSubscription(Subscription):

    def __init__(self, account_id: str, epic: str, fields: list[PriceSubscriptionFields]):
        super().__init__(
            mode=StreamModes.DISTINCT,
            items=[f"PRICE:{account_id}:{epic}"],
            fields=fields,
        )
        self.setDataAdapter("Pricing")


class AccountSubscription(Subscription):

    def __init__(self, account_id: str, fields: list[AccountSubscriptionFields]):
        super().__init__(
            mode=StreamModes.MERGE,
            items=[f"ACCOUNT:{account_id}"],
            fields=fields,
        )


class TradeSubscription(Subscription):

    def __init__(self, account_id: str, fields: list[TradeSubscriptionFields]):
        super().__init__(
            mode=StreamModes.DISTINCT,
            items=[f"TRADE:{account_id}"],
            fields=fields,
        )
        

class ConsolidatedChartSubscription(Subscription):

    def __init__(
        self, 
        epic: str, 
        scale: ConsolidatedChartSubscriptionScale,
        fields: list[ConsolidatedChartSubscriptionFields],
    ):
        super().__init__(
            mode=StreamModes.MERGE,
            items=[f"CHART:{epic}:{scale}"],
            fields=fields,
        )


class ChartSubscription(Subscription):

    def __init__(self, epic: str, fields: list[ChartSubscriptionsFields]):
        super().__init__(
            mode=StreamModes.DISTINCT,
            items=[f"CHART:{epic}:TICK"],
            fields=fields,
        )
