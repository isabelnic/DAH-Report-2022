import urllib.request
import tempfile
import shutil
import time
import numpy as np
import re
import matplotlib.pyplot as plt


def get_num(mystring):  # get numbers from string
    nums = re.findall("\d+\.\d+", mystring)
    return float(nums[0])


def get_tempNhum(IP):
    temps = []
    humids = []
    levels = []
    count = 0
    
    while count < 10:
        with urllib.request.urlopen(IP + 'temp') as response:
            tempf = get_num(response.read())
            tempc = (tempf - 32) * 5/9
            temps.append(tempc)
        with urllib.request.urlopen(IP + 'humidity') as response:
            hum = get_num(response.read())
            humids.append(hum)
        with urllib.request.urlopen(IP + 'water_level') as response:
            lev = get_num(response.read())
            levels.append(lev)
        count += 1
        time.sleep(0.25)
    
    return np.mean(temps), np.mean(humids), np.mean(levels)


# def maxmin():
    
#     print(get_tempNhum('http://192.168.0.16/'))
    
# maxmin()
    
    
# def plottemphum(temps, humids):
#     print(temps, humids)
#     plt.style.use('ggplot')
#     plt.scatter(temps, humids, marker='s')
#     plt.xlabel('temperature, C')
#     plt.ylabel('Relative humidity %')
#     plt.ylim(ymax=100, ymin=0)
#     plt.xlim(xmax=35, xmin=-50)
#     plt.show()