import socket
import threading
import discord
from discord.ext import commands
from os import environ
import hastebin
import logging
discordKey = environ.get('grabMyReportKey')
logging.basicConfig(level=logging.INFO)

bot = commands.Bot(command_prefix='?')

@bot.event
async def on_login():
    logging.info("Bot logged in")

def pasteAndSend(data):
    data = data.decode('utf-8')
    pasteLink = hastebin.post(data)
    channel = bot.get_channel(667025203523616773)
    channel.send(f"Report: {pasteLink}")

def run_server(host, port):
    global report
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
            # empty bytes object means EOF here, but we also let the client send 'quit' to signal shutdown
            if incoming:
                print(incoming)
                pasteAndSend(incoming)
            if incoming == b'' or incoming == b'quit':
               # neither of these steps are formally required, but are
               # hygienic to do when we know the socket is going away
               newClient.shutdown(socket.SHUT_RDWR)
               newClient.close()
               # break the inner loop and await a new connection
               break

        report = incoming.decode('utf-8')
            # if we didn't break, just prepend the message and return as is

threading.Thread(target=run_server, args=('0.0.0.0', 9254), daemon=True).start()
bot.run(discordKey)
