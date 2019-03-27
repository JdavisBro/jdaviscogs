import discord
from discord.ext import commands
import time
import random

class gay:
    """GAY!"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def gay(self,ctx):
        """GAY!"""
        await self.bot.send_typing(ctx.message.channel)
        sleepfor=random.randint(1,10)
        time.sleep(sleepfor)
        await self.bot.say("{} is Gay".format(ctx.message.author))

def setup(bot):
    bot.add_cog(gay(bot))
