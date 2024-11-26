# Write your solution here
pin = 4321
attempt = 0
while True:
    pin1 = int(input("PIN"))
    attempt += 1
    if pin1 == pin:
        break
    print("Wrong")

if attempt == 1:
    print("Correct! It only took you one single attempt!")
else:
    print(f"Correct! It took you {attempt} attempts")