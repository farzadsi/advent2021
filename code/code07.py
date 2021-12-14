import os
import time
import numpy as np

cdir = os.path.dirname(__file__)
os.chdir(cdir)
os.getcwd()

with open("../data/data07") as file:
    # data = file.read().split('\n')
    data = file.read().split(',')

data = [int(i) for i in data]

position = int(np.quantile(data, 0.5))

print('Fuel consumption with constant fuel consumption ', sum(abs(np.array(data) - position)))

position = np.mean(data)
low = abs(np.array(data) - np.round(position))
high = abs(np.array(data) - np.round(position) + 1)
low = sum([i * (i + 1) / 2 for i in low])
high = sum([i * (i + 1) / 2 for i in high])
print('Fuel consumption with increased fuel consumption ', low if low < high else high)
print('done')
