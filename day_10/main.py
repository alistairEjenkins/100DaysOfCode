# Calculator

def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operands = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}

answer = 0
new_calc = 'n'
while True:
    if new_calc == 'n':
        num1 = int(input("What is your first number?\n>> "))
    else:
        num1 = answer
        print(f"First number is: {num1}")
    if num1 == 'exit': break
    for operand in operands:
        print(operand)
    operand = input("Pick an operation:\n>> ")
    num2 = int(input("What is your next number?\n>> "))
    answer = operands[operand](num1, num2)
    print(f"{num1} {operand} {num2} = {answer}")
    new_calc = input(f"Type 'y' to continue with {answer}, or type 'n' to start new calculation:\n>> ")