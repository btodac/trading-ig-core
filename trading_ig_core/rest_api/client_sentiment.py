from dataclasses import dataclass

from trading_ig_core.rest_api.rest_api_enums import IGRestAPIVersion, RequestType
from trading_ig_core.rest_api.base_rest_api_call import Arguments, RestApiCall


@dataclass
class FetchClientSentimentByInstrumentArguments(Arguments):
    market_id: str

    def as_string(self):
        return f"/{self.market_id}"


class FetchClientSentimentByInstrument(RestApiCall):
    def __init__(self, market_id: str):
        self.base_endpoint = "/clientsentiment"
        self.request_type = RequestType.GET
        self.api_version = IGRestAPIVersion.ONE
        self.arguments = FetchClientSentimentByInstrumentArguments(market_id=market_id)

    def process_payload(self, payload):
        return _to_sentiment_dict(payload)


@dataclass
class FetchClientSentimentByInstrumentsArguments(Arguments):
    market_ids: list[str]

    def as_string(self):
        market_ids = ",".join(self.market_ids)
        return f"/?marketIds={market_ids}"


class FetchClientSentimentByInstruments(RestApiCall):
    def __init__(self, market_ids: list[str]):
        self.base_endpoint = "/clientsentiment"
        self.request_type = RequestType.GET
        self.api_version = IGRestAPIVersion.ONE
        self.arguments = FetchClientSentimentByInstrumentsArguments(
            market_id=market_ids
        )

    def process_payload(self, payload):
        return _to_sentiments_dict(payload)


@dataclass
class FetchRelatedClientSentimentByInstrumentArguments(Arguments):
    market_id: str

    def as_string(self):
        return f"/related/{self.market_id}"


class FetchRelatedClientSentimentByInstrument(RestApiCall):
    def __init__(self, market_id: str):
        self.base_endpoint = "/clientsentiment"
        self.request_type = RequestType.GET
        self.api_version = IGRestAPIVersion.ONE
        self.arguments = FetchRelatedClientSentimentByInstrumentArguments(
            market_id=market_id
        )

    def process_payload(self, payload):
        return _to_sentiments_dict(payload)


def _to_sentiment_dict(sentiment_json: dict):
    return {
        "long": sentiment_json["longPositionPercentage"],
        "short": sentiment_json["shortPositionPercentage"],
    }


def _to_sentiments_dict(sentiments_json: dict):
    return {
        sentiment["marketId"]: _to_sentiment_dict(sentiment)
        for sentiment in sentiments_json
    }
