print ("-----------------------------------------------------------------------------------------------------------------")
print ("Newton\'s Second Law".center(120))
print("------------------------------------------------------------------------------------------------------------------")

print ("""
    Select the missing value
    1. Mass(m)
    2. Accleration(a)
    3. Force(F)
         
""")
missing_value_choice = input("Enter the option number for the missing value:")
print()

if missing_value_choice == "1":
    F = float(input("Force(F): "))
    a = float(input("Acceleration(a): "))
    m = F/a
    print (f"Mass (m) = {m}")

elif missing_value_choice == "2":
    F = float(input("Force(F): "))
    m = float(input("Massma): "))
    a = F/m
    print (f"Accleration (a) = {a}")

elif missing_value_choice == "1":
    m = float(input("Mass(m): "))
    a = float(input("Acceleration(a): "))
    F = m * a
    print (f"Force (F) = {F}")

else:
    print ("Invalid input. Try Again")


print ("""
---------------------------------------------------------------------------------------------------------------------
                                                Thank You
---------------------------------------------------------------------------------------------------------------------
""")