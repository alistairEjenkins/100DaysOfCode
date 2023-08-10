import time
def delay_decorator(function):
    def wrapper_func():
        time.sleep(2)
        function()

    return wrapper_func


@delay_decorator
def say_hello():
    print("hello")

def say_bye():
    print("bye")

def say_greeting():
    print("Howdy!")

say_hello()