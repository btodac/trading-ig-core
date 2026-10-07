from enum import StrEnum

from pydantic.dataclasses import dataclass


class AppStatus(StrEnum):
    DISABLED = "DISABLED" 
    ENABLED = "ENABLED"
    REVOKED = "REVOKED"


@dataclass
class ClientApplications:
    allowEquities: bool  # (Boolean) 	True if access to equity prices is permitted
    allowQuoteOrders: bool  # (Boolean) 	True if quote orders are permitted
    allowanceAccountHistoricalData: float  # (Number) 	Historical price data data points per minute allowance
    allowanceAccountOverall: float  # (Number) 	Per account request per minute allowance
    allowanceAccountTrading: float  # (Number) 	Per account trading request per minute allowance
    allowanceApplicationOverall: float  # (Number) 	Overall request per minute allowance
    apiKey: str  # (String) 	API key
    concurrentSubscriptionsLimit: float  # (Number) 	Concurrent subscription limit per lightstreamer connection
    createdDate: str  # (String) 	Application creation date
    name: str  # (String) 	Application name
    status: AppStatus   # (Constant) 	


@dataclass
class GetClientAppsResponse:
    applications: list[ClientApplications]