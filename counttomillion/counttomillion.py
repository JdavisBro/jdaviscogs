import discord
from discord.ext import commands
import json, os
dirname="data/counttomillion"
f="data/counttomillion/count.json"
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
        data=json.load(fileR)
        if ctx.message.author.server_permissions.manage_server:
            if data[ctx.message.channel.id]==0:
                await self.bot.say("Ok, count to 1 million started! I'll begin!")
                data[ctx.message.channel.id]=1
                await self.bot.edit_channel(ctx.message.channel,topic="Next number: 1")
                json.dump(data, fileW, sort_keys=True, indent=4)
            else:
                await self.bot.say("A count is already running in this channel!")

    @commands.command(pass_context=True)
    async def stopcount(self,ctx):
        data=json.load(fileR)
        if ctx.message.author.server_permissions.manage_server:
            if data[ctx.message.channel.id]==0:
                await self.bot.say("This channel isn't even counting!")
            else:
                await self.bot.say("Ok, stopped! We got to {} before stopping!".format(data[ctx.message.channel.id]))
                data[ctx.message.channel.id]=0
                json.dump(data, fileW, sort_keys=True, indent=4)
                await self.bot.edit_channel(ctx.message.channel,topic="")

    async def on_message(self,message):
        data=json.load(fileR)
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
                    await self.bot.say("We have reached a million! Resetting, say 1 to start.")
                    data[message.channel.id]=1
                await self.bot.edit_channel(message.channel,topic="Next number: {}".format(data[message.channel.id]))
                json.dump(data, fileW, sort_keys=True, indent=4)
            else:
                try:
                    await self.bot.delete_message(message)
                except:
                    pass

def setup(bot):
    bot.add_cog(counttomillion(bot))