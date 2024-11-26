# Write your solution here
def dict_of_numbers():
    d = {}
    single = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teen = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

    for set in range(0,10):
        d[set] = single[set]
        
    c = 0
    for set in range(10, 20):
        d[set] = teen[c]
        c += 1
    
    c = 0
    t = 0
    for set in range(20,100):
        if c == 10:
            t += 1
            c = 0
            d[set] = tens[t]
            c += 1
        elif c == 0:
            d[set] = tens[t]
            c += 1
        else:
            d[set] = f"{tens[t]}-{single[c]}"
            c += 1

    return d

if __name__ == "__main__":
    numbers = dict_of_numbers()
    print(numbers[2])
    print(numbers[11])
    print(numbers[45])
    print(numbers[99])
    print(numbers[0])