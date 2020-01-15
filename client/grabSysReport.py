from system_info import sysinfo
from gpuinfo.windows import get_gpus

def grabSys(platform):
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
    sysReport = '\n'.join(listSys)
    print(sysReport)
    return sysReport

grabSys('Windows')
