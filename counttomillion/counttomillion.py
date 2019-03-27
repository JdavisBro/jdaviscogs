import discord
from discord.ext import commands
import json

json="data/counttomillion/count.json"
fileW=open(json, 'w')
fileR=open(json, 'r')

if fileR.read()!='':
    print("Creating count.json file in data/counttomillion/")
    open(json,'w+').write("{}")
else:
    print("file already exists continuing.")

data=json.load(fileR)

class counttomillion:
    """counttomillion!"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def count(self,ctx):
        """Start the count!"""
        if ctx.message.author.server_permissions.manage_server:
            if data[ctx.message.channel.id]==0:
                await self.bot.say("Ok, count to 1 million started! I'll begin!")
                await self.bot.say("1")
                data[ctx.message.channel.id]=2
                await self.bot.edit_channel(ctx.message.channel,topic="Next number: 2")
                json.dump(data, fp, sort_keys=True, indent=4)
            else:
                await self.bot.say("A count is already running in this channel!")

    @commands.command(pass_context=True)
    async def stopcount(self,ctx):
        if ctx.message.author.server_permissions.manage_server:
            if data[ctx.message.channel.id]==0:
                await self.bot.say("This channel isn't even counting!")
            else:
                await self.bot.say("Ok, stopped! We got to {} before stopping!".format(data[ctx.message.channel.id]))
                data[ctx.message.channel.id]=0
                await self.bot.edit_channel(ctx.message.channel,topic="")

    @commands.event
    async def on_message(message):
        if [message.channel.id]!=0
            try:
                content=int(message.content)
                if content==data[message.channel.id]:
                    data[message.channel.id]+1
                    await self.bot.edit_channel(ctx.message.channel,topic="Next number: {}".format(data[message.channel.id]))
                    json.dump(data, fileW, sort_keys=True, indent=4
            except:
                try:
                    await self.bot.delete_message(message)
                except:
                    pass

def setup(bot):
    bot.add_cog(counttomillion(bot))
