import psutil

processList = psutil.process_iter()
for list in processList:
    print(list)
