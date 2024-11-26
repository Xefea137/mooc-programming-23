# Write your solution here
def all_the_longest(list: list):
    new_list = []
    longest = list[0]
    for string in list:
        if len(string) > len(longest):
            longest = string
    for string in list:
        if len(string) == len(longest):
            new_list.append(string)
    return new_list

if __name__ == "__main__":
    my_list = ["first", "second", "fourth", "eleventh"]
    result = all_the_longest(my_list)
    print(result) # ['eleventh']
    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]
    result = all_the_longest(my_list)
    print(result) # ['dorothy', 'richard']