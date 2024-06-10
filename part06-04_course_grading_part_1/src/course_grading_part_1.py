# write your solution here
def main():
    student = input("Student information: ")
    exercise = input("Exercises completed: ")
    
    with open(exercise) as file:
        total = {}
        for line in file:
            part = line.split(";")
            if part[0] == "id":
                continue
            sum = 0
            for item in part[1:]:
                sum += int(item)
            total[part[0]] = sum
    
    with open(student) as file:
        name = {}
        for line in file:
            line = line.replace("\n", "")
            part = line.split(";")
            if part[0] == "id":
                continue
            name[part[0]] = part[1] + " " + part[2]    

    for id, name in name.items():
        if id in total:
            print(f"{name} {total[id]}")

main()