import socket
import platform
import grabCrashReport
import grabProcessReport
import grabSysReport
import grabHostFile
os = platform.system()
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
print("4. Grab hosts file")
grabWanted = input("Enter service (1-4)")
discordUser = input("Enter Discord username and tag (e.g CmdrNorthpaw#1716)")

if int(grabWanted) == 1:
    minecraftDir = input('Enter your Minecraft directory (leave blamk for default)')
    report = grabCrashReport.grabCrash(os, minecraftDir)
elif grabWanted == 2:
    report = grabProcessReport.grabProcess()
elif grabWanted == 3:
    report = grabSysReport.grabSys(os)
elif grabWanted == 4:
    report = grabHostFile.readHost(os)

def run_client(host, port):
    global report
    global discordUser
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # connect to the provided address tuple
    client.connect((host, port))

    # convert to bytes and send on the socket
    client.send(report.encode('utf-8'))
    client.send(discordUser.encode('utf-8'))
    # read back the response

run_client('34.73.189.184', 9254)
