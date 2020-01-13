import discord
import socket
from os import environ

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.bind(socket.gethostname(), 9254)
sock.listen(5)

while True:
    clientSock, address = sock.accept()
    report = sock.recv(1024)
    report = report(message.decode())
