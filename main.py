#!/usr/bin/env python

from tcoki import Tcoki
from tcoki import profileTcoki

#t = Tcoki('./data/uuids.csv', 10000)
#print(t.getLen())

# Run five profile buckets:
print(profileTcoki('./data/uuids.csv', 1, 1000))
print(profileTcoki('./data/uuids.csv', 1000, 2000))
print(profileTcoki('./data/uuids.csv', 2000, 3000))
print(profileTcoki('./data/uuids.csv', 3000, 4000))
print(profileTcoki('./data/uuids.csv', 4000, 5000))



#print(profileTcoki('./data/uuids.csv', 1, 10))
#print(profileTcoki('./data/uuids.csv', 10, 100))
#print(profileTcoki('./data/uuids.csv', 100, 1000))
#print(profileTcoki('./data/uuids.csv', 1000, 10000))
#print(profileTcoki('./data/uuids.csv', 10000, 100000))

