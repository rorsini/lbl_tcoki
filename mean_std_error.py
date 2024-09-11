#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt

ste = [ {'dict size': [1, 1001], 'std(time)': np.float64(8.635842282555293e-06), 'mean': [5.00500000e+02, 8.55922541e-05]},
        {'dict size': [1001, 2001], 'std(time)': np.float64(9.529766907987224e-06), 'mean': [1.50050000e+03, 8.81218009e-05]},
        {'dict size': [2001, 3001], 'std(time)': np.float64(1.0069549750500673e-05), 'mean': [2.50050000e+03, 9.00490589e-05]},
        {'dict size': [3001, 4001], 'std(time)': np.float64(1.0652099749207155e-05), 'mean': [3.50050000e+03, 9.07631273e-05]},
        {'dict size': [4001, 5001], 'std(time)': np.float64(1.063846178576672e-05), 'mean': [4.50050000e+03, 9.18800132e-05]}, ]

y = [x['std(time)'] for x in ste]
x = [1000,2000,3000,4000,5000]
e = [.1,.2,.3,.4,.5] 

plt.errorbar(x, y, e, linestyle='None', ecolor='red', marker='^', capsize=3)
plt.savefig(f"./images/mean_std_error_alt.png")

