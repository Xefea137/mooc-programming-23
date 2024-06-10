# Write your solution here
students = int(input("How many students on the course? "))
size = int((input("Desired group size ")))
group = students/size
if group %2 != 0:
    group += 1

print(f"Number of groups formed: {int(group)}")