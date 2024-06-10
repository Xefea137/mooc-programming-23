# Write your solution here
def anagrams(string1, string2):
    if sorted(string1) == sorted(string2):
        return True
    else:
        return False
    #return sorted(string1) == sorted(string2)

if __name__ == "__main__":
    print(anagrams("tame", "meta")) # True
    print(anagrams("tame", "mate")) # True
    print(anagrams("tame", "team")) # True
    print(anagrams("tabby", "batty")) # False
    print(anagrams("python", "java")) # False