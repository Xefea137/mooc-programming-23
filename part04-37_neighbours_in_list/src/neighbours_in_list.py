# Write your solution here
def longest_series_of_neighbours(list: list):
    i = 1
    size = 1
    longest = 1
    while i < len(list):
        if abs(list[i-1] - list[i]) == 1:
            size += 1
        else:
            size = 1
        longest = max(longest,size)
        i += 1
    return longest

if __name__ == "__main__":
    my_list = [1, 2, 5, 7, 6, 5, 6, 3, 4, 1, 0] #4
    print(longest_series_of_neighbours(my_list))
    my_list = [1, 2, 3, 5, 6, 9, 10] #3
    print(longest_series_of_neighbours(my_list))
    my_list = [0, 1, 2, 3, 4, 5, 9, 10, 11, 2, 3, 4] #6
    print(longest_series_of_neighbours(my_list))
    my_list = [1, 2, 3, 5, 6, 7, 6, 5, 6, 7, 10, 11, 10] #7
    print(longest_series_of_neighbours(my_list))