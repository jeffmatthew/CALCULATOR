def add(num1, num2):
    return num1 +num2

def subtract(num1,num2):
    return num1-num2

def multiply(num1,num2):
    return num1*num2

def divide(num1,num2):
    return num1/num2

cond = "y"
while cond == "y":
    choice = eval((input("Enter choice: ")))
    num1 = eval(input("Enter first number:"))
    num2 = eval(input("Enter second number:"))
    if choice == 1:
        add(num1,num2)
        print(add(num1,num2))
    elif choice == 2:
        subtract(num1,num2)
        print(subtract(num1,num2))
    elif choice == 3:
        multiply(num1,num2)
        print(multiply(num1,num2))
    elif choice == 4:
        divide(num1,num2)
        print(divide(num1,num2))
    else:
        print("you can only put a number from 1 to 4")
    cond = input("would you like to use the program again? y/n")