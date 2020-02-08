import websockets
import asyncio
import discord
from discord.ext import commands
from os import environ
import async_hastebin as hastebin
import logging
import pickle
discordKey = environ.get('grabMyReportKey')
logging.basicConfig(level=logging.INFO)

bot = commands.Bot(command_prefix='?')

@bot.event
async def on_ready():
    logging.info("Bot logged in")

async def pasteAndSend(data):
    try:
        data = pickle.loads(data)
    except EOFError:
        logging.info('Data recieved; pasting...')
        pasteLink = await hastebin.post(data)
        print(pasteLink)
        logging.info('Data posted to Hastebin')
        channel = bot.get_channel(667025203523616773)
        await channel.send(f"Report: {p asteLink}")

async def dataRecieve(websocket, path):
    logging.info('Server Running')
    incoming = await websocket.recv()
    print(incoming)
    pasteAndSend(incoming)

bot.run(discordKey)

server = websockets.serve(dataReceive, 'localhost', 9254)
asyncio.get_event_loop().run_until_complete(server)
asyncio.get_event_loop().run_forever()
