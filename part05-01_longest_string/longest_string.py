# Write your solution here
def longest(strings: list):
    word = ""
    for words in strings:
        if len(words) > len(word):
            word = words
    return word
    
if __name__ == "__main__":
    strings = ["hi", "hiya", "hello", "howdydoody", "hi there"]
    print(longest(strings))