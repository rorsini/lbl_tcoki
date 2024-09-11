import numpy as np
from timeit import timeit
from datetime import datetime
import uuid
import matplotlib.pyplot as plt
import pandas as pd

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


def profileTcoki(datafile, start, end):

    res, td = [], []
    num_tests = 0

    for size in range(start, end):

        d = Tcoki(datafile, size)
        t = timeit("d.insertKey()", globals=locals(), number=10)
        
        td.append(t)
        res.append([size,t])
        num_tests += 1

    stdt = np.std(td)
    data = np.array(res)
    mean = np.mean(res, axis=0, dtype=np.float64)
    dataset = pd.DataFrame({'Size': data[:, 0], 'Time': data[:, 1]})

    tcoki_data = dataset
    tcoki_data = tcoki_data[tcoki_data['Size'].notnull()]
    tcoki_data['Time'] = tcoki_data['Time'].fillna(tcoki_data['Time'].mean())
    tcoki_data = tcoki_data.drop_duplicates()

    now = datetime.now()
    today = now.strftime("%Y-%m-%d")
    date = str(now)

    plt.scatter(tcoki_data['Size'], tcoki_data['Time'])
    plt.show()
    #plt.savefig(f"./images/{today}/plot-{end}.png")

    data = {
        'size': [start, end],
        'std': stdt,
        'mean': mean,
    }

    with open(f"./data/{today}/output.log", "a") as file:
        file.write(f"{date} | {data}\n")

    return data

