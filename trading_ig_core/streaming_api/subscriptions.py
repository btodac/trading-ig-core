import logging

from lightstreamer.client import Subscription

from trading_ig_core.streaming_api.streaming_enums import (
    AccountSubscriptionFields,
    ChartSubscriptionsFields,
    ConsolidatedChartSubscriptionFields,
    ConsolidatedChartSubscriptionScale,
    PriceSubscriptionFields,
    StreamModes,
    TradeSubscriptionFields,
)

logger = logging.getLogger(__name__)


class SubscriptionError(Exception):
    """Raised when a subscription fails"""


class IGBaseSubscription(Subscription):

    def onSubscription(self):
        logger.debug(f"{self.__class__}: Subscribed successfully")

    def onSubscriptionError(self, code, message):
        logger.debug(f"{self.__class__}: SubscriptionError: '{code}' {message}")
        raise SubscriptionError(f"'{code}' {message}")

    def onUnsubscription(self):
        logger.debug(f"{self.__class__}: Unsubscribed")


class PriceSubscription(IGBaseSubscription):
    def __init__(
        self, account_id: str, epic: str, fields: list[PriceSubscriptionFields]
    ):
        super().__init__(
            mode=StreamModes.MERGE,
            items=[f"PRICE:{account_id}:{epic}"],
            fields=fields,
        )
        super().setDataAdapter("Pricing")


class AccountSubscription(IGBaseSubscription):
    def __init__(self, account_id: str, fields: list[AccountSubscriptionFields]):
        super().__init__(
            mode=StreamModes.MERGE,
            items=[f"ACCOUNT:{account_id}"],
            fields=fields,
        )


class TradeSubscription(IGBaseSubscription):
    def __init__(self, account_id: str, fields: list[TradeSubscriptionFields]):
        super().__init__(
            mode=StreamModes.DISTINCT,
            items=[f"TRADE:{account_id}"],
            fields=fields,
        )


class ConsolidatedChartSubscription(IGBaseSubscription):
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


class ChartSubscription(IGBaseSubscription):
    def __init__(self, epic: str, fields: list[ChartSubscriptionsFields]):
        super().__init__(
            mode=StreamModes.DISTINCT,
            items=[f"CHART:{epic}:TICK"],
            fields=fields,
        )
