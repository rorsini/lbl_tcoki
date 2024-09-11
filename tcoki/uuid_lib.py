#!/usr/bin/env python

import uuid

def makeUuidDatafile(size=1000000):

    with open(f"../data/uuids_{size}.csv", 'w') as file:

        for n in range(size):

            key = str(uuid.uuid4())
            value = "v:" + str(key)
            data = f"{key},{value}\n"

            file.write(data)

