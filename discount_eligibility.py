age = int(input("Your Age: "))
student = input("Are You Student?(Yes/No): ")

if (age >= 12 and (age >= 13 or age <= 18 and student == "yes")):
    print("You are eigible for the discount")

else:
    print("Sorry,you are not eligible for the discount")