import discord
import time
import random
from discord.ext import commands

class jroll(commands.Cog):
    """Jdavis Roll"""

@commands.command()
async def jroll(self,ctx):
    """tHIS ROLLS"""
    stop= random.randint(1,5)
    await commands.say(stop)
    message= await commands.say("Rolling\n  1\n  2\n>3\n  4\n  5\nRolling")
    time.sleep(0.4)
    await commands.edit_message(message,new_content=str("Rolling\n  2\n  3\n>4\n  5\n  1\nRolling"))
    time.sleep(0.4)
    await commands.edit_message(message,new_content=str("Rolling\n  3\n  4\n>5\n  1\n  2\nRolling"))
    time.sleep(0.4)
    await commands.edit_message(message,new_content=str("Rolling\n  4\n  5\n>1\n  2\n  3\nRolling"))
    time.sleep(0.4)
    await commands.edit_message(message,new_content=str("Rolling\n  5\n  1\n>2\n  3\n  4\nRolling"))
    time.sleep(0.4)
    await commands.edit_message(message,new_content=str("Rolling\n  1\n  2\n>3\n  4\n  5\nRolling"))
    time.sleep(0.4)
    await commands.edit_message(message,new_content=str("Rolling\n  2\n  3\n>4\n  5\n  1\nRolling"))
    time.sleep(0.5)
    await commands.edit_message(message,new_content=str("Rolling\n  3\n  4\n>5\n  1\n  2\nRolling"))
    time.sleep(0.5)
    await commands.edit_message(message,new_content=str("Rolling\n  4\n  5\n>1\n  2\n  3\nRolling"))
    time.sleep(0.6)
    await commands.edit_message(message,new_content=str("Rolling\n  5\n  1\n>2\n  3\n  4\nRolling"))
    time.sleep(0.7)
    await commands.edit_message(message,new_content=str("Rolling\n  1\n  2\n>3\n  4\n  5\nRolling"))
    if stop==1:
        time.sleep(0.8)
        await commands.edit_message(message,new_content=str("Rolling\n  2\n  3\n>4\n  5\n  1\nRolling"))
        time.sleep(0.9)
        await commands.edit_message(message,new_content=str("Rolling\n  3\n  4\n>5\n  1\n  2\nRolling"))
        time.sleep(1)
        await commands.edit_message(message,new_content=str("Rolling\n  4\n  5\n>1\n  2\n  3\nRolling"))
    elif stop==2:
        time.sleep(0.8)
        await commands.edit_message(message,new_content=str("Rolling\n  2\n  3\n>4\n  5\n  1\nRolling"))
        time.sleep(0.9)
        await commands.edit_message(message,new_content=str("Rolling\n  3\n  4\n>5\n  1\n  2\nRolling"))
        time.sleep(1.0)
        await commands.edit_message(message,new_content=str("Rolling\n  4\n  5\n>1\n  2\n  3\nRolling"))
        time.sleep(1.1)
        await commands.edit_message(message,new_content=str("Rolling\n  5\n  1\n>2\n  3\n  4\nRolling"))
    elif stop==3:
        time.sleep(0.8)
        await commands.edit_message(message,new_content=str("Rolling\n  2\n  3\n>4\n  5\n  1\nRolling"))
        time.sleep(0.9)
        await commands.edit_message(message,new_content=str("Rolling\n  3\n  4\n>5\n  1\n  2\nRolling"))
        time.sleep(1.0)
        await commands.edit_message(message,new_content=str("Rolling\n  4\n  5\n>1\n  2\n  3\nRolling"))
        time.sleep(1.1)
        await commands.edit_message(message,new_content=str("Rolling\n  5\n  1\n>2\n  3\n  4\nRolling"))
        time.sleep(1.2)
        await commands.edit_message(message,new_content=str("Rolling\n  1\n  2\n>3\n  4\n  5\nRolling"))
    elif stop==4:
        time.sleep(0.8)
        await commands.edit_message(message,new_content=str("Rolling\n  2\n  3\n>4\n  5\n  1\nRolling"))
    else:
        time.sleep(0.8)
        await commands.edit_message(message,new_content=str("Rolling\n  2\n  3\n>4\n  5\n  1\nRolling"))
        time.sleep(0.9)
        await commands.edit_message(message,new_content=str("Rolling\n  3\n  4\n>5\n  1\n  2\nRolling"))

def setup(bot):
    bot.add_cog(jroll(bot))
