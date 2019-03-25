import discord
from discord.ext import commands

class owocog:
    """OwO!"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def owo(self):
        """OwO!"""
        oldchar = "L"
        newchar = "W"
        OwOL = pasta.replace(oldchar,newchar)
        oldchar = "R"
        OwOR = OwOL.replace(oldchar,newchar)
        oldchar = "l"
        newchar = "w"
        OwOl = OwOR.replace(oldchar,newchar)
        oldchar = "r"
        OwOr = OwOl.replace(oldchar,newchar)
        await self.bot.say(OwOr)

def setup(bot):
    bot.add_cog(owocog(bot))
