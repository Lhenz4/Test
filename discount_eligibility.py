
def eligibility_test():

    age = int(input("Your Age: "))
    student = input("Are You Student?(Yes/No): ")

    if (age <= 12 or ((age >= 13 or age <= 18) and student == "yes")):
        print("You are eigible for the discount on the movie ticket")

    else:
        print("Sorry, you are not eligible for the discount")

eligibility_test()