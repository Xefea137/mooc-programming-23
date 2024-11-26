# tee ratkaisu tänne
def main():
    student = input("Student information: ")
    exercise = input("Exercises completed: ")
    exam = input("Exam points: ")
    course = input("Course information: ")

    with open(student) as s_file, open(exercise) as e_file, open(exam) as exam_file, open("results.txt", "w") as rtxt_file, open("results.csv", "w") as rcsv_file, open(course) as c_file:
    
        name = {}
        for line in s_file:
            part = line.split(";")
            if part[0] == "id":
                continue
            name[part[0]] = f"{part[1]} {part[2].strip()}"

        exercise_total = {}
        for line in e_file:
            part = line.split(";")
            if part[0] == "id":
                continue
            sum = 0
            for item in part[1:]:
                sum += int(item)
            exercise_total[part[0]] = sum

        exam_total = {}
        for line in exam_file:
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

        x = []
        for line in c_file:
            part = line.split(":")
            x.append(part[1].strip())
        z = f"{x[0]}, {x[1]} credits\n"
        rtxt_file.write(z)
        rtxt_file.write("=" * (len(z)-1))
        rtxt_file.write(f"\n{s_name:30}{exec_nbr:10}{exec_pts:10}{exm_pts:10}{tot_pts:10}{s_grade:10}\n")
        for id, name in name.items():
            if id in exercise_total and id in completed and id in exam_total and id in ep_ep and id in grade:
                rtxt_file.write(f"{name:30}{exercise_total[id]:<10}{completed[id]:<10}{exam_total[id]:<10}{ep_ep[id]:<10}{grade[id]:<10}\n")
                rcsv_file.write(f"{id};{name};{grade[id]}\n")

    print("Results written to files results.txt and results.csv")

main()