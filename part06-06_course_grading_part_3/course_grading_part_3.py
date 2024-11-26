# tee ratkaisu tänne
def main():
    student = input("Student information: ")
    exercise = input("Exercises completed: ")
    exam = input("Exam points: ")
    
    name = {}
    with open(student) as file:
        for line in file:
            part = line.split(";")
            if part[0] == "id":
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
    completed = {}
    for id, item in exercise_total.items():
        if id in exam_total:
            ep_ep[id] = (int((item*10)/40)) + exam_total[id]
            completed[id] = (int((item*10)/40))
    print(completed)
    
    grade = {}
    for id, item in ep_ep.items():
        a = 0
        limits = [15, 18, 21, 24, 28]
        while a < 5 and item >= limits[a]:
            a += 1
        grade[id] = a

    s_name = "name"
    exec_nbr = "exec_nbr"
    exec_pts = "exec_pts."
    exm_pts = "exm_pts."
    tot_pts = "tot_pts."
    s_grade = "grade"
    #cant' do the :30 space without ^
    print(f"{s_name:30}{exec_nbr:10}{exec_pts:10}{exm_pts:10}{tot_pts:10}{s_grade:10}")
    
    for id, name in name.items():
        if id in exercise_total and id in completed and id in exam_total and id in ep_ep and id in grade:
            print(f"{name:30}{exercise_total[id]:<10}{completed[id]:<10}{exam_total[id]:<10}{ep_ep[id]:<10}{grade[id]:<10}")

main()