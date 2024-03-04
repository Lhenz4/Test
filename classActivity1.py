 

name = input("Your Name: ")
num1 = float(input("Enter your first number: ")) 
num2 = float(input("Enter your second number(Your second number can\'t be zero): "))

addition_result = num1 + num2
subtraction_result = num1 - num2
multiplication_result = num1*num2
division_result = num1 / num2



print (f"""
Hello {name}. Following are your calculations:

Addition Result: {num1} + {num2} = {addition_result}

Subtraction Result: {num1} - {num2} = {subtraction_result}

Multiplication Result: {num1} x {num2} ={multiplication_result}

Division Result: {num1} / {num2} = {division_result}

Thank You. Hoping to see you next time
""")
