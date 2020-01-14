import os

winDir = os.environ.get('APPDATA')
def grabCrash(platform, directory):
    if directory == '':
        if platform == 'Windows':
            print("Using default Windows directory for Minecraft (%APPDATA&/.minecraft)")
            os.chdir(winDir + '\.minecraft')
        elif platform == 'Linux':
            print("Using default Linux directory for Minecraft (~/.minecraft)")
            os.chdir('~/.minecraft')
        elif platform == 'macOS':
            print("Using default macOS directory for Minecraft (~/Library/Application Support/minecraft)")
            os.chdir('~/Library/Application Support/minecraft')
    else:
        os.chdir(directory)
    crashReport = open('launcher_log.txt', 'r')
    crashReport = crashReport.read()
    print(crashReport)
    return crashReport
