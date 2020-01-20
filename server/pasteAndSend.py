import discord
from discord.ext import commands
from os import environ
import hastebin
import logging
discordKey = environ.get('grabMyReportKey')
logging.basicConfig(level=logging.INFO)

bot = commands.bot(command_prefix='?')

def pasteAndSend(data):
    data = data.decode('utf-8')
    pasteLink = hastebin.post(data)
    channel = bot.get_channel(667025203523616773)
    channel.send(f"Report: {pasteLink}")

bot.run(discordKey)
