#!/usr/bin/env python

from tcoki import profileTcoki
import numpy as np
from numpy import array
import pprint

data = [
    {'size_range': [1, 10], 'mean_time': np.float64(1.9334217843910057e-05), 'std_time': np.float64(6.577901417405355e-06)},
    {'size_range': [10, 100], 'mean_time': np.float64(1.8043926037434075e-05), 'std_time': np.float64(4.022633755827987e-06)},
    {'size_range': [100, 1000], 'mean_time': np.float64(2.2379783654792442e-05), 'std_time': np.float64(8.042521196087182e-06)},
    {'size_range': [1000, 10000], 'mean_time': np.float64(8.860559031988184e-05), 'std_time': np.float64(5.263201767485302e-05)},
    {'size_range': [10000, 100000], 'mean_time': np.float64(0.0015507531675199668), 'std_time': np.float64(0.0008694342600839186)},
]

#res = profileTcoki(data)
res = profileTcoki()

pp = pprint.PrettyPrinter(indent=4)
pp.pprint(res)


