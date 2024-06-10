# Write your solution here
import urllib.request, json
def retrieve_all():
    total = 0
    list_enable = []
    my_request = urllib.request.urlopen("https://studies.cs.helsinki.fi/stats-mock/api/courses")
    data = my_request.read()
    course = json.loads(data)

    for items in course:
        if items['enabled'] == True:
            for value in items['exercises']:
                total += value
            list_enable.append((items['fullName'], items['name'], items['year'], total))
            total = 0
    return list_enable

def retrieve_course(course_name: str):
    d = {}
    weeks = 0
    students = 0
    hours = 0
    exercises = 0
    url = f"https://studies.cs.helsinki.fi/stats-mock/api/courses/{course_name}/stats"
    my_request = urllib.request.urlopen(url)
    data = my_request.read()
    course = json.loads(data)
    
    for week, data in course.items():
        weeks += 1
        if students < data["students"]:
            students = data['students']
        hours += data['hour_total']
        hours_average = hours//students
        exercises += data['exercise_total']
        exercises_average = exercises//students

    d = {'weeks' : weeks, 'students' : students, 'hours' : hours, 'hours_average': hours_average, 'exercises' : exercises, 'exercises_average' : exercises_average}
    return d

if __name__ == "__main__":
    print(retrieve_all())
    print(retrieve_course("docker2019"))