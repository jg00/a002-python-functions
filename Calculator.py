first_number = int(input("Enter first number: "))
operator = input("Enter operand (+, -, *, /): ")
second_number = int(input("Enter second number: "))


def calculate(first_number, operator, second_number):
    if (operator == "*"):
        return multiply(first_number, second_number)
    elif (operator == "/"):
        return divide(first_number, second_number)
    elif (operator == "+"):
        return add(first_number, second_number)
    elif (operator == "-"):
        return subtract(first_number, second_number)


def multiply(first_number, second_number):
    return first_number * second_number

def divide(first_number, second_number):
    if (second_number == 0):
        return
    return first_number / second_number

def add(first_number, second_number):
    return first_number + second_number

def subtract(first_number, second_number):
    return first_number - second_number


result = calculate(first_number, operator, second_number)
print(result)
