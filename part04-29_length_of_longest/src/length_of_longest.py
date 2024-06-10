# Write your solution here
def length_of_longest(list: list):
    longest = list[0]
    for string in list:
        if len(string) > len(longest):
            longest = string
    return len(longest)

if __name__ == "__main__":
    my_list = ["first", "second", "fourth", "eleventh"]
    result = length_of_longest(my_list)
    print(result)
    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]
    result = length_of_longest(my_list)
    print(result)