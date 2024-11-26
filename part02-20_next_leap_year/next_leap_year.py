# Write your solution here
base_year = int(input("Year: "))
year = base_year + 1
while True:
    if year%4==0 and year%100!=0 or year%400==0 and year%100==0:
        break
    year += 1

print(f"The next leap year after {base_year} is {year}")