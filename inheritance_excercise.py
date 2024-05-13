class Person:
    def __init__(self, name, age, cid_number):
        self.name = name
        self.age = age
        self.cid_no = cid_number
    
    def walk(self):
        print(self.name, "walks.")

    def talk(self):
        print(self.name, "talks")

    def eat(self):
        print(self.name, "eats")
    
    def sleep(self):
        print(self.name, "sleeps")

class Student(Person):
    def __init__(self,name, age,cid_number, student_id, course, year, gpa):
        super().__init__(name, age,cid_number)
        self.student_id = student_id
        self.course = course
        self.year = year
        self.gpa = gpa
    
    def study(self):
        print(self.name, "do study")

    def attend_class(self):
        print(self.name, "do attend class")
    def write_exam(self):
        print(self.name, "writes exam")
    
class Teacher(Person):
    def __init__(self,name, age,cid_number, subject, salary, departement, designation):
        super().__init__(name, age,cid_number)
        self.subject = subject
        self.salary = salary
        self.department = departement
        self.designation = designation

    def teach(self):
        print(self.name, "do teach students.")

    def grade_students(self):
        print(self.name, "grades student")

    def attend_meeting(self):
        print(self.name, "attend meeting")

p1 = Student("Ugyen", 30, 10101010, 2230116,"ECE", 1, 99.5)
p2 = Teacher("Lendup", 50, 10101011, "CSF101", "100,000", "Software Enginer", "IT")

p1.attend_class()
p2.grade_students()





