#!/usr/bin/env python

import uuid

with open('../data/uuids.csv', 'w') as file:

    fields = 'Key,Value,\n'
    file.write(fields)

    for n in range(1000000):

        key = str(uuid.uuid4())
        value = "v:" + str(key)
        data = f"{key},{value},\n"

        file.write(data)

