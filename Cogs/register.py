import discord
import secrets
from discord.ext import commands
from random import randint

class RegisterCog(commands.Cog, name="help command"):
    def __init__(self, bot):
		self.bot = bot

    @commands.command(name = "register",
                    usage = "",
                    description = "Register with the bot.")
    @commands.command(1, 2, commands.BucketType.member)
    async def on_message(self, ctx, key : str):
        
        #if statement whether or not valid key is in msg
        
        message = await ctx.send("Please add a key and/or valid key eg: !tcbotregister [key]")


        
        



def setup(bot):
    bot.add_cog(RegisterCog(bot))