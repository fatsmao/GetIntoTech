#Calculator
#1. Ask user for a number
#2. Ask user for an operator (+, - ,* or / should be supported)
#3. Ask user for a second number
#4. Print out the result.

#As an extra extra extra challenge, make the calculator loop until the user doesn't want to use it anymore (i.e. before asking for numbers and operator, ask if the user wants to stop, maybe press q to quit?).

#Don't hesitate to reach out if you have any questions.

'''''''''
while True:
    num1 = float(input("Please enter a number: "))
    operator = input("Please choose one of the following operators: +, -, *, /")
    num2 = float(input("Please enter a second number"))
    if operator == '+':
        print(num1 + num2)
    elif operator == '-':
        print(num1 - num2)
    elif operator == '*':
        print(num1 * num2)
    elif operator == '/':
        print(num1 / num2)
    else:
        print("You have selected an incorrect operator. Please try again")
'''''''''