# Variable Declaration and Printing
# This code declares three variables: name, age, and is_student
name = "Smith"
age = 37
is_student = True

print(f"Name: {name}, Age: {age}, Is Student: {is_student}")

#  all about strings and string methods
# String Declaration
greeting = "Hello, World!"
print(f"Greeting: {greeting}")
# String Length
greeting_length = len(greeting)
print(f"Length of greeting: {greeting_length}")
# String Slicing
first_five_chars = greeting[:5]
print(f"First five characters: {first_five_chars}") 
# String Concatenation
greeting2 = " How are you?"
full_greeting = greeting + greeting2
# String Formatting
formatted_greeting = f"{greeting} {greeting2}"
print(f"Formatted Greeting: {formatted_greeting}")
# String Methods
upper_greeting = greeting.upper()   
lower_greeting = greeting.lower()
print(f"Uppercase: {upper_greeting}, Lowercase: {lower_greeting}")
# String Replacement
replaced_greeting = greeting.replace("World", "Python")
print(f"Replaced Greeting: {replaced_greeting}")
# String Split
split_greeting = greeting.split(", ")
print(f"Split Greeting: {split_greeting}")
# String Join
joined_greeting = " ".join(split_greeting)
print(f"Joined Greeting: {joined_greeting}")
# String Count
count_greeting = greeting.count("o")    
print(f"Count of 'o': {count_greeting}")
# String Find
find_greeting = greeting.find("World")
print(f"Index of 'World': {find_greeting}")
# String Strip
strip_greeting = greeting.strip("!")    
print(f"Stripped Greeting: {strip_greeting}")
# String Check
is_alpha = greeting.isalpha()
print(f"Is Alpha: {is_alpha}")
# String Check
is_digit = greeting.isdigit()
print(f"Is Digit: {is_digit}")
# String Check
is_alnum = greeting.isalnum()
print(f"Is Alphanumeric: {is_alnum}")

#Using dir() to list all attributes and methods of a string
print("String Methods and Attributes: ", dir(greeting))
#Using help() to get documentation on a specific string method  
print(help(greeting.upper))
