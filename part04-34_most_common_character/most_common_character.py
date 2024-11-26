# Write your solution here
def most_common_character(string: str):
    i = 0
    count = 0
    high = 0
    char = ""
    while len(string) > i:
        count = string.count(string[i])
        if count > high:
            high = count
            char = string[i]
        i += 1
    return char

if __name__ == "__main__":
    first_string = "abcdbde"
    print(most_common_character(first_string))

    second_string = "exemplaryelementary"
    print(most_common_character(second_string))