import discord
from discord.ext import commands


class Help(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener() #event decorator for inside cogs
    async def on_ready(self):
        print(f"Cog Help initialized")

    @commands.command(help="Attempts to help you by helping you with help about help. Helping helpers since 1997!", usage=".help help")
    async def help(self, ctx, args=None):
        help_embed = discord.Embed(title="softbirdbot: help edition")
        command_names_list = []
        for x in self.client.commands:
            if x.hidden == False:
                command_names_list.append(x.name)

        #command_names_list = [x.name for x in self.client.commands]

        if not args:
            help_embed.add_field(
                name="List of supported commands:",
                value="\n".join([x.name for i,x in enumerate(self.client.commands) if x.hidden == False]),
                inline=False
            )

            help_embed.add_field(
                name="Details",
                value="Type `.help <command name>` for more details about each command.",
                inline=False
            )

        elif args in command_names_list:
            help_embed.add_field(
                name=args,
                value=self.client.get_command(args).help)
            help_embed.add_field(
                name="Usage:",
                value=self.client.get_command(args).usage)

        else:
            help_embed.add_field(
                name="oops",
                value="Command not found"
            )

        await ctx.send(embed=help_embed)







def setup(client):
    client.add_cog(Help(client))
