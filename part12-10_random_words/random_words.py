# Write your solution here:
import random
def word_generator(characters: str, length: int, amount: int):
    return ("".join(random.sample(characters, length))for i in range(amount))
    #return ("".join([choice(letters ) for i in range(length)]) for j in range(amount))

if __name__ == "__main__":
    wordgen = word_generator("abcdefg", 3, 5)
    for word in wordgen:
        print(word)