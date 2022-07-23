def sudoku(puzzle):
    """return the solved puzzle as a 2d array of 9 x 9"""
    number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    # change 0 to any number
    for row in puzzle:
        for item in row:
            if item == 0:
                for number in number_list:
                    if number not in row:
                        puzzle[puzzle.index(row)][row.index(item)] = number
    # find a solution later
    return puzzle

puzzle = [[5,3,0,0,7,0,0,0,0],
          [6,0,0,1,9,5,0,0,0],
          [0,9,8,0,0,0,0,6,0],
          [8,0,0,0,6,0,0,0,3],
          [4,0,0,8,0,3,0,0,1],
          [7,0,0,0,2,0,0,0,6],
          [0,6,0,0,0,0,2,8,0],
          [0,0,0,4,1,9,0,0,5],
          [0,0,0,0,8,0,0,7,9]]

lists= sudoku(puzzle)
for _ in lists:
    print(_)