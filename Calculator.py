def caculator():

    print("This is a calculator!")

    def addition(num1,num2):
        result = num1 + num2
        print(result)

    def subtraction(num1,num2):
        result = num1 - num2
        print(result)

    def multiplication(num1,num2):
        result = num1 * num2
        print(result)

    def division(num1 , num2):
        result = num1 / num2
        print(result)

    num1 = int(input("Enter number 1: "))
    num2 = int(input("Enter number 2: "))

    print("Press 1 for Addition")
    print("press 2 for Subtraction")
    print("Press 3 for Multiplication")
    print("Press 4 for Division")

    operation = int(input("Enter number: "))

    if operation == 1:
        addition(num1,num2)
    elif operation == 2:
        subtraction(num1,num2)
    elif operation == 3:
        multiplication(num1,num2)
    elif operation == 4:
        division(num1 , num2)
    else:
        print("Wrong Operation number")

keep_running = 1
caculator()

while keep_running == 1:
    print("Press 1 if you want to keep the program running")
    print("Press 2 if you want to close the program")
    ask = int(input("Do you want to keep the program running? "))
    if ask == 2:
        print("Thanks for using the caculator")
        keep_running = 2
    if ask == 1:    
        caculator()