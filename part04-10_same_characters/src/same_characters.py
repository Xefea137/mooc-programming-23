# Write your solution here
def same_chars(string, x, y):
    if y > len(string)-1 or x > len(string)-1:
        return False
    elif string[x] != string[y]:
        return False
    elif string[x] == string[y]:
        return True
    
# You can test your function by calling it within the following block
if __name__ == "__main__":
    print(same_chars("abc", 0, 3))

'''
if y > len(string)-1 or x > len(string)-1 or string[x] != string[y]:
        return False
    return True
'''