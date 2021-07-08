import discord
import time
import re
from discord.ext import commands
from utils.util import convertTimeStringToSeconds, sleepUntilUnixtime

class Scheduler(commands.Cog):
    def __init__(self, client):
        self.client = client

    
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
                time_seconds = convertTimeStringToSeconds(result.group('tijd'), result.group('eenheid'))

                await ctx.send(f"Time given: {time_seconds} seconden")

        else:
            await ctx.send(f"No time given!")

        

    


def setup(client):
    client.add_cog(Scheduler(client))
