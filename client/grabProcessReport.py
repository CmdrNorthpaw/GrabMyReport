import psutil

def grabProcess():
    listProcesses = []
    strList = []
    processList = []
    processes = psutil.process_iter()
    for list in processes:
        listProcesses.append(list)
    for object in listProcesses:
        strList.append(str(object))
    process = '\n \n'.join(strList)
    print(process)
    return process
