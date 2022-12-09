import numpy as np
import math, random

original_sudoku = np.array([
    [8,1,2,0,0,0,0,0,0],
    [0,0,3,6,0,0,0,0,0],
    [0,7,0,0,9,0,2,0,0],
    [0,5,0,0,0,7,0,0,0],
    [0,0,0,0,4,5,7,0,0],
    [0,0,0,1,0,0,0,3,0],
    [0,0,1,0,0,0,0,6,8],
    [4,0,8,5,0,0,0,1,0],
    [7,9,6,3,1,8,4,5,2]
])


possibility_indexes = np.zeros((9,9), np.uint8)

def check_column(loc, current_state, sudoku):
    for number in sudoku[loc]:
        if (number == 0): continue

        current_state.remove(number)

    return current_state

def check_row(loc, current_state, sudoku):
    for number in sudoku[:, loc]:
        if (number == 0 or number not in current_state): continue

        current_state.remove(number)

    return current_state

def check_cell(loc, current_state, sudoku):
    cell_col = math.floor(loc[0]/3)*3
    cell_row = math.floor(loc[1]/3)*3

    cell = sudoku[cell_col:cell_col+3, cell_row:cell_row+3]
    cell = cell.flatten()

    for number in cell:
        if (number == 0 or number not in current_state): continue

        current_state.remove(number)

    return current_state

def find_possibilities(loc, sudoku):
    state = [1,2,3,4,5,6,7,8,9]


    state = check_column(loc[0], state, sudoku)
    state = check_row(loc[1], state, sudoku)
    state = check_cell(loc, state, sudoku)
    
    return state


def solve(sudoku):
    changes = 1
    while changes > 0:
        changes = 0
        for col in range(9):
            for row in range(9):
                if (sudoku[col][row] > 0): continue

                possibilities = find_possibilities((col, row), sudoku)

                
                if (len(possibilities) == 1):
                    sudoku[col][row] = possibilities[0]
                    changes += 1




    valid_indexes = []
    curr_index = 0
    backing = False

    while curr_index < 81:
        col = curr_index % 9
        row = math.floor(curr_index/9)

        if (backing):
            backing = False
            sudoku[col][row] = 0
            valid_indexes.remove(curr_index)


        if (sudoku[col][row] > 0):
            curr_index += 1
            continue 


        valid_indexes.append(curr_index)

        possibilities = find_possibilities((col, row), sudoku)
        possibility_index = possibility_indexes[col][row]
        # print(possibility_index, possibilities, curr_index, valid_indexes)


        if (len(possibilities) <= possibility_index):
            possibility_indexes[col][row] = 0
            sudoku[col][row] = 0
            valid_indexes.remove(curr_index)
            curr_index = valid_indexes[-1]
            backing = True
            # print("backing up to ",curr_index)
            continue

        sudoku[col][row] = possibilities[possibility_index]
        possibility_indexes[col][row] += 1

    return sudoku

def generate_sudoku(difficulty_percentage):
    sudoku = np.zeros((9,9), np.uint8)

    one_to_nine_range = list(range(1,10))
    print(one_to_nine_range)
    sudoku[0] = random.sample(range(1,10), 9)

    sudoku = solve(sudoku)
    for col in range(9):
        for row in range(9):
            if (np.random.rand() < difficulty_percentage):
                sudoku[col][row] = 0

    return sudoku


