import discord
from discord.ext import commands
from os import environ
key = environ.get('grabMyReportKey')

bot = commands.Bot(command_prefix='?')

@bot.command
async def helpme(ctx):
    string = ("**How to use GrabMyReport**\n"
              "1. Download GrabMyReport from https://github.com/CmdrNorthpaw/GrabMyReport\n"
              "2. Double click the EXE to run it. Select More Info > Run anyway to bypass SmartScreen. Don't worry, this is completely safe.\n"
              "3.The EXE will open a window. Input your Discord name, and what you need doing, and GrabMyReport will take care of the rest!")
    ctx.send(string)

bot.run(key)
