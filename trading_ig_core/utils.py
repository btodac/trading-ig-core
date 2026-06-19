#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import logging
import traceback
import six

logger = logging.getLogger(__name__)
logger.setLevel(logging.WARNING)

OPT_URL = "https://trading-ig.readthedocs.io/en/latest/faq.html#optional-dependencies"

try:
    import pandas
except ImportError:
    _HAS_PANDAS = False
    logger.warning(f"pandas is not present in the environment. See {OPT_URL}")
else:
    _HAS_PANDAS = True


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
