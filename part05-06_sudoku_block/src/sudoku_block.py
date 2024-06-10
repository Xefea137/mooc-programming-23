# Write your solution here
def block_correct(sudoku: list, row_no: int, column_no: int):
    check_list = []
    for i in range(row_no,row_no+3):
        for j in range(column_no,column_no+3):
            if sudoku[i][j] > 0 and sudoku[i][j] in check_list:
                return False
            check_list.append(sudoku[i][j])
    return True

if __name__ == "__main__":
    sudoku = [
        [9, 0, 0, 0, 8, 0, 3, 0, 0],
        [2, 0, 0, 2, 5, 0, 7, 0, 0],
        [0, 2, 0, 3, 0, 0, 0, 0, 4],
        [2, 9, 4, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 7, 3, 0, 5, 6, 0],
        [7, 0, 5, 0, 6, 0, 4, 0, 0],
        [0, 0, 7, 8, 0, 3, 9, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 3],
        [3, 0, 0, 0, 0, 0, 0, 0, 2]
        ]

    print(block_correct(sudoku, 0, 0))  #False
    print(block_correct(sudoku, 1, 2))  #True