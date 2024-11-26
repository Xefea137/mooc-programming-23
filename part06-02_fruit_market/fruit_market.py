# write your solution here
def read_fruits():
    fruit_dictionary = {}
    with open("fruits.csv") as new_file:
        for line in new_file:
            parts = line.split(";")
            fruit_dictionary[parts[0]] = float(parts[1])
    return fruit_dictionary

if __name__ == "__main__":
    read_fruits()