import os
import discord

from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

cog_folder = "cogs"

client = commands.Bot(command_prefix=';', help_command=None)

@client.event
async def on_ready():
    print("main bot loaded")

# load cog
@client.command(hidden=True)
@commands.is_owner()
async def load(ctx, extension):
    try:
        client.load_extension(f"cogs.{extension}")
        await ctx.send(f"Loaded {extension}!")
    except discord.ext.commands.ExtensionAlreadyLoaded:
        print("Extension already loaded!")
        await ctx.send(f"{extension} already loaded!")

# unload cog
@client.command(hidden=True)
@commands.is_owner()
async def unload(ctx, extension):
    client.unload_extension(f"cogs.{extension}")
    await ctx.send(f"Unloaded {extension}!")

# reload cog
@client.command(hidden=True, aliases=[';rl'])
@commands.is_owner()
async def reload(ctx, extension):
    client.reload_extension(f"cogs.{extension}")
    await ctx.send(f"Reloaded {extension}!")

# reload all cogs
@client.command(hidden=True, aliases=[';ra'])
@commands.is_owner()
async def reloadall(ctx):
    exlist = []
    for entry in client.extensions:
        exlist.append(entry)
        print(exlist)
    
    for i, ext in enumerate(exlist):
        client.reload_extension(exlist[i])
    
    await ctx.send(f"Reloaded {*exlist,}!")


# load all cogs when bot starts
for filename in os.listdir(cog_folder):
    try:
        if filename.endswith(".py"):
            client.load_extension(f"cogs.{filename[:-3]}")
            print(f"found file {filename}")
    except discord.ext.commands.ExtensionNotFound:
        print("Extension not found.")
    except discord.ext.commands.ExtensionAlreadyLoaded:
        print("Extenstion already loaded.")

client.run(TOKEN)