# Write your solution here
from random import choice
def roll(die: str):
    if die == 'A':
        x = "333336"
    if die == 'B':
        x = "222555"
    if die == 'C':
        x = "144444"
    return int(choice(x))

def play(die1: str, die2: str, times: int):
    d1 = 0
    d2 = 0
    d = 0
    
    for i in range(times):
        x = roll(die1)
        z = roll(die2) 
        if x == z:
            d += 1
        elif x > z:
            d1 += 1
        elif x < z:
            d2 += 1

    return (d1,d2,d)

if __name__ == "__main__":
    for i in range(20):
        print(roll("A"), " ", end="")
    print()
    for i in range(20):
        print(roll("B"), " ", end="")
    print()
    for i in range(20):
        print(roll("C"), " ", end="")

    result = play("A", "C", 10)
    print(result)
    result = play("B", "B", 1000)
    print(result)