import discord
from discord.ext import commands
import asyncio
import time

class getmessages:
    """getmessages!"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def getmessages(self,ctx,*,contains):
        """Get messages!"""
        person=0
        server=0
        percent=0
        await self.bot.say("Checking server for {} by you!".format(contains))
        await self.bot.send_typing(ctx.message.channel)
        async for channel in ctx.message.server.channels
            async for message in client.logs_from(channel):
                if contains in message.content:
                    server += 1
                    if message.author==ctx.message.author:
                        user += 1
        time.sleep(10)
        if server==0:
            await self.bot.say("You have said {} {} times out of the server's {} times! That makes an error".format(contains,person,server))
        else:
            percent=person/server*100
            await self.bot.say("You have said {} {} times out of the server's {} times! That makes {}%".format(contains,person,server,percent))

def setup(bot):
    bot.add_cog(getmessages(bot))
