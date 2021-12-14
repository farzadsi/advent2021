import os
import re
import numpy as np

cdir = os.path.dirname(__file__)
os.chdir(cdir)
os.getcwd()

with open("../data/data05") as file:
    # data = file.read().split('\n')
    data = file.read().split('\n')


def parse_data(data, only_h_v_lines=True):
    row_patt = re.compile('(\d*),(\d*) -> (\d*),(\d*)')
    update_data = list()
    max_val = 0
    for line in data:
        vals = row_patt.search(line)
        vals = [int(vals[1]), int(vals[2]), int(vals[3]), int(vals[4])]
        max_val = max(max(vals), max_val)
        if only_h_v_lines:
            if not ((vals[0] == vals[2]) or (vals[1] == vals[3])):
                continue
        max_space = max(abs(vals[2] - vals[0]), abs(vals[3] - vals[1])) + 1
        coords = [np.linspace(vals[0], vals[2], max_space, endpoint=True).astype(int),
                  np.linspace(vals[1], vals[3], max_space, endpoint=True).astype(int)]
        update_data.append(coords)
    return update_data, max_val + 1


data_hv_lines, max_vals = parse_data(data)
data_all_lines, _ = parse_data(data, only_h_v_lines=False)


def get_danger_numbers(data, field_extent):
    field = np.zeros(field_extent * field_extent).reshape(field_extent, field_extent)
    for vals in data:
        field[vals] += 1
    return np.where(field > 1)[0].shape


danger_hv = get_danger_numbers(data_hv_lines, field_extent=max_vals)
danger_all = get_danger_numbers(data_all_lines, field_extent=max_vals)

print(f'number of danger fields when only horizontal and vertical are considered: {danger_hv}')
print(f'number of danger fields when  horizontal, vertical, and diagonal are considered: {danger_all}')

print('done')
