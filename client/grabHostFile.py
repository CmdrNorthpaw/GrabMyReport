import os

def readHost(platform):
    if platform == 'Windows':
        os.chdir('C:\Windows\System32\drivers\etc')
    else:
        os.chdir('/etc')
    hostFile = open('hosts', 'r')
    hostFile = hostFile.read()
    return hostFile

readHost('Windows')
