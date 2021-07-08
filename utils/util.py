import asyncio
import time
import datetime
import re

MAX_ASYNCIO_SECONDS = 3456000 #~40 days

"""
adapted from discord.utils.sleep_until

original:
async def sleep_until(when, result=None):
  if when.tzinfo is None:
        when = when.replace(tzinfo=datetime.timezone.utc)
    now = datetime.datetime.now(datetime.timezone.utc)
    delta = (when - now).total_seconds()
    while delta > MAX_ASYNCIO_SECONDS:
        await asyncio.sleep(MAX_ASYNCIO_SECONDS)
        delta -= MAX_ASYNCIO_SECONDS
    return await asyncio.sleep(max(delta, 0), result)"""

async def sleep_until_unixtime(time_target, result=None):
    time_now = int(time.time()) #unix time in seconds, truncated to int
    delta = time_target - time_now
    while delta > MAX_ASYNCIO_SECONDS:
        await asyncio.sleep(MAX_ASYNCIO_SECONDS)
        delta -= MAX_ASYNCIO_SECONDS
    return await asyncio.sleep(max(delta, 0), result)


