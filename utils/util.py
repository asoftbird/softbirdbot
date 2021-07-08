import asyncio
import time
import datetime
import re

HOUR = 3600
MINUTE = 60
DAY = HOUR * 24
MONTH = DAY * 30
YEAR = DAY * 365
MAX_ASYNCIO_SECONDS = 3456000 #~40 days

"""
adapted from discord.utils.sleep_until

original: (requires datetime module)
async def sleep_until(when, result=None):
  if when.tzinfo is None:
        when = when.replace(tzinfo=datetime.timezone.utc)
    now = datetime.datetime.now(datetime.timezone.utc)
    delta = (when - now).total_seconds()
    while delta > MAX_ASYNCIO_SECONDS:
        await asyncio.sleep(MAX_ASYNCIO_SECONDS)
        delta -= MAX_ASYNCIO_SECONDS
    return await asyncio.sleep(max(delta, 0), result)"""

async def sleepUntilUnixtime(time_target, result=None):
    time_now = int(time.time()) #unix time in seconds, truncated to int
    delta = time_target - time_now
    while delta > MAX_ASYNCIO_SECONDS:
        await asyncio.sleep(MAX_ASYNCIO_SECONDS)
        delta -= MAX_ASYNCIO_SECONDS
    return await asyncio.sleep(max(delta, 0), result)

async def viewAsyncioTasks():
    return asyncio.all_tasks()

def convertTimeStringToSeconds(int_time, unit):
    # convert input time and unit to equivalent in seconds
    int_time = int(int_time)
    print(f"Got {int_time} time and unit {unit}")
    print(f"Type int_time: {type(int_time)}, type unit: {type(unit)}")
    if unit == "seconde" or unit == "seconden":
        return int_time
    elif unit == "minuut" or unit == "minuten":
        print("match MINUUT")
        return int_time * MINUTE
    elif unit == "uur" or unit == "uren":
        print("match UUR")
        return int_time * HOUR
    elif unit == "dag" or unit == "dagen":
        return int_time * DAY
    elif unit == "maand" or unit == "maanden":
        return int_time * MONTH
    elif unit == "jaar" or unit == "jaren":
        return int_time * YEAR
    else:
        return 60

