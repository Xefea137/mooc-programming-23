# Write your solution here
import fractions 
def fractionate(amount: int):
    l = []
    for item in range(amount):
        l.append(fractions.Fraction(1,amount))
    return l

if __name__ == "__main__":
    print(fractionate(5))