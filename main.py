import numpy as np
# cduartes
# mcampusano
# dsoto

class Matrix(object):
    def __init__(self, dim, col, row):
        self.matrix = np.zeros(shape=(dim[0], dim[1]))
        self.col = col
        self.row = row

def first_rule(board):
    for index, col in enumerate(board.col):
        if len(col) > 1:
            if (sum(col) + len(col) - 1) == board.matrix.shape[1]:
                current = 0
                for hint in col:
                    for value in range(0 + current, hint + current):
                        board.matrix[value, index] = 1
                        current += 1
                    current += 1
                    if current < board.matrix.shape[1]:
                        board.matrix[current -1, index] = -1
    for index, row in enumerate(board.row):
        if len(row) > 1:
            if (sum(row) + len(row) - 1) == board.matrix.shape[0]:
                current = 0
                for hint in row:
                    for value in range(0 + current, hint + current):
                        board.matrix[index, value] = 1
                        current += 1
                    current += 1
                    if current < board.matrix.shape[0]:
                        board.matrix[index, current] = -1
    print(board.matrix)

if __name__ == "__main__":
    print("---- nonograms ----")
    #read board file (clues)
    lines = [line.rstrip('\n') for line in open('input.txt')]
    dim = eval(lines[0]) #dimension
    h_hints = eval(lines[1]) #horizontal hints
    v_hints = eval(lines[2]) #vertical hints
    b = Matrix(dim, h_hints, v_hints)
    first_rule(b)
