# Write your solution here
value = int(input("Value of gift: "))
if value>=1000000:
    print(f"Amount of tax: {(142100+(value-1000000)*0.17)} euros")
elif value>=200000:
    print(f"Amount of tax: {(22100+(value-200000)*0.15)} euros")
elif value>=55000:
    print(f"Amount of tax: {(4700+(value-55000)*0.12)} euros")
elif value>=25000:
    print(f"Amount of tax: {(1700+(value-25000)*0.10)} euros")
elif value>=5000:
    print(f"Amount of tax: {(100+(value-5000)*0.08)} euros")
else:
    print("No tax!")