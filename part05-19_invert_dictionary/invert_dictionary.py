# Write your solution here
def invert(dictionary: dict):
    temp_d = {}
    for key, value in dictionary.items():
        temp_d[key] = value
    dictionary.clear()
    for key, value in temp_d.items():
        dictionary[value] = key

if __name__ == "__main__":
    s = {1: "first", 2: "second", 3: "third", 4: "fourth"}
    invert(s)
    print(s)