# HomeWork about classes in Python by Igor Golovin

# Get average of a list
def AverageLst(lst):
    if len(lst) != 0:
        return sum(lst) / len(lst)
    else:
        return f"List is empty"

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.averageGrades = []

    def rate_hw(self, lecturer, course, grade):
        if (isinstance(lecturer, Lecturer) and course in
                lecturer.courses_attached
                and course in self.courses_in_progress):
            if course in lecturer.grades:
                lecturer.grades[course] += [int(grade)]
            else:
                lecturer.grades[course] = [int(grade)]
        else:
           print("Error.. Somthing went wrong: check input data")
           return False

    def average_grades(self):
        for grade in self.grades:
            avr = AverageLst(self.grades[grade])
            # Now 1st element of each list is average value of this list
            # self.grades[grade].insert(0,avr)
            # Or we can create a new list to store average values of all lists
            self.averageGrades.append(avr)
        res = AverageLst(self.averageGrades)
        return res

    def __str__(self):
        newLine = '\n'
        res = (f"Имя: {self.name} {newLine}Фамилия: {self.surname}{newLine}"
               f"Средняя оценка за домашние задания: "
               f"{self.average_grades()}{newLine}Курсы в процессе изучения: "
               f"{', '.join(self.courses_in_progress)}{newLine}"
               f"Завершённые курсы: {','.join(self.finished_courses)}")
        return res

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Not a Student!')
            return
        return self.average_grades() < other.average_grades()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if (isinstance(student, Student) and course in self.courses_attached
                and course in student.courses_in_progress):
            if course in student.grades:
                student.grades[course] += [int(grade)]
            else:
                student.grades[course] = [int(grade)]
        else:
           print(f"Error: {str(self.name)} doesn't have such course -"
                 f" {str(course)}")
           return False
    def __str__(self):
        newLine = '\n'
        res = f"Имя: {self.name} {newLine}Фамилия: {self.surname}"
        return res

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.averageGrades = []

    def average_grades(self):
        for grade in self.grades:
            avr = AverageLst(self.grades[grade])
            # Now 1st element of each list is average value of this list
            # self.grades[grade].insert(0,avr)
            # Or we can create a new list to store average values of all lists
            self.averageGrades.append(avr)
        res = AverageLst(self.averageGrades)
        return res

    def __str__(self):
        newLine = '\n'
        res = (f"Имя: {self.name} {newLine}Фамилия: {self.surname}"
               f"{newLine}Средняя оценка за лекции: {self.average_grades()}")
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Not a Lecturer!')
            return
        return self.average_grades() < other.average_grades()

def AverageHWstudents(studentsLst, CourseName):
    AVRlst = []
    for student in studentsLst:
        if isinstance(student, Student):
            if CourseName in student.courses_in_progress:
               AVRlst.append(student.average_grades())
            else:
                print("Error. Student has not such course")
        else:
            print("Error. Object is not a student")
    res = AverageLst(AVRlst)
#    return res
    return print(f"Средний бал за ДЗ по курсу {CourseName}: "
                 f"{res}")

def AverageGradeLecturers(lectureresLst, CourseName):
    AVRlst = []
    for lecturer in lectureresLst:
        if isinstance(lecturer, Lecturer):
            if CourseName in lecturer.courses_attached:
               AVRlst.append(lecturer.average_grades())
            else:
                print("Error. Lecturer has not such course")
        else:
            print("Error. Object is not a lecturer")
    res = AverageLst(AVRlst)
#    return res
    return print(f"Средний бал за лекции по курсу {CourseName}: "
                 f"{res}")


print("Let's start")
print()
student1 = Student("Rodion","Meglin","unknown")
student1.courses_in_progress = ["JavaScript","Git","HTML","Python"]
student1.finished_courses = ["Введение в программирование"]
student2 = Student("Crazy","Men","unknown")
student2.courses_in_progress = ["JavaScript","Git","HTML","Python"]
student2.finished_courses = ["Основы Linux"]
reviewer1 = Reviewer("Eseniya", "Steklova")
reviewer1.courses_attached = ["JavaScript","Git","HTML","Python"]
reviewer2 = Reviewer("Vera", "Steklova")
reviewer2.courses_attached = ["JavaScript","HTML","Git","Python"]

lecturer1 = Lecturer("Andrej", "Bykov")
lecturer1.courses_attached = ["Git","Python"]
lecturer2 = Lecturer("mustache", "Men")
lecturer2.courses_attached = ["JavaScript","Git","HTML","Python"]

reviewer1.rate_hw(student1, "Git", 10)
reviewer1.rate_hw(student1, "Git", 10)
reviewer1.rate_hw(student1, "Python", 8)
reviewer1.rate_hw(student1, "Python", 9)
reviewer2.rate_hw(student2, "JavaScript", 5)
reviewer2.rate_hw(student2, "JavaScript", 5)
reviewer2.rate_hw(student2, "HTML", 3)
reviewer2.rate_hw(student2, "HTML", 4)
student1.rate_hw(lecturer1, "Git", 5)
student1.rate_hw(lecturer1, "Git", 3)
student1.rate_hw(lecturer1, "Python", 10)
student1.rate_hw(lecturer1, "Python", 9)
student2.rate_hw(lecturer2, "JavaScript", 2)
student2.rate_hw(lecturer2, "JavaScript", 3)
student2.rate_hw(lecturer2, "HTML", 4)
student2.rate_hw(lecturer2, "HTML", 6)

print(reviewer1)
print()
print(lecturer1)
print()
print(student1)
print()
print(reviewer2)
print()
print(lecturer2)
print()
print(student2)
print()

if student1 > student2:
    print(f"{student1.name} имеет средний бал за ДЗ выше, чем {student2.name}")
else:
    print(f"{student2.name} имеет средний бал за ДЗ выше, чем {student1.name}")

if lecturer1 > lecturer2:
    print(f"{lecturer1.name} имеет средний бал за лекции выше, "
          f"чем {lecturer2.name}")
else:
    print(f"{lecturer2.name} имеет средний бал за лекции выше, "
          f"чем {lecturer1.name}")

StudentList = [student1, student2]
LecturerList = [lecturer1, lecturer2]
print()
AverageHWstudents(StudentList, "Git")
print()
AverageGradeLecturers(LecturerList,"Git")