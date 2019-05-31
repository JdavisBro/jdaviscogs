import discord
from discord.ext import commands
import os
dirname="data/counttomillion"
f="data/counttomillion/count.txt"
try:
    os.mkdir(dirname)
except:
    pass
try:
    open(f,"x")
    open(f,"w").write("{}")
    fileW=open(f, 'w')
    fileR=open(f, 'r')
except:
    fileW=open(f, 'w')
    fileR=open(f, 'r')


class counttomillion:
    """counttomillion!"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def count(self,ctx):
        """Start the count!"""
        data = eval(fileR.read())
        if ctx.message.author.server_permissions.manage_server:
            if data[ctx.message.channel.id]==0:
                await self.bot.say("Ok, count to 1 million started! Say 1 to begin!")
                data[ctx.message.channel.id]=1
                await self.bot.edit_channel(ctx.message.channel,topic="Next number: 1")
                fileW.write(data)
            else:
                await self.bot.say("A count is already running in this channel!")

    @commands.command(pass_context=True)
    async def stopcount(self,ctx):
        data = eval(fileR.read())
        if ctx.message.author.server_permissions.manage_server:
            if data[ctx.message.channel.id]==0:
                await self.bot.say("This channel isn't even counting!")
            else:
                await self.bot.say("Ok, stopped! We got to {} before stopping!".format(data[ctx.message.channel.id]))
                data[ctx.message.channel.id]=0
                fileW.write(data)
                await self.bot.edit_channel(ctx.message.channel,topic="")

    async def on_message(self,message):
        data = eval(fileR.read())
        if data[message.channel.id] != 0:
            try:
                content=int(message.content)
            except:
                try:
                    await self.bot.delete_message(message)
                    return
                except:
                    return
            if content==data[message.channel.id]:
                data[message.channel.id]+=1
                if data[message.channel.id]==1000000:
                    await self.bot.say("We have reached a million! Resetting, say 1 to restart.")
                    data[message.channel.id]=1
                await self.bot.edit_channel(message.channel,topic="Next number: {}".format(data[message.channel.id]))
                fileW.write(data)
            else:
                try:
                    await self.bot.delete_message(message)
                except:
                    pass

def setup(bot):
    bot.add_cog(counttomillion(bot))