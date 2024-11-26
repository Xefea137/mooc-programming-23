# Write your solution here
def add_student(students: dict, name: str):
    students[name] = "no completed courses"

def print_student(students: dict, name: str):
    if name in students:
        print(f"{name}: ")
        if students[name] != "no completed courses":
            details = students[name]
            print(f" {len(students[name])//2:.0f} completed courses:")
            x = 1
            avg = 0
            for item in details:
                if x % 2 == 1:
                    print(f"  {item}", end="")
                    x += 1
                else:
                    print(f" {item}")
                    x += 1
                    avg += item
            print(f" average grade {avg/((x-1)/2):.1f}")
        else:
            print(" no completed courses")
    else:
        print(f"{name}: no such person in the database")

def add_course(students: dict, name: str, course_name_grade: tuple):
    if course_name_grade[1] == 0:
        return

    if students[name] == "no completed courses":
        students[name] = []

    if name in students:
        if course_name_grade[0] in students[name]:
            new_list = students[name]
            for item in range(0,len(new_list)):
                if new_list[item] == course_name_grade[0] and new_list[item+1] < course_name_grade[1]:
                    new_list[1] = course_name_grade[1]
        else:
            students[name].append(course_name_grade[0])
            students[name].append(course_name_grade[1])
    else:
        print(f"{name}: no such person in the database")

def summary(students: dict):
    print(f"students {len(students)}")
    most = 0
    current_average = 0

    for name in students: 
        if len(students[name]) > most:
            most = len(students[name])
            student_name = name
        total = 0
        x = 1
        details = students[name]
        for item in details:
            if x % 2 == 0:
                total += item
            x += 1
        average = total / ((x-1)/2)
        if current_average < average:
            current_average = average
            current_name = name
    print(f"most courses completed {most/2:.0f} {student_name}")
    print(f"best average grade {current_average:.1f} {current_name}")

if __name__ == "__main__":
    students = {}
    #add_student(students, "Peter")
    #add_student(students, "Eliza")
    #print_student(students, "Peter")
    #print_student(students, "Eliza")
    #print_student(students, "Jack")

    #add_student(students, "Peter")
    #add_course(students, "Peter", ("Introduction to Programming", 3))
    #add_course(students, "Peter", ("Advanced Course in Programming", 2))
    #print_student(students, "Peter")

    #add_student(students, "Peter")
    #add_course(students, "Peter", ("Introduction to Programming", 3))
    #add_course(students, "Peter", ("Advanced Course in Programming", 2))
    #add_course(students, "Peter", ("Data Structures and Algorithms", 0))
    #add_course(students, "Peter", ("Introduction to Programming", 2))
    #print_student(students, "Peter")

    #add_student(students, "Peter")
    #add_student(students, "Eliza")
    #add_course(students, "Peter", ("Data Structures and Algorithms", 1))
    #add_course(students, "Peter", ("Introduction to Programming", 1))
    #add_course(students, "Peter", ("Advanced Course in Programming", 1))
    #add_course(students, "Eliza", ("Introduction to Programming", 5))
    #add_course(students, "Eliza", ("Introduction to Computer Science", 4))
    #summary(students)

    #add_student(students, "Emily")
    #add_student(students, "Peter")
    #add_course(students, "Emily", ("Software Development Methods", 4))
    #add_course(students, "Emily", ("Software Development Methods", 5))
    #add_course(students, "Peter", ("Data Structures and Algorithms", 3))
    #add_course(students, "Peter", ("Models of Computation", 0))
    #add_course(students, "Peter", ("Data Structures and Algorithms", 2))
    #add_course(students, "Peter", ("Introduction to Computer Science", 1))
    #print_student(students, "Emily")
    #print_student(students, "Peter")

    add_student(students, "Emily")
    add_student(students, "Peter")
    add_course(students, "Emily", ("Software Development Methods", 4))
    add_course(students, "Emily", ("Software Development Methods", 5))
    add_course(students, "Peter", ("Data Structures and Algorithms", 3))
    add_course(students, "Peter", ("Models of Computation", 0))
    add_course(students, "Peter", ("Data Structures and Algorithms", 2))
    add_course(students, "Peter", ("Introduction to Computer Science", 1))
    add_course(students, "Peter", ("Software Engineering", 3))
    summary(students)