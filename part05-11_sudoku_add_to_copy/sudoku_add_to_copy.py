# Write your solution here
def print_sudoku(sudoku: list):
    for row in range(9):
        if row > 0 and row % 3 == 0:
            print()
        for column in range(9):
            if sudoku[row][column] == 0:
                print("_", end=" ")
            else:
                print(sudoku[row][column], end=" ")
            if (column+1) % 3 == 0:
                print(" ", end="")
        print()

def copy_and_add(sudoku: list, row_no: int, column_no: int, number: int):
    temp_sudoku = []
    for row in sudoku:
        new_row = []
        for element in row:
            new_row.append(element)
        temp_sudoku.append(new_row)
    temp_sudoku[row_no][column_no] = number
    return temp_sudoku

if __name__ == "__main__":
    sudoku  = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    grid_copy = copy_and_add(sudoku, 0, 0, 2)
    print("Original:")
    print_sudoku(sudoku)
    print()
    print("Copy:")
    print_sudoku(grid_copy)