#All we need to know about lists
# A list is a collection of items that can be of different types    
# Lists are mutable, meaning you can change their content
# Lists can contain duplicates
# Lists can be nested, meaning you can have lists within lists
# Lists can be created using square brackets []
# Lists can be created using the list() constructor
name = "Smith", "John", "Doe", "Jane"
print(list(name))
cart = []
cart.append("Laptop")
cart.append("hard disk")
cart.append("mouse")    
cart.append("keyboard")
cart.append("monitor")
cart.append("printer")
print(f"your cart contains: {cart}")
cart.remove("printer")  
print(f"your cart contains: {cart}")
cart.append("printer")
print(f"your cart contains: {cart}")
cart.pop(0)
print(f"your cart contains: {cart}")


book = ["1984", "Brave New World", "Fahrenheit 451"]
book.append("Animal Farm")
book.insert(0, "The Giver")
book.remove("1984")
print(f"The Number of books are: {len(book)}")
print(book)

# looping through a list
# A list of favorite foods
foods = ["pizza", "burger", "pasta", "salad", "sushi"]
# Using a for loop to iterate through the list
for food in foods:
    print(f"I love {food}!")

  #list comprehension
  # What is list comprehension?
  # List comprehension is a concise way to create lists in Python.
  # It allows you to generate a new list by applying an expression to each item in an existing iterable (like a list or range).
  # List comprehension syntax:  
  # new_list = [expression for  item in iterable if condition]  
# Example: Create a list of squares of even numbers from 0 to 9
squares = [x**2 for x in range(10) if x % 2 == 0]

movies = [
    "Avatar",
    "Inception",
    "Avengers",
    "Titanic",
    "The Matrix",
    "Alien",
    "Gladiator",
    "A Quiet Place",
    "Interstellar",
    "Aladdin"
]
# Using list comprehension to filter movies that start with 'A' 
movies_starting_with_a = [movie for movie in movies if movie.startswith("A")]
print(f"Movies starting with 'A': {movies_starting_with_a}")

# Looping through a list of scores to produce a new list of grades that are higher than 60

scores = [45, 82, 67, 90, 33, 76, 50]
passing_scores = [score for score in scores if score > 60]
print(f"Passing scores: {passing_scores}")

names = ["alice", "BOB", "Charlie", "daVid"]
new_names = [name.capitalize() for name in names ]
print(f"Capitalized names: {new_names}")

prices = [100, 250, 85]
# Using list comprehension to apply a tax of 16% to each price
taxed_prices = [price *1.16 for price in prices]
print(f"Prices with tax: {taxed_prices}")