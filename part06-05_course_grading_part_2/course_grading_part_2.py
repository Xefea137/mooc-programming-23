# wwite your solution here
def main():
    student = input("Student information: ")
    exercise = input("Exercises completed: ")
    exam = input("Exam points: ")

    name = {}
    with open(student) as file:
        for line in file:
            part = line.split(";")
            if part [0] == "id":
                continue
            name[part[0]] = f"{part[1]} {part[2].strip()}"

    exercise_total = {}
    with open(exercise) as file:
        for line in file:
            part = line.split(";")
            if part[0] == "id":
                continue
            sum = 0
            for item in part[1:]:
                sum += int(item)
            exercise_total[part[0]] = sum

    exam_total = {}
    with open(exam) as file:
        for line in file:
            part = line.split(";")
            if part[0] == "id":
                continue
            total = 0
            for item in part[1:]:
                total += int(item)
            exam_total[part[0]] = total

    ep_ep = {}
    for id, item in exercise_total.items():
        if id in exam_total:
            ep_ep[id] = (int((item*10)/40)) + exam_total[id]

    grade = {}
    for id, item in ep_ep.items():
        a = 0
        limits = [15, 18, 21, 24, 28]
        while a < 5 and item >= limits[a]:
            a += 1
        grade[id] = a

    '''
    grade = {}
    for id, item in ep_ep.items():
        if item >= 0 and item <= 14:
            grade[id] = 0
        elif item >= 15 and item <= 17:
            grade[id] = 1
        elif item >= 18 and item <= 20:
            grade[id] = 2
        elif item >= 21 and item <= 23:
            grade[id] = 3
        elif item >= 24 and item <= 27:
            grade[id] = 4
        elif item >= 28:
            grade[id] = 5
    '''

    for id, name in name.items():
        if id in grade:
            print(f"{name} {grade[id]}")

main()