import discord
from discord.ext import commands

class getmessages:
    """getmessages!"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def getmessages(self,ctx,*,contains):
        """Get messages!"""
        person=int(0)
        server=int(0)
        percent=int(0)
        contains=str(contains)
        await self.bot.say("Checking server for {} by you!".format(contains))
        await self.bot.send_typing(ctx.message.channel)
        for channel in ctx.message.server.channels:
            channel=yield channel
            for message in self.bot.logs_from(channel,limit=100000):
                if contains in message.content:
                    server=server+1
                    if message.author==ctx.message.author:
                        person=person+1
        percent=person/server*100
        await self.bot.say("You have said {} {} times out of the server's {} times! That makes {}%".format(contains,person,server,percent))


def setup(bot):
    bot.add_cog(getmessages(bot))
