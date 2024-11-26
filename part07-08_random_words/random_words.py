# Write your solution here
from random import sample

def words(n: int, beginning: str):
    x = []
    with open("words.txt") as file:
        for word in file:
            word = word.strip()
            if word.startswith(beginning):
                if word not in x:
                    x.append(word)

    if len(x) < n:
        raise ValueError("Not enough words")
    else:
        return sample(x,n)

if __name__ == "__main__":
    word_list = words(3, "castl")
    for word in word_list:
        print(word)