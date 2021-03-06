import discord
from discord.ext import commands
import time
import random,asyncio

class sugarcog:
    """Sugarcane farm!!"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def sugarcane(self,times=2):
        """Sugar Cane!"""
        times=int(times)
        msg=await self.bot.say("<:space:559559231817121793><:observer:559556253807017985><:redstone:559556253081272320>\n<:space:559559231817121793><:piston:559556586650206223><:stone:559556253169483796>\n<:sugarcane:559556252972220478>")
        await self.bot.edit_message(msg,new_content="<:space:559559231817121793><:observer:559556253807017985><:redstone:559556253081272320>\n<:space:559559231817121793><:piston:559556586650206223><:stone:559556253169483796>\n<:sugarcane:559556252972220478>")
        for i in range(times):
            pause=random.randint(1,8)
            await asyncio.sleep(pause)
            await self.bot.edit_message(msg,new_content="<:space:559559231817121793><:observer:559556253807017985><:redstone:559556253081272320>\n<:sugarcane:559556252972220478><:piston:559556586650206223><:stone:559556253169483796>\n<:sugarcane:559556252972220478>")
            pause=random.randint(1,8)
            await asyncio.sleep(pause)
            await self.bot.edit_message(msg,new_content="<:sugarcane:559556252972220478><:observer:559556253807017985><:redstone:559556253081272320>\n<:sugarcane:559556252972220478><:piston:559556586650206223><:stone:559556253169483796>\n<:sugarcane:559556252972220478>")
            pause=random.randint(1,8)
            await asyncio.sleep(pause)
            await self.bot.edit_message(msg,new_content="<:space:559559231817121793><:observer:559556253807017985><:redstone:559556253081272320>\n<:space:559559231817121793><:piston:559556586650206223><:stone:559556253169483796>\n<:sugarcane:559556252972220478>")
        await self.bot.add_reaction(msg,"✅")

def setup(bot):
    bot.add_cog(sugarcog(bot))
