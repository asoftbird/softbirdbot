import discord
import time
import configparser
import asyncio
import re
from discord.ext import commands
from utils.util import convertTimeStringToSeconds, sleepUntilUnixtime, viewAsyncioTasks
from cogs.roleutil import RoleUtils as roleHelper

config = configparser.ConfigParser()
config.read("config.ini")

role_spanjool_id = int(config['Roles']['R_SPANJOOL_ID'])
role_praat_id = int(config['Roles']['R_PRAAT_ID'])
role_ridder_id = int(config['Roles']['R_RIDDER_ID'])
roles_removable_ids = [role_spanjool_id, role_praat_id, role_ridder_id]


class Scheduler(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener() #event decorator for inside cogs
    async def on_ready(self):
        print(f"Cog Scheduler initialized")

    # @commands.command()
    # async def ping(self, ctx):
    #     await ctx.send("qwer")

    async def TASKprintMessageAfterDelay(self, ctx, expire_time):
        total_time = expire_time + int(time.time())
        await sleepUntilUnixtime(total_time)
        await ctx.send(f"Waited {expire_time} seconds!")

    async def TASK_spanjool(self, ctx, member, expire_time):
        guild = ctx.guild
        __role_spanjool = guild.get_role(role_spanjool_id)
        __role_praat = guild.get_role(role_praat_id)

        total_time = expire_time + int(time.time())
        await roleHelper.setRoles(self, member, __role_spanjool)
        await roleHelper.removeRoles(self, member, __role_praat)
        await sleepUntilUnixtime(total_time)
        await ctx.send(f"Waited {expire_time} seconds!")
        await roleHelper.removeRoles(self, member, __role_spanjool)
        await roleHelper.setRoles(self, member, __role_praat)

    @commands.command()
    async def time(self, ctx, member: discord.Member, *args):
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
                #asyncio.create_task(self.TASKprintMessageAfterDelay(ctx, time_seconds), name="asdf")
                asyncio.create_task(self.TASK_spanjool(ctx, member, time_seconds))
                print(await viewAsyncioTasks())

        else:
            await ctx.send(f"No time given!")

        
    @commands.command()
    async def tasks(self, ctx):
        current_tasks = await viewAsyncioTasks()
        await ctx.send(current_tasks)


def setup(client):
    client.add_cog(Scheduler(client))
