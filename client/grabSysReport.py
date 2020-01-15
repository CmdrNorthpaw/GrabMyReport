from system_info import sysinfo
from gpuinfo.windows import get_gpus
from psutil import virtual_memory

def grabSys(platform):
    memory = virtual_memory()
    info = sysinfo.os_info.systemSpec()
    listSys = []
    if platform == 'Linux':
        print('Warning! On Linux, this process requires sudo permissions and only works on Debian and Ubuntu-based systems! It also doesn\'t provide GPU information')
    del info['Ip']
    del info['Serial_Number']
    for i in info:
        listSys.append(f'{i}: {info[i]}')
    for gpu in get_gpus():
        gpuDict = gpu.__dict__
    listSys.append(f'GPU: {gpuDict["name"]}')
    listSys.append(f'Total RAM: {memory[0]} bytes')
    sysReport = '\n'.join(listSys)
    print(sysReport)
    return sysReport
