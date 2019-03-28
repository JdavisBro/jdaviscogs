import discord
from discord.ext import commands
import time
import random

class getmessages:
    """getmessages!"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def getmessages(self,ctx,*,contains):
        """Get messages!"""
        int(person=0)
        int(server=0)
        await self.bot.say("Checking server for {} by you!".format(contains))
        await self.bot.send_typing(ctx.message.channel)
        for channel in ctx.message.server.channels:
            channel=yield channel
            logs=await self.bot.logs_from(channel,limit=1000000)
            for message in logs:
                if contains in message.content:
                    server+1
                    if message.author==ctx.message.author:
                        person+1
        int(percent=person/server*100)
        await self.bot.say("You have said {} {} times out of the server's {} times! That makes {}%".format(contains,person,server,percent))
                    

def setup(bot):
    bot.add_cog(getmessages(bot))
