num_students = int(input("enter the number of student: "))

i = 1
while i <= num_students:
    total_grade = 0
    num_subject = int(input(f"Enter the number of subjeects for student {i}: "))

    for j in range (1, num_subject+1):
        grade = float(input(f"Enter the subject {j} grade of student {i}: "))
        total_grade += grade

    average_grade = total_grade / num_subject
    print(f"Average grade for studeent {i}: {average_grade:.2f}")
    i += 1