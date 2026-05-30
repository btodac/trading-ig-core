from dataclasses import dataclass

from trading_ig.rest_api.rest_api_enums import IGRestAPIVersion, RequestType, ApplicationStatus
from trading_ig.rest_api.base_rest_api_call import RestApiCall, RequestData


class GetClientApps(RestApiCall):

    def __init__(self):
        self.base_endpoint = "/operations/application"
        self.request_type = RequestType.GET
        self.api_version = IGRestAPIVersion.ONE


@dataclass
class UpdateClientAppData(RequestData):
    allowanceAccountOverall: int
    allowanceAccountTrading: int
    apiKey: str
    status: ApplicationStatus


class UpdateClientApp(RestApiCall):

    def __init__(
        self,
        allowance_account_overall: int,
        allowance_account_trading: int,
        api_key: str,
        status: str,
    ):
        self.base_endpoint = "/operations/application"
        self.request_type = RequestType.PUT
        self.api_version = IGRestAPIVersion.ONE
        self.request_data = UpdateClientAppData(
            allowanceAccountOverall=allowance_account_overall,
            allowanceAccountTrading=allowance_account_trading,
            apiKey=api_key,
            status=status,
        )


class DisableClientAppKey(RestApiCall):

    def __init__(self):
        self.base_endpoint = "/operations/application/disable"
        self.request_type = RequestType.PUT
        self.api_version = IGRestAPIVersion.ONE