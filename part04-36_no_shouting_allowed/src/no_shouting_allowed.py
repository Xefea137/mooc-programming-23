# Write your solution here
def no_shouting(list: list):
    new_list = []
    for name in list:
        if name.isupper() == False:
            new_list.append(name)
    return new_list

if __name__ == "__main__":
    my_list = ["ABC", "def", "UPPER", "ANOTHERUPPER", "lower", "another lower", "Capitalized"]
    pruned_list = no_shouting(my_list)
    print(pruned_list)