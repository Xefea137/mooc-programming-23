# Write your solution here
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
size = int(input("Enter Layers: "))
left = ""
right = ""
char = size-1
f = size + (size-1)
count = 0

while count < (size + (size-1))//2:
    left = left + letters[char]
    right = letters[char] + right
    f -= 2
    middle = letters[char] * f
    print(left+middle+right)
    char -= 1
    count += 1

while count >= (size + (size-1))//2 and count < size + (size-1):
    middle = letters[char] * f
    print(left+middle+right)
    left = left[:-1]
    right = right[1:]
    f += 2
    char += 1
    count += 1