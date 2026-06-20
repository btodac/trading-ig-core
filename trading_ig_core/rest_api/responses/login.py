from pydantic.dataclasses import dataclass

from trading_ig_core.rest_api.base_rest_api_call import Response
from trading_ig_core.rest_api.rest_api_enums import AccountType, ReroutingEnvironment


@dataclass
class SessionDetailsResponse(Response):
    accountId: str  # Active account identifier
    clientId: str  # Client identifier
    currency: str  # Currency
    lightstreamerEndpoint: str  # Lightstreamer endpoint
    locale: str  # Locale
    timezoneOffset: float  # Timezone offset relative to UTC (in hours)


@dataclass
class AccountInfo:
    available: float  # Account funds available for trading amount
    balance: float  # Balance of funds in the account
    deposit: float  # Minimum deposit amount required for margins
    profitLoss: float  # Account profit and loss amount


@dataclass
class ClientAccount:
    accountId: str  # Account identifier
    accountName: str  # Account name
    accountType: AccountType  # CFD, PHYSICAL, or SPREADBET
    preferred: bool  # Indicates whether this account is the client's preferred account


@dataclass
class SessionCreateV1Response(Response):
    accountInfo: AccountInfo	
    accountType: AccountType
    accounts: list[ClientAccount]  # List of client accounts
    clientId: str  # Client identifier
    currencyIsoCode: str  # Account currency
    currencySymbol: str  # Account currency symbol
    currentAccountId: str  # Active account identifier
    dealingEnabled: bool  # Whether the account is enabled for placing trading orders
    hasActiveDemoAccounts: bool  # Whether the Client has active demo accounts
    hasActiveLiveAccounts: bool  # Whether the Client has active live accounts
    lightstreamerEndpoint: str  # Lightstreamer endpoint for subscribing to account and price updates
    reroutingEnvironment: ReroutingEnvironment | None  # DEMO, LIVE, TEST, or UAT
    timezoneOffset: float  # Client account timezone offset relative to UTC, expressed in hours
    trailingStopsEnabled: bool  # Whether the account is allowed to set trailing stops on trades


@dataclass
class OAuthToken:
    access_token: str  # Access token
    expires_in: float  # str Access token expiry in seconds
    refresh_token: str  # Refresh token
    scope: str  # Scope of the access token
    token_type: str  # Token type


@dataclass
class SessionCreateV3Response(Response):
    accountId: str  # Active account identifier
    clientId: str  # Client identifier
    lightstreamerEndpoint: str  # Lightstreamer endpoint for subscribing to account and price updates
    oauthToken: OAuthToken
    timezoneOffset: float  # Timezone offset of the active account relative to UTC, expressed in hours


@dataclass
class SwitchAccountResponse(Response):
    dealingEnabled: bool  # Whether the account is enabled for placing trading orders
    hasActiveDemoAccounts: bool  # Whether the Client has active demo accounts
    hasActiveLiveAccounts: bool  # Whether the Client has active live accounts
    trailingStopsEnabled: bool  # Whether the account is allowed to set trailing stops on his trades


@dataclass
class GetEncryptionKeyResponse(Response):
    encryptionKey: str  # Encryption key in Base 64 format
    timeStamp: float  # Current timestamp in milliseconds since epoch

