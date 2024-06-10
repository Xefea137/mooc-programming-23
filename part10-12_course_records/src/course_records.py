# tee ratkaisusi tänne
class Course:
    def __init__(self, course_name: str):
        self.__course_name = course_name
        self.__grade = 0
        self.__credits = 0

    def name(self):
        return self.__course_name

    def grade(self):
        return self.__grade

    def credits(self):
        return self.__credits

    def add_detail(self, grade: int, credits: int):
        if self.__grade < grade:
            self.__grade = grade
        self.__credits = credits
        
class CourseRecords:
    def __init__(self):
        self.__course = {}

    def add_course(self, course_name: str, grade: int, credits: int):
        if not course_name in self.__course:
            self.__course[course_name] = Course(course_name)
        self.__course[course_name].add_detail(grade, credits)

    def course_detail(self, course_name: str):
        if not course_name in self.__course:
            return None
        return self.__course[course_name]

    def stats(self):
        return self.__course

class CourseApplication:
    def __init__(self):
        self.__course = CourseRecords()

    def help(self):
        print("1 add course")
        print("2 get course data")
        print("3 statistics")
        print("0 exit")

    def add_course(self):
        course_name = input("course: ")
        grade = int(input("grade: "))
        credits = int(input("credits: "))
        self.__course.add_course(course_name, grade, credits)

    def get_course_data(self):
        course_name = input("course: ")
        data = self.__course.course_detail(course_name)
        if data == None:
            print("no entry for this course")
            return
        print(f"{course_name} ({data.credits()} cr) grade {data.grade()}")

    def statistics(self):
        total_credits = 0
        total_grade = 0
        grade = []
        all_details = self.__course.stats()
        for key, item in all_details.items():
            total_credits += item.credits()
            total_grade += item.grade()
            grade.append(item.grade())
        
        print(f"{len(all_details)} completed courses, a total of {total_credits} credits")
        print(f"mean {(total_grade/len(all_details)):.1f}")
        print("grade distribution")
        print(f"5: {'x' * grade.count(5)}")
        print(f"4: {'x' * grade.count(4)}")
        print(f"3: {'x' * grade.count(3)}")
        print(f"2: {'x' * grade.count(2)}")
        print(f"1: {'x' * grade.count(1)}")

    def execute(self):
        self.help()
        while True:
            print()
            command = input("command: ")
            if command == "0":
                break
            elif command == "1":
                self.add_course()
            elif command == "2":
                self.get_course_data()
            elif command == "3":
                self.statistics()

c = CourseApplication()
c.execute()