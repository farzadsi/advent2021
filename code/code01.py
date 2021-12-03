import os
import re

import numpy as np

cdir = os.path.dirname(__file__)
os.chdir(cdir)
os.getcwd()

with open("../data/data01") as file:
    data = file.read().splitlines()

data = [int(n) for n in data]
diff = [np.nan]
sumslide = []
for i, n in enumerate(data[:-1]):
    diff.append(data[i+1] > n)

for i, n in enumerate(data[:-2]):
    # print(data[i:i+3])
    sumslide.append(sum(data[i:i+3]) < sum(data[i+1:i+4]))

print('number of increasing depth: ', diff.count(True))
print('number of window increasing depth:', sumslide.count(True))
print('done')
