import os
import re

import numpy as np

cdir = os.path.dirname(__file__)
os.chdir(cdir)
os.getcwd()

with open("../data/data02") as file:
    data = file.read().splitlines()

p = re.compile('([a-z]*) (\d*)')

def get_matrix(direction):
    if direction == 'forward':
        return np.array([1, 0])
    elif direction == 'down':
        return np.array([0, 1])
    elif direction == 'up':
        return np.array([0, -1])
    else:
        raise 'wrong line'

def get_new_matrix(direction, aim):
    if direction == 'forward':
        return np.array([1, 1 * aim, 0])
    elif direction == 'down':
        return np.array([0, 0, 1])
    elif direction == 'up':
        return np.array([0, 0, -1])
    else:
        raise 'wrong line'



location = np.array([0, 0])
for line in data:
    direction = p.search(line)[1]
    step = int(p.search(line)[2])
    mat = get_matrix(direction)
    location += mat * step

print('multiplication of x and depth: ', np.multiply(*location))

# [x, depth] aim
geoloc = np.array([0, 0, 0])
for line in data:
    direction = p.search(line)[1]
    step = int(p.search(line)[2])
    mat = get_new_matrix(direction, geoloc[2])
    geoloc += mat * step

print('multiplication of x and depth with aim: ', np.multiply(*geoloc[0:2]))

print('done')
