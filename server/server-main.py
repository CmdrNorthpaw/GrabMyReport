import websockets
import asyncio
import discord
from discord.ext import commands
from os import environ
import hastebin
import logging
import pickle
discordKey = environ.get('grabMyReportKey')
logging.basicConfig(level=logging.INFO)

bot = commands.Bot(command_prefix='?')

@bot.event
async def on_ready():
    logging.info("Bot logged in")
    await reciever()

async def pasteAndSend(data):
    try:
        data = pickle.loads(data)
    except EOFError:
        logging.info('Data recieved; pasting...')
        pasteLink = hastebin.post(data)
        print(pasteLink)
        logging.info('Data posted to Hastebin')
        channel = bot.get_channel(667025203523616773)
        await channel.send(f"Report: {pasteLink}")

async def reciever():
    host = 'ws://localhost:9254'
    async with websockets.connect(host) as socket:
        print('Socket server running')
        data = await socket.recv()
        data = pickle.loads(data)
        pasteAndSend(data)

server = websockets.serve(reciever, 'localhost', 9254)
asyncio.get_event_loop().run_until_complete(server)
asyncio.get_event_loop().run_forever()

bot.run(discordKey)
