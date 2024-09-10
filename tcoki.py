#!/usr/bin/env python

import numpy as np
from timeit import timeit
import uuid
import logging

#logging.basicConfig(level=logging.INFO)

class Tcoki:

    def __init__(self, size: int) -> int:
        # create a dict of {size}:
        self.d = {}
        logging.debug(f"making a dict of size {size}")
        for n in range(1, size, 10):
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


sd, td = [], []

num_tests = 0
for size in range(1, 10000, 10):

    d = Tcoki(size)
    logging.info(f"dict size: {d.getLen()}")

    # profile 100 inserts:
    g = globals()
    t = timeit("d.insertKey()", globals=g, number=100)
    
    sd.append(size)
    td.append(t)
    print(t)
    num_tests += 1


print(f"total tests run: {num_tests}")


stdt = np.std(td)
print(f"std of time is: {stdt}")

stds = np.std(sd)
print(f"std of size is: {stds}")



