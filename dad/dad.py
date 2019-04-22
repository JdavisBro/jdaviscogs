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
        await self.bot.say("Hi {}, I'm Dad!".format(youneedhelpwithacommandthatiseasy))

def setup(bot):
    bot.add_cog(dad(bot))
