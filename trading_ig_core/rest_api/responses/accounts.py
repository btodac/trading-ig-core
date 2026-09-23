from pydantic.dataclasses import dataclass

from trading_ig_core.rest_api.base_rest_api_call import RestAPIResponse
from trading_ig_core.rest_api.rest_api_enums import AccountStatus, AccountType


@dataclass
class Balances:
    available: float  # Amount available for trading
    balance: float  # Balance of funds in the account
    deposit: float  # Minimum deposit amount required for margins
    profitLoss: float  # Profit and loss amount


@dataclass
class Account:
    
    accountId: str  # Account identifier
    accountName: str  # Account name
    accountType: AccountType
    balance: Balances
    canTransferFrom: bool  # True if account can be transferred to
    canTransferTo: bool  # True if account can be transferred from
    currency: str  # Account currency
    preferred: bool  # True if this the default login account
    status: AccountStatus
    accountAlias: str | None = None  # Account alias


@dataclass
class Accounts(RestAPIResponse):
    """Response from FetchAccounts"""
    accounts: list[Account]

    @classmethod
    def from_response(cls, response: list[str]):
        return cls(response["accounts"])
