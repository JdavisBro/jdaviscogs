import discord
from discord.ext import commands
import time
import random

class saymeanthings:
    """Mean!"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def meanthing(self,ctx,*,mean_thing):
        """Mean!"""
        time.sleep(1)
        await self.bot.send_typing(ctx.message.channel)
        sleepfor=random.randint(2,6)
        time.sleep(sleepfor)
        await self.bot.say("WOW IM LITERALLY CRYING AND SHAKING I CAN'T BELIEVE {} SAID `{}` TO ME 😢 😰".format(ctx.message.author.display_name,mean_thing))

def setup(bot):
    bot.add_cog(saymeanthings(bot))
