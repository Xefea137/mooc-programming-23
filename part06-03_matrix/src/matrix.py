# write your solution here
def matrix_sum():
    sum = 0
    with open("matrix.txt") as file:
        for line in file:
            line = line.split(",")
            for item in range(len(line)):
                sum += int(line[item])
    return sum

def matrix_max():
    greatest = 0
    with open("matrix.txt") as file:
        for line in file:
            line = line.split(",")
            for item in range(len(line)):
                if int(line[item]) > greatest:
                    greatest = int(line[item])
    return greatest

def row_sums():
    sum = 0
    sum_row_list = []
    with open("matrix.txt") as file:
        for line in file:
            line = line.split(",")
            for item in range(len(line)):
                sum += int(line[item])
            sum_row_list.append(sum)
            sum = 0
    return sum_row_list

if __name__ == "__main__":
    matrix_sum()
    matrix_max()
    row_sums()