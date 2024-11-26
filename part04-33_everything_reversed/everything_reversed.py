# Write your solution here
def everything_reversed(list: list):
    new = []
    x = len(list) - 1
    for x in list[::-1]:
        new.append(x[::-1])
    return new

if __name__ == "__main__":
    my_list = ["Hi", "there", "example", "one more"]
    new_list = everything_reversed(my_list)
    print(new_list)