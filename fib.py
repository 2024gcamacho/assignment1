import time
from functools import lru_cache

def timer(func):
    #wrapper replaces any function timer decorates
    def wrapper(*args, **kwargs):
        #start time of function execution
        start = time.perf_counter()
        #calls original function with its arguments and stores in res
        res = func(*args, **kwargs)
        #end time of function execution
        end = time.perf_counter()
        #calcuates time taken to execute function
        finished = end - start
        #shows how long it took to exceute 
        print(f"Finished in {finished:.8f}s: {func.__name__}({args[0]}) -> {res}")
        return res
    return wrapper

@lru_cache #using correctly?
#runs each time fib is run, timing execution
@timer 
#series of numbers where each number is the sum of the two preceding ones, starting with 0 and 1
def fib(n: int) -> int:
        #base cases for recusion
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        #otherwise - function calls itself twice, subtrating 1 and 2 then adding together to return sum
        else:
            return fib(n - 1) + fib(n - 2)

if __name__ == "__main__":
    fib(100) 
        


