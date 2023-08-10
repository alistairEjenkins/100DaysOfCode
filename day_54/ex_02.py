# functions inputs/functionality/output
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

# functions are first class objects, can be passed around as arguments

def calculate(calc_func, n1, n2):
    return calc_func(n1,n2)

result = calculate(multiply, 2, 3)
print(result)

# nested functions

def outer_function():
    print("I'm outer")

    def nested_function():
        print("I'm inner")

    nested_function()

outer_function()

# functions can be returned from other functions
def outer_function2():
    print("I'm outer")

    def nested_function():
        print("I'm inner")

    return nested_function

inner_function = outer_function2()
inner_function()


