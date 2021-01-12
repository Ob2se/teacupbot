import discord
from discord.ext import commands
from random import randint

class StinkCog(commands.Cog, name="help command"):
  def __init__(self, bot):
    self.bot = bot

  @commands.command(name = "stinky", usage = "", description = "find out whos stinky")

  @commands.cooldown(1, 2, commands.BucketType.member)
  async def stinky(self, ctx):
    message = await ctx.send("Tommy, Dylan and Ernie are quite honestly the stinkiest of them all!")
    
def setup(bot):
    bot.add_cog(StinkCog(bot))