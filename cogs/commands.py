import discord
from discord.ext import commands


class Extension(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener() #event decorator for inside cogs
    async def on_ready(self):
        print(f"Cog Extension initialized")

    @commands.command()
    async def ping(self, ctx):
        await ctx.send("qwer")


def setup(client):
    client.add_cog(Extension(client))
