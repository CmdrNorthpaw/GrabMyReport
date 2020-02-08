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

async def pasteAndSend(data):
    finalData = b''.join(data)
    try:
        data = pickle.loads(finalData)
    except EOFError:
        logging.info('Data recieved; pasting...')
        pasteLink = hastebin.post(finalData)
        print(pasteLink)
        logging.info('Data posted to Hastebin')
        channel = bot.get_channel(667025203523616773)
        await channel.send(f"Report: {pasteLink}")

async def dataRecieve(websocket, path):
    incoming = await websocket.recv()
    print(incoming)

bot.run(discordKey)

server = websockets.serve(dataRecieve, 'localhost', 9254)
asyncio.get_event_loop().run_until_complete(server)
asyncio.get_event_loop().run_forever()
