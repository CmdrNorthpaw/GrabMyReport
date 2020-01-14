import psutil

listProcesses = []
processes = psutil.process_iter()
for list in processes:
    listProcesses.append(list)

print(type(listProcesses))
