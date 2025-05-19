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