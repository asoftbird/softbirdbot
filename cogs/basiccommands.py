import discord
from discord.ext import commands


class BasicCommands(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener() #event decorator for inside cogs
    async def on_ready(self):
        print(f"Cog BasicCommands initialized")

    # @commands.command()
    # async def ping(self, ctx):
    #     await ctx.send("qwer")

def setup(client):
    client.add_cog(BasicCommands(client))
