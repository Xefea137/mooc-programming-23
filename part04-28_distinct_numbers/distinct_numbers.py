# Write your solution here
def distinct_numbers(list: list):
    new_list = []
    number = 0
    list.sort()
    for i in list:
        if number == i:
            continue
        else:
            new_list.append(i)
        number = i
    return new_list

if __name__ == "__main__":
    my_list = [3, 2, 2, 1, 3, 3, 1]
    print(distinct_numbers(my_list)) # [1, 2, 3]

'''
def distinct_numbers(my_list: list):
    results = []
    for item in my_list:
        if item not in results:
            results.append(item)
    results.sort()
    return results
'''