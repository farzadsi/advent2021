import os

import numpy as np

cdir = os.path.dirname(__file__)
os.chdir(cdir)
os.getcwd()


class Board:
    def __init__(self, board_vals):
        board_vals = board_vals.splitlines()
        self.board_values = np.array([a.split() for a in board_vals]).astype(int)
        self.winner = False

    def add_num(self, number):
        self.board_values = np.where(self.board_values == number, -1, self.board_values)
        self.update_status()

    def update_status(self):
        for n in range(self.board_values.shape[0]):
            if ((self.board_values[n, :] == -1).all()) or ((self.board_values[:, n] == -1).all()):
                self.winner = True
                break

        # self.board_status row or col are all gotit


with open("../data/data04") as file:
    data = file.read().split('\n\n')

numbers = [int(a) for a in data[0].split(',')]

boards = [Board(a) for a in data[1:]]

sum_unmarked = 0
final_number = 0
for i, curr_num in enumerate(numbers):
    [a.add_num(curr_num) for a in boards]
    winner_board = [a for a in boards if a.winner]
    if winner_board:
        boards = [a for a in boards if not a.winner] # only needed for part 2
        # which board
        winner_board = winner_board[0]
        # sum of all values left + sum of -1
        sum_unmarked = winner_board.board_values.sum() + np.sum(np.where(winner_board.board_values == -1, True, False))
        final_number = curr_num
        # break  # uncomment for part 1 and comment for part 2

print('final score: ', sum_unmarked * final_number)
