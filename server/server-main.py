import socket
import threading
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
async def on_login():
    logging.info("Bot logged in")

def pasteAndSend(data):
    dataList = []
    try:
        data = pickle.loads(data)
    except EOFError:
        logging.info('Data recieved; pasting...')
        finalData = ''.join(dataList)
        pasteLink = hastebin.post(finalData)
        logging.info('Data posted to Hastebin')
        channel = bot.get_channel(667025203523616773)
        await channel.send(f"Report: {pasteLink}")

def run_server(host, port):
    global report
    incomingList = []
    # TCP/IP
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # this lets us take ownership of a derelict-but-not-deallocated socket
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # bind to the provided address tuple, configure, and start accepting connections
    server.bind((host, port))
    logging.info('Socket server running')
    # set timeout - the value can change, but it's hygienic to always set a timeout
    server.settimeout(1)
    server.listen()

    while True:
        # just try again if we timed out - in a normal application we might want
        # to do other kinds of bookkeeping etc if this happens
        try:
            newClient = server.accept()[0]
        except socket.timeout:
            continue

        # repeatedly read up to 1024 bytes from the new client
        while True:
            incoming = newClient.recv(1024)
            incomingList.append(incoming)
            if incoming == b'' or incoming == b'quit':
               pasteAndSend(incoming)
               newClient.shutdown(socket.SHUT_RDWR)
               newClient.close()
               # break the inner loop and await a new connection
               break

        report = incoming.decode('utf-8')
            # if we didn't break, just prepend the message and return as is

threading.Thread(target=run_server, args=('0.0.0.0', 9254), daemon=True).start()
bot.run(discordKey)
