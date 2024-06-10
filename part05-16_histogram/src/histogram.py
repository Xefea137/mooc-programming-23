# Write your solution here
def histogram(word: str):
    star = {}
    for letter in word:
        if letter not in star:
            star[letter] = []
        star[letter].append("*")

    for key, values in star.items():
        print(key, end=" ")
        for item in values:
            print(item, end="")
        print()

if __name__ == "__main__":
    histogram("abba")
    histogram("statistically")