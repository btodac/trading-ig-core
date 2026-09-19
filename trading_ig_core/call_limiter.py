import datetime as dt
import time
from collections import deque
from collections.abc import Callable

from trading_ig_core.rest_api.base_rest_api_call import RestApiCall

_limits = {
    "accounts": 60,
    "trading": 100,
    "non-trading": 30,
}

_limit_map = {
    "accounts": "accounts",
    "positions": "trading",
    "working-orders": "trading",
}


class RESTCallLimiter:
    """Wrapper class to limit api request calls"""
    def __init__(self, func: Callable):
        self._func = func
        self._call_times: dict[str, deque[dt.datetime]] = {
            key: deque(maxlen=request_limit)
            for key, request_limit in _limits.items()
        }

    def __call__(self,
            rest_api_call: RestApiCall,
            return_raw: bool,
        ):
            endpoint = rest_api_call.base_endpoint.split('/',2)[1]
            limit_type = _limit_map.get(endpoint, "non-trading")
            limit_deque = self._call_times[limit_type]
            self._wait(limit_deque)
            return self._func(rest_api_call, return_raw)

    def _wait(self, limit_deque: deque[dt.datetime]):
        new_dt = dt.datetime.now(tz=dt.UTC)
        if len(limit_deque) == limit_deque.maxlen:
            time.sleep(new_dt - limit_deque.popleft())
        limit_deque.append(new_dt)

