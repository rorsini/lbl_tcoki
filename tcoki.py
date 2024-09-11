#!/usr/bin/env python

import numpy as np
from timeit import timeit
import uuid
import logging
import matplotlib.pyplot as plt
import pandas as pd

#logging.basicConfig(level=logging.INFO)

class Tcoki:

    def __init__(self, size: int) -> int:
        # create a dict of {size}:
        self.d = {}
        logging.debug(f"making a dict of size {size}")
        for n in range(size):
            key = uuid.uuid4()
            value = "v:" + str(key)
            if key not in self.d.keys():
                self.d[key] = value
            else:
                raise Exception(f"Duplicate key found: {key}!")

    def getLen(self) -> int:
        return len(self.d.keys())

    def insertKey(self) -> str:
        key = uuid.uuid4()
        value = "v:" + str(key)
        if key in self.d.keys():
            raise Exception(f"Duplicate key found: {key}!")
        # insert a new key
        self.d[key] = value
        logging.debug("key inserted")
        return f"size: {len(self.d.keys())} {key}: {self.d[key]}"



def profileTcoki(start=1, end=1000):

    res, td = [], []
    num_tests = 0

    for size in range(start, end):

        d = Tcoki(size)
        logging.info(f"dict size: {d.getLen()}")

        t = timeit("d.insertKey()", globals=locals(), number=10)
        
        td.append(t)
        res.append([size,t])
        #print('{:f}'.format(t), size)
        num_tests += 1


    stdt = np.std(td)

    data = np.array(res)

    mean = np.mean(res, axis=0, dtype=np.float64)

    dataset = pd.DataFrame({'Size': data[:, 0], 'Time': data[:, 1]})

    tcoki_data = dataset
    tcoki_data = tcoki_data[tcoki_data['Size'].notnull()]
    tcoki_data['Time'] = tcoki_data['Time'].fillna(tcoki_data['Time'].mean())
    tcoki_data = tcoki_data.drop_duplicates()
    plt.scatter(tcoki_data['Size'], tcoki_data['Time'])
    #plt.show()
    plt.savefig(f"./plot-{end}.png")

    return {
        'dict size': [start, end],
        'std(time)': stdt,
        'mean': mean,
    }


## Run profile buckets:
#for size in range(1, 5000, 1000):
#    print(profileTcoki(start=size, end=size+1000))


ste = [ {'dict size': [1, 1001], 'std(time)': np.float64(8.635842282555293e-06), 'mean': [5.00500000e+02, 8.55922541e-05]},
        {'dict size': [1001, 2001], 'std(time)': np.float64(9.529766907987224e-06), 'mean': [1.50050000e+03, 8.81218009e-05]},
        {'dict size': [2001, 3001], 'std(time)': np.float64(1.0069549750500673e-05), 'mean': [2.50050000e+03, 9.00490589e-05]},
        {'dict size': [3001, 4001], 'std(time)': np.float64(1.0652099749207155e-05), 'mean': [3.50050000e+03, 9.07631273e-05]},
        {'dict size': [4001, 5001], 'std(time)': np.float64(1.063846178576672e-05), 'mean': [4.50050000e+03, 9.18800132e-05]}, ]


y = [x['std(time)'] for x in ste]
x = [1000,2000,3000,4000,5000]
e = [.1,.2,.3,.4,.5] 

plt.errorbar(x, y, e, linestyle='None', ecolor='red', marker='^', capsize=3)
plt.savefig(f"./mean_std_error.png")

