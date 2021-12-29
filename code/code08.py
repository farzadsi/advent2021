import os
import time
import numpy as np

cdir = os.path.dirname(__file__)
os.chdir(cdir)
os.getcwd()

Ground_Truth = {1: 'cf', 7: 'acf', 4: 'bcdf', 8: 'abcdefg',
                5: 'abdfg', 2: 'acdeg', 3: 'acdfg',
                9: 'abcdfg', 0: 'abcefg', 6: 'abdefg'
                }


def import_data(file_path):
    with open(file_path) as file:
        data = file.read().split('\n')
        # data = file.read().split(',')
    outdata = list()
    for c_data in data:
        cdata = dict()
        input_data, output_data = c_data.split(' | ')
        cdata['in'] = input_data.split(' ')
        cdata['out'] = output_data.split(' ')
        outdata.append(cdata)
    return outdata


def count_easy_nums(idata):
    total = 0
    for cdata in idata:
        k = [i for i in cdata['out'] if len(i) in [2, 3, 4, 7]]
        total += len(k)
    return total


unique_vals = {2: 1, 3: 7, 4: 4, 7: 8}


def create_and_get_easy(numbers):
    key_dict = dict()
    for vals in numbers:
        if len(vals) == 2:
            key_dict[1] = vals
        elif len(vals) == 3:
            key_dict[7] = vals
        elif len(vals) == 4:
            key_dict[4] = vals
        elif len(vals) == 7:
            key_dict[8] = vals
    return key_dict


def get_the_rest(numbers, keys):
    for cn in numbers:
        if len(cn) == 5:
            if len([i for i in cn if i not in keys[7]]) == 2:
                keys[3] = cn
            elif len([i for i in cn if i not in keys[4]]) == 3:
                keys[2] = cn
            else:
                keys[5] = cn
        if len(cn) == 6:
            if len([i for i in cn if i not in keys[4]]) == 2:
                keys[9] = cn
            elif len([i for i in cn if i not in keys[7]]) == 4:
                keys[6] = cn
            else:
                keys[0] = cn
    return {"".join(sorted(j)): i for i, j in keys.items()}


def get_out_numbers(out, keys):
    vals = [keys[''.join(sorted(i))] for i in out]
    return vals[0] * 1000 + vals[1] * 100 + vals[2] * 10 + vals[3]


data = import_data("../data/data08")

total = 0
for cline in data:
    ckeys = create_and_get_easy(cline['in'])
    ckeys = get_the_rest(cline['in'], ckeys)
    c_num = get_out_numbers(cline['out'], ckeys)
    total += c_num

print(f'total number of 1,4,7,0 repeats: {count_easy_nums(data)}')
print(f'sum of all output numbers: {total}')
