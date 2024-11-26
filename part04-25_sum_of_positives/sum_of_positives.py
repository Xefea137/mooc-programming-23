# Write your solution here
def sum_of_positives(list: list):
    x = 0
    for i in list:
        if i > 0:
            x += i
    return x

if __name__ == "__main__":
    #my_list = [1, -2, 3, -4, 5]
    #my_list = [1, -1, 2, -2, 3, -3]
    my_list = [-10, -8, -6, -4, -2]
    result = sum_of_positives(my_list)
    print("The result is", result)