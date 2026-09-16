
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.WARNING)


def api_limit_hit(response_text: str):
    # note we don't check for historical data allowance - it only gets reset
    # once a week
    return (
        "exceeded-api-key-allowance" in response_text
        or "exceeded-account-allowance" in response_text
        or "exceeded-account-trading-allowance" in response_text
    )


def token_invalid(response_text: str):
    return (
        "oauth-token-invalid" in response_text
        or "client-token-invalid" in response_text
    )
