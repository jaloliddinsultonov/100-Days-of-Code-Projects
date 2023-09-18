import time
current_time = time.time()
print(current_time)

def speed_calc_decorator(function):
    def calculator():
        start_time = time.time()
        function()
        time_after_run = time.time()
        print(time_after_run - start_time)
    return calculator

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