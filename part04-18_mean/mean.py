# Write your solution here
def mean(list: list):
    return sum(list)/len(list)
# You can test your function by calling it within the following block
if __name__ == "__main__":
    my_list = [1, 6, -4]
    #my_list = [1, 3, 67, 7, 4, 23, 1, 5, 7, 4]
    result = mean(my_list)
    print(result)