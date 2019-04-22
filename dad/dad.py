import discord
from discord.ext import commands
import time
import random

class dad:
    """DADDY!"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True,aliases=['Im', "I'm", "i'm"])
    async def im(self,ctx,youneedhelpwithacommandthatiseasy):
        """YOU NEED HELP WITH A COMMAND THAT IS EASY"""
        if ctx.message.channel.id=="493543036882649098":
            await self.bot.say("Hi {}, I'm Dad!".format(youneedhelpwithacommandthatiseasy))
        else:
            await self.bot.add_reaction(ctx.message,❎)

def setup(bot):
    bot.add_cog(dad(bot))
