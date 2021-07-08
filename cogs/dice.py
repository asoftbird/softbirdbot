import discord
import random
from discord.ext import commands

class Dice(commands.Cog):
    """Provides commands related to dice rolling"""
    def __init__(self, client):
        self.client = client
    
    def __randomRoll(self, repeats, dice_size):

        result_list = []
        for i in range(repeats):
            result = random.randint(1, dice_size)
            result_list.append(result)
        
        return sum(result_list), result_list

    @commands.Cog.listener() #event decorator for inside cogs
    async def on_ready(self):
        print(f"Cog Dice initialized")

    @commands.command(
        aliases=['rtd'], 
        help="Roll a dice with [count]d[dice size]. Optional arguments: +/-[modifier], 'avg' for average roll, 'list' to display all rolls.",
        usage=".roll 2d20 +5 list\n Aliases: '.r' or '.rtd'.")
    async def roll(self, ctx, *args):
        try: 
            print(args)
            try:
                roll = list(map(int, args[0].split('d')))
            except IndexError:
                await ctx.send("Not enough arguments! Use ..d.. where '.' is a number")
                return
            
            if roll[0] and roll[1] != 0 and roll[0] and roll[1] != None:
                if roll[0] in range(1, 101) and roll[1] in range(1, 501):

                    roll_sum, roll_list = self.__randomRoll(roll[0], roll[1])
                    avg = roll_sum / len(roll_list)
                    avg = '{:.2f}'.format(avg)

                    if len(args) > 1:
                        list_str = ""
                        average_str = ""
                        mod_str = ""
                        
                        try:
                            await ctx.send(str(f'Rolling {roll[0]}d{roll[1]}'))
                            if "list" in args:
                                list_str = f' List: {*roll_list,},'
                                
                            if "avg" in args:
                                average_str = f' Average: {avg},'
                            
                            if len(list(filter(lambda s: "+" in s, args))) > 0:
                                strCheck = list(filter(lambda s: "+" in s, args))
                                if strCheck[0] in args:
                                    modifier = int(strCheck[0][1:]) #remove + from string
                                    if modifier in range(0, 100):
                                        total = int(roll_sum) + int(modifier)
                                        mod_str = f'+{modifier}, total: {total},'

                            if len(list(filter(lambda s: "-" in s, args))) > 0:
                                strCheck = list(filter(lambda s: "-" in s, args))
                                if strCheck[0] in args:
                                    modifier = -int(strCheck[0][1:]) #remove + from string
                                    if modifier in range(-100, 1):
                                        total = int(roll_sum) - int(modifier)
                                        mod_str = f'-{modifier}, total: {total},'
                        
                            await ctx.send(f'Rolled {roll_sum}'+mod_str+list_str+average_str)

                        except:
                            await ctx.send("Invalid argument")
                    else:
                        await ctx.send(str(f'Rolled {roll_sum}'))

                else:
                    await ctx.send('Roll too large; max 100 rolls, max dice size 500')
            else:
                await ctx.send("Invalid roll!")
        except:
            await ctx.send("Not enough arguments!")

def setup(client):
    client.add_cog(Dice(client))
