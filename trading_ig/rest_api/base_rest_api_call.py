from abc import ABC, abstractmethod
from dataclasses import dataclass
import json
from typing import Any

from trading_ig.rest_api.api_enums import RequestType, IGRestAPIVersion

class Arguments(ABC):

    @abstractmethod
    def as_string(self) -> str:
        pass


class RequestData:

    def to_json(self):
        json.dumps(vars(self))


@dataclass
class RestApiCall:

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
        return vars(self.request_data)
    
    def process_payload(self, payload: dict[str,Any]):
        return payload