import asyncio
import sys
from functools import wraps

from .apinya import ErApi


def syncify(apinya, meth):
    async_meth = getattr(apinya, meth)

    @wraps(async_meth)
    def sync_meth(*args, **kwargs):
        coro = async_meth(*args, **kwargs)
        if sys.version_info >= (3, 7):
            try:
                loop = asyncio.get_running_loop()
            except RuntimeError:
                loop = asyncio.get_event_loop_policy().get_event_loop()
        else:
            loop = asyncio.get_event_loop()

        if loop.is_running():
            return coro
        else:
            return loop.run_until_complete(coro)

    return sync_meth


class SyncApi:
    def __init__(self):
        self._async_api = ErApi()

    def __getattr__(self, name):
        attr = getattr(self._async_api, name)
        if asyncio.iscoroutinefunction(attr):
            return syncify(self._async_api, name)
        return attr


apinya = SyncApi()
