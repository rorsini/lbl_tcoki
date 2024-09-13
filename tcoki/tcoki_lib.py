import numpy as np
from timeit import timeit
import time
import uuid
import matplotlib.pyplot as plt
import pandas as pd
from numpy import array
import datetime
import time
from pathlib import Path
import pprint

pp = pprint.PrettyPrinter(indent=4)
DATE_STR = datetime.date.today()
Path(f"./output/images/{DATE_STR}/").mkdir(parents=True, exist_ok=True)
Path(f"./output/logs/{DATE_STR}/").mkdir(parents=True, exist_ok=True)
UUIDS_FILE = './data/uuids.csv'

class Tcoki:

    def __init__(self, size):
        # create a dict of {size}:
        self.d = {}
        count = 0
        with open(UUIDS_FILE, encoding="utf-8") as f:
            for line in f:
                if count >= size:
                    break 
                key = line.split(',')[0]
                value = line.split(',')[1]
                if key not in self.d.keys():
                    self.d[key] = value
                else:
                    raise Exception(f"Duplicate key found: {key}!")
                count += 1

    def getLen(self) -> int:
        return len(self.d.keys())

    def insertKey(self):
        key = uuid.uuid4()
        value = "v:" + str(key)
        #if key in self.d.keys():
        #    raise Exception(f"Duplicate key found: {key}!")
        # insert a new key
        self.d[key] = value
        return True


def profileTcokiBucket(timestamp, start, end):

    size_time_data = []
    num_tests = 0

    for size in range(start, end):

        d = Tcoki(size)
        t = timeit("d.insertKey()", globals=locals(), number=1)
        
        size_time_data.append([size,t])
        num_tests += 1


    size_data = [x[0] for x in size_time_data]
    time_data = [x[1] for x in size_time_data]

    # timestamp
    timestamp = int(time.time())

    # standard deviation (time)
    std_time = np.std(time_data)

    data = np.array(size_time_data)
    mean_time = np.mean(time_data, axis=0, dtype=np.float64)
    dataset = pd.DataFrame({'Size': data[:, 0], 'Time': data[:, 1]})

    tcoki_data = dataset
    tcoki_data = tcoki_data[tcoki_data['Size'].notnull()]
    tcoki_data['Time'] = tcoki_data['Time'].fillna(tcoki_data['Time'].mean())
    tcoki_data = tcoki_data.drop_duplicates()

    plt.scatter(tcoki_data['Size'], tcoki_data['Time'])
    #plt.show()

    plt.savefig(f"./output/images/{DATE_STR}/{timestamp}_scatter-{start}-{end}.png")

    data = {
        'size_range': [start, end],
        'mean_time': mean_time,
        'std_time':  std_time,
    }

    Path(f"./logs/{DATE_STR}/").mkdir(parents=True, exist_ok=True)
    with open(f"./output/logs/{DATE_STR}/{timestamp}_logfile.txt", "a") as file:
        file.write(f"{data}\n")

    return data


def profileTcoki(inData=None):

    ts = time.time()

    data = []
    if not inData:
        data.append(profileTcokiBucket(ts, 1, 10))
        data.append(profileTcokiBucket(ts, 10, 100))
        data.append(profileTcokiBucket(ts, 100, 1000))
        #data.append(profileTcokiBucket(ts, 1000, 10000))
        #data.append(profileTcokiBucket(ts, 10000, 100000))
    else:
        data = inData

    x = [d['size_range'][1] for d in data]
    y = [d['mean_time'] for d in data]
    e = [d['std_time'] for d in data]

    fig2, ax2 = plt.subplots()
    ax2.set_title('mean and std results')
    ax2.errorbar(x, y, yerr=e, linestyle='None', ecolor='red', marker='^', capsize=3)
    #ax2.show()
    fig2.savefig(f"./output/images/{DATE_STR}/{ts}_mean_std_error_alt.png")

    return data

