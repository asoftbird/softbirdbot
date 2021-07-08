import configparser
import discord
from discord import role
from discord.ext import commands

config = configparser.ConfigParser()
config.read("config.ini")

role_spanjool_id = int(config['Roles']['R_SPANJOOL_ID'])
role_praat_id = int(config['Roles']['R_PRAAT_ID'])
role_ridder_id = int(config['Roles']['R_RIDDER_ID'])
roles_removable_ids = [role_spanjool_id, role_praat_id, role_ridder_id]

class RoleUtils(commands.Cog):
    def __init__(self, client):
        self.client = client
        

    @commands.Cog.listener() #event decorator for inside cogs
    async def on_ready(self):
        print(f"Cog RoleManager initialized")

    def getMemberRoles(self, member: discord.Member):
        return member.roles
    
    def checkMemberHasRole(self, member: discord.Member, role_name):
        if role_name in member.roles:
            return True
        else:
            return False

    async def setRoles(self, member: discord.Member, roles):
        await member.add_roles(roles)

    async def removeRoles(self, member: discord.Member, roles):
        await member.remove_roles(roles)

    # ADD Spanjool REMOVE ridder, praat
    @commands.command(aliases=['s'])
    async def spanjool(self, ctx, member: discord.Member):
        guild = ctx.guild
        __role_spanjool = guild.get_role(role_spanjool_id)

        if not self.checkMemberHasRole(member, __role_spanjool):
            for i, id in enumerate(roles_removable_ids):
                await self.removeRoles(member, guild.get_role(id))
            await self.setRoles(member, __role_spanjool)
            await ctx.send(f"Gave {member.display_name} role {__role_spanjool}.")
        else:
            await ctx.send(f"User {member.display_name} already has this role!")

    # ADD praat REMOVE spanjool
    @commands.command(aliases=['os'])
    async def ontspanjool(self, ctx, member: discord.Member):
        guild = ctx.guild
        __role_spanjool = guild.get_role(role_spanjool_id)
        __role_praat = guild.get_role(role_praat_id)

        if self.checkMemberHasRole(member, __role_spanjool):
            await self.removeRoles(member, __role_spanjool)
            await self.setRoles(member, __role_praat)
            await ctx.send(f"Removed {__role_spanjool} from {member.display_name}.")
        else:
            await ctx.send(f"{member.display_name} does not have {__role_spanjool}!")

    # ADD ridder REMOVE spanjool
    @commands.command(aliases=['r'])
    async def ridder(self, ctx, member: discord.Member):
        guild = ctx.guild
        __role_ridder = guild.get_role(role_ridder_id)
        __role_spanjool = guild.get_role(role_spanjool_id)

        if not self.checkMemberHasRole(member, __role_ridder):
            await self.setRoles(member, __role_ridder)
            await self.removeRoles(member, __role_spanjool)
            await ctx.send(f"Gave {member.display_name} role {__role_ridder}.")
        else:
            await ctx.send(f"User {member.display_name} already has this role!")

    # REMOVE ridder
    @commands.command(aliases=['or'])
    async def ontridder(self, ctx, member: discord.Member):
        guild = ctx.guild
        __role_ridder = guild.get_role(role_ridder_id)

        if self.checkMemberHasRole(member, __role_ridder):
            await self.removeRoles(member, __role_ridder)
            await ctx.send(f"Removed {__role_ridder} from {member.display_name}.")
        else:
            await ctx.send(f"{member.display_name} does not have {__role_ridder}!")

    @commands.command(aliases=['info'])
    async def serverInfo(self, ctx):
        guild = ctx.guild.name
        await ctx.send(f"Guild name: {guild}")


    # multi role set
    # @commands.command(aliases=['ms'])
    # async def msetRole(self, ctx, *args: discord.Member):
    #     guild = ctx.guild
    #     role_name = guild.get_role(862698602938105886)
    #     for i, _ in enumerate(args):
    #         if not self.checkMemberHasRole(args[i], role_name):
    #             await args[i].add_roles(role_name)
    #             await ctx.send(f"Gave {args[i].display_name} role {role_name}.")
    #         else:
    #             await ctx.send(f"User {args[i].display_name} already has this role!")



def setup(client):
    client.add_cog(RoleUtils(client))
