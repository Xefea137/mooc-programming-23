# Write your solution here
def transpose(matrix: list):
    for row in range(len(matrix)):
        for column in range(row,len(matrix[row])):
            temp = matrix [row][column]
            matrix[row][column] = matrix[column][row]
            matrix[column][row] = temp

if __name__ == "__main__":
    m = [[1,2,3],[4,5,6],[7,8,9]]
    print(m)
    transpose(m)
    print(m)