import os
import re

import numpy as np

cdir = os.path.dirname(__file__)
os.chdir(cdir)
os.getcwd()

with open("../data/data03") as file:
    data = file.read().splitlines()

gamma_rate = str()
epsilon_rate = str()
for i in range(len(data[0])):
    lst = [a[i] for a in data]
    gamma_rate += max(lst, key=lst.count)
    epsilon_rate += min(lst, key=lst.count)

def max_count(lst):
    if lst.count('1') != lst.count('0'):
        return max(lst, key=lst.count)
    else:
        return '1'

def min_count(lst):
    if lst.count('1') != lst.count('0'):
        return min(lst, key=lst.count)
    else:
        return '0'


def oxy_rating(data):
    cdata = data.copy()
    for i in range(len(data[0])):
        lst = [a[i] for a in cdata]
        sel_val = max_count(lst)
        cdata = [a for a in cdata if a[i] == sel_val]
        if len(cdata) == 1:
            return cdata[0]


def co2_rating(data):
    cdata = data.copy()
    for i in range(len(data[0])):
        lst = [a[i] for a in cdata]
        sel_val = min_count(lst)
        cdata = [a for a in cdata if a[i] == sel_val]
        if len(cdata) == 1:
            return cdata[0]


ox_rate = oxy_rating(data)
co2_rate = co2_rating(data)

dec_mult = int(gamma_rate, 2) * int(epsilon_rate, 2)
dec_lsup = int(ox_rate, 2) * int(co2_rate, 2)

print('gamma_rate x epsilon rate: ', dec_mult)
print('life support rating rate: ', dec_lsup)
