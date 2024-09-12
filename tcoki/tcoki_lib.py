import numpy as np
from timeit import timeit
import time
import uuid
import matplotlib.pyplot as plt
import pandas as pd
from numpy import array
import pprint

pp = pprint.PrettyPrinter(indent=4)

class Tcoki:

    def __init__(self, datafile, size):
        # create a dict of {size}:
        self.d = {}
        count = 0
        with open(datafile, encoding="utf-8") as f:
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
        if key in self.d.keys():
            raise Exception(f"Duplicate key found: {key}!")
        # insert a new key
        self.d[key] = value
        return True


def profileTcokiBucket(datafile, start, end):

    size_time_data = []
    num_tests = 0

    for size in range(start, end):

        d = Tcoki(datafile, size)
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

    #fig1, ax1 = plt.subplots()
    #plt.settitle('insertKey() timeit results')
    plt.scatter(tcoki_data['Size'], tcoki_data['Time'])
    #plt.show()
    plt.savefig(f"./images/{timestamp}_plot-{end}.png")

    data = {
        'size_range': [start, end],
        'mean_time': mean_time,
        'std_time':  std_time,
    }

    with open(f"./logs/{timestamp}.log", "a") as file:
        file.write(f"{data}\n")

    return data


def profileTcoki(inData=None):

    data = []
    if not inData:
        data.append(profileTcokiBucket('./data/uuids.csv', 1, 10))
        data.append(profileTcokiBucket('./data/uuids.csv', 10, 100))
        data.append(profileTcokiBucket('./data/uuids.csv', 100, 1000))
        data.append(profileTcokiBucket('./data/uuids.csv', 1000, 10000))
        data.append(profileTcokiBucket('./data/uuids.csv', 10000, 100000))
    else:
        data = inData

    x = [d['size_range'][1] for d in data]
    y = [d['mean_time'] for d in data]
    e = [d['std_time'] for d in data]

    print(x)
    print(y)
    print(e)

    fig2, ax2 = plt.subplots()
    ax2.set_title('mean and std results')
    ax2.errorbar(x, y, yerr=e, linestyle='None', ecolor='red', marker='^', capsize=3)
    #ax2.show()
    fig2.savefig(f"./images/mean_std_error_alt.png")

    return data

