def fizz_buzz(n):
    """
    Returns 'Fizz' if n is divisible by 3, 'Buzz' if n is divisible by 5,
    and 'FizzBuzz' if n is divisible by both 3 and 5. Otherwise, returns n.
    """
    if n % 3 == 0 and n % 5 == 0:
        return "FizzBuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    else:
        return n
    
print(fizz_buzz(6))  # Output: FizzBuzz    
print(fizz_buzz(10))  # Output: Buzz
print(fizz_buzz(7))  # Output: 7
print(fizz_buzz(15))  # Output: Fizz

# keyword arguments
# What are keyword arguments?
# Keyword arguments are a way to pass arguments to a function by explicitly specifying the name of the parameter and its value.
# This allows you to pass arguments in any order and makes the code more readable.
# For example, consider the following function:
def greet(name, age):
    print(f"Hello, {name}! You are {age} years old.")

# You can call this function using positional arguments:
greet("Alice", 30)  # Output: Hello, Alice! You are 30 years old.

# Default arguments
# What are default arguments?   
# Default arguments are values that are assigned to parameters in a function definition. If the caller does not provide a value for that parameter, the default value is used.
# For example, consider the following function: 
def greet(name, age=25):
    print(f"Hello, {name}! You are {age} years old.")

# You can call this function with or without the age argument:
greet("Alice")  # Output: Hello, Alice! You are 25 years old.
greet("Bob", 30)  # Output: Hello, Bob! You are 30 years old.

# *args 

# What are *args?
# *args is a special syntax in Python that allows you to pass a variable number of arguments to a function. It collects the extra positional arguments as a tuple.

# For example, consider the following function:

def add_numbers(*args):
    total = 0
    for num in args:
        total += num
    return total

# You can call this function with any number of arguments:
print(add_numbers(1, 2, 3))  # Output: 6

 # **kwargs

# What are **kwargs?
# **kwargs is a special syntax in Python that allows you to pass a variable number of keyword arguments to a function. It collects the extra keyword arguments as a dictionary.

# For example, consider the following function:

def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# You can call this function with any number of keyword arguments:
print_info(name="Alice", age=30, city="New York")
# Output:
# name: Alice
# age: 30   
# city: New York
