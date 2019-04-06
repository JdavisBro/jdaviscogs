import discord
from discord.ext import commands
import time
import random

class robotuprising:
    """See what the future will be like!"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def robot(self,ctx,text=''):
        """ROBOTS ARE GONNA TAKE UR KIDS!"""
        if text='':
            await self.bot.say("Please say what text to generate from!\nList of available texts:\n`ramranch | `")
        if text='ramranch':
            

def setup(bot):
    bot.add_cog(robotuprising(bot))
