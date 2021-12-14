import os
import time
import numpy as np

cdir = os.path.dirname(__file__)
os.chdir(cdir)
os.getcwd()

with open("../data/data06") as file:
    # data = file.read().split('\n')
    data = file.read().split(',')

days = 256
data = [int(i) for i in data]


def count_fish_number(darr, day):
    partial = 0
    for i in range(day):
        babies = darr.size - np.count_nonzero(darr)
        babies = np.repeat(8, babies).astype(int)
        darr = np.where(darr == 0, 6, darr - 1)
        darr = np.append(darr, babies)
        if len(darr) > 10000000:
            # using 'set' to only calculate the offspring once per age of mother fish
            for j in set(darr):
                offsprings = count_fish_number(j, day - i - 1)  # Number of days left need index correction of 1
                partial += offsprings * (np.where(darr == j)[0].shape[0])
            return partial
    return len(darr)


now = time.time()
total = count_fish_number(np.array(data, dtype=int), day=days)
print(f'time: {time.time() - now}')

print(f'number of fishes: {total}')
print('done')
