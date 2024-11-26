# WRITE YOUR SOLUTION HERE:
import string
def most_common_words(filename: str, lower_limit: int):
    words = []
    with open(filename) as file:
        for line in file:
            words += [word.strip(string.whitespace+string.punctuation) for word in line.split()]

    return {word: words.count(word) for word in words if words.count(word) >= lower_limit}

if __name__ == "__main__":
    print(most_common_words('programming.txt', 4))