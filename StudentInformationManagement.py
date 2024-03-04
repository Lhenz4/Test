
students_list = []
students_dicts = {}

name = input("Your Name: ")
age = int(input("Your age: "))
grade = int(input("Your grade: "))

students_list.append(name)
students_dicts[name] = {"Age":age, "Grade":grade} #{"Pema":{"age":19, "grade":13}}

print("Successfully added student information.")
print(students_dicts.items())

print()

search_student = input("Enter name of the student to search: ")
if search_student in students_list:
    print (f"Student found!\n")
else:
    print("Student not found")

remove_student = input("Enter the name of the student to remove: ")
if remove_student in students_list:
    students_list.remove(remove_student)
    del students_dicts[remove_student]

    print("Remove Successful")
    
else:
    print("student not found.")

