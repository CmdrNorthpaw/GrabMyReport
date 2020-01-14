import socket
import platform
import grab-crash-report
import grab-process-report

sock =  socket.socket(socket.AF_INET, socket.SOCK_STREAM)
os = platform.system()
sock.connect(localhost)
print("""
=============================================================================================
   ____                  _       __  __           ____                                  _
  / ___|  _ __    __ _  | |__   |  \/  |  _   _  |  _ \    ___   _ __     ___    _ __  | |_
 | |  _  | '__|  / _` | | '_ \  | |\/| | | | | | | |_) |  / _ \ | '_ \   / _ \  | '__| | __|
 | |_| | | |    | (_| | | |_) | | |  | | | |_| | |  _ <  |  __/ | |_) | | (_) | | |    | |_
  \____| |_|     \__,_| |_.__/  |_|  |_|  \__, | |_| \_\  \___| | .__/   \___/  |_|     \__|
                                          |___/                 |_|
 ==============================================================================================""")
print("Welcome to GrabMyReport v0.1!")
print("To get started, select the service you need")
print("1. Grab crash report")
print("2. Grab running processes")
print("3. Grab system specs")
grabWanted = input("Enter service (1-3)")
discordUser = raw_input("Enter Discord username and tag (e.g CmdrNorthpaw#1716)")

if grabWanted == 1:
    minecraftDir = raw_input('Enter your Minecraft directory (leave blamk for default)')
    report = grab-crash-report.grabCrash(os, minecraftDir)
elif grabWanted == 2:
    # Do things
elif grabWanted == 3:
    # Moar things

def run_client(host, port):
    global report
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # connect to the provided address tuple
    client.connect((host, port))

    while True:
        # convert to bytes and send on the socket
        client.send(report.encode('utf-8'))
        client.send(discordUser.encode('utf-8'))
        # read back the response
        response = client.recv(1024)

        # empty bytes as result of a read means EOF
        if response == b'':
            print('remote hung up')
            break

        # just decode the response and print
        print(response.decode('utf-8'))
