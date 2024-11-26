def user_input():
    list=[]
    data = input("Exam points and exercises completed: ")
    while data != "":
        for i in data.split():
            list.append(int(i))
        data = input("Exam points and exercises completed: ")
    return list

def exam_point_and_exercise_complete(list: list):
    i = 0
    tot_point_list = []
    tot_point_list_grade = []
    while i < len(list):
        list[i+1] = list[i+1] // 10
        check = list[i] + list[i+1]
        tot_point_list.append(check)
        if list[i] < 10:
            tot_point_list_grade.append(0)
            i += 2
            continue
        tot_point_list_grade.append(check)
        i += 2
    return tot_point_list, tot_point_list_grade

def grade(list: list):
    grade_list = []
    for i in list:
        if i <= 14:
            grade_list.append(0)
        elif i <= 17 and i >= 15:
            grade_list.append(1)
        elif i <= 20 and i >= 18:
            grade_list.append(2)
        elif i <= 23 and i >= 21:
            grade_list.append(3)
        elif i <= 27 and i >= 24:
            grade_list.append(4)
        elif i <= 30 and i >= 28:
            grade_list.append(5)
    return grade_list

def display(t_p_list: list, g_list: list):
    print("Statistics:")
    print(f"Points average: {sum(t_p_list)/len(t_p_list)}")
    x = g_list.count(0)
    print(f"Pass percentage: {(((len(g_list) - x) * 100)/(len(g_list))):.1f}")
    g_list.sort()
    print("Grade distribution:")
    for i in range(5,-1,-1):
        print("  " + str(i) +": " + "*" * g_list.count(i))
   
def main():
    input = user_input()
    pts, pts_grade = exam_point_and_exercise_complete(input)
    grd = grade(pts_grade)
    display(pts, grd)

main()