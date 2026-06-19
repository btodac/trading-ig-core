from abc import ABC, abstractmethod
from dataclasses import dataclass, fields
from typing import Any

from trading_ig_core.rest_api.rest_api_enums import RequestType, IGRestAPIVersion


class Arguments(ABC):
    @abstractmethod
    def as_string(self) -> str:
        pass


class RequestData(ABC):
    def to_json(self):
        json_data = {k: v for k, v in vars(self).items() if v is not None}
        for f in fields(self):
            if "json_name" in f.metadata and f.name in json_data:
                json_data[f.metadata["json_name"]] = json_data.pop(f.name)

        return json_data


class Response(ABC):
    pass


@dataclass
class RestApiCall(ABC):
    base_endpoint: str
    request_type: RequestType
    api_version: IGRestAPIVersion

    arguments: Arguments | None = None
    request_data: RequestData | None = None

    @property
    def endpoint(self):
        endpoint = self.base_endpoint
        if self.arguments is not None:
            endpoint += self.arguments.as_string()
        return endpoint

    @property
    def data(self):
        if self.request_data is None:
            return {}
        return self.request_data.to_json()

    @abstractmethod
    def process_payload(self, payload: dict[str, Any]) -> Response:
        pass
