import time

def speed_calc_decorator(function):

    def timer_function():
        current_time = time.time()
        function()
        new_time = time.time()
        print(f"{function.__name__} run speed: {new_time - current_time}")

    return timer_function




@speed_calc_decorator
def fast_function():
    for i in range(10000000):
        i * i

@speed_calc_decorator
def slow_function():
    for i in range(100000000):
        i * i


fast_function()

slow_function()
