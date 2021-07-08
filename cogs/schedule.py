import discord
import time
import re
from discord.ext import commands
import utils.util

HOUR = 3600
MINUTE = 60
DAY = HOUR * 24
MONTH = DAY * 30
YEAR = DAY * 365


class Scheduler(commands.Cog):
    def __init__(self, client):
        self.client = client

    def convertTimeStringToSeconds(self, int_time, unit):
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

    @commands.Cog.listener() #event decorator for inside cogs
    async def on_ready(self):
        print(f"Cog Scheduler initialized")

    # @commands.command()
    # async def ping(self, ctx):
    #     await ctx.send("qwer")

    @commands.command()
    async def time(self, ctx, *args):
        arg_string = ""
        # syntax ;time "over 5 minuten" or "10 seconden" "3 uur" etc
        if len(args) > 0:
            for i, argument in enumerate(args):
                arg_string += argument + " "

            result = re.search(r'(?:over)\s(?P<tijd>\d{1,2})\s(?P<eenheid>seconde|seconden|minuut|minuten|uur|uren|dag|dagen|maand|maanden|jaar|jaren)', arg_string)
            if result != None:
                #await ctx.send(f"args: {args}, string:  {arg_string}, result: {result.group('tijd'), result.group('eenheid')}")
                print(result.group('tijd'))
                print(result.group('eenheid'))
                time_seconds = self.convertTimeStringToSeconds(result.group('tijd'), result.group('eenheid'))
                await ctx.send(f"Time given: {time_seconds} seconden")

        else:
            await ctx.send(f"No time given!")

        

    


def setup(client):
    client.add_cog(Scheduler(client))
