# 1. Decorator to ensure all input arguments are non-negative integers
def non_negative_args(func):
    def wrapper(*args, **kwargs):
        if all(isinstance(arg, int) and arg >= 0 for arg in args):
            return func(*args, **kwargs)
        else:
            return "Invalid"
    return wrapper

@non_negative_args
def calculate_square_root(x):
    return x ** 0.5

# 2. Decorator to print function’s name, arguments, and return value
def debug(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"{func.__name__} called with {args}, returned {result}")
        return result
    return wrapper

@debug
def add(a, b):
    return a + b

# 3. Decorator to repeat function execution n times
def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def greet(name):
    print(f"Hello, {name}")

# 4. Decorator to count number of times a function has been called
def count_calls(func):
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        return func(*args, **kwargs)
    wrapper.calls = 0
    return wrapper

@count_calls
def say_hello():
    print("Hello")


#Call the functions here to see output

print(calculate_square_root(9))    
print(calculate_square_root(-9))    

add(5, 7)                            

greet("Sahil")                      

say_hello()
say_hello()
print(f"say_hello was called {say_hello.calls} times")  
