# Tuples
# Tuples are immutable sequences, typically used to store collections of heterogeneous data.
# Tuples are defined by enclosing the elements in parentheses (()).
# Tuples can contain any type of data, including other tuples, lists, and dictionaries.
# Tuples can be nested, meaning you can have tuples within tuples.
car = ("Toyota","Corolla",2020)
print(car[0])
print(car[1])
print(car[2])

# looping through a tuple
for item in car:
    print(item)

# enumerate function
for index, item in enumerate(car):
    print(f"Index: {index}, Item: {item}")

# Tuple unpacking
car = ("Toyota","Corolla",2020)
brand, model, year = car
print(brand)

#looping through a tuple
for brand, model, year in [car]:
    print(f"Brand: {brand}, Model: {model}, Year: {year}")

student = ("John", "Doe", "grade 10",)
first_name, last_name, grade = student
for first_name, last_name, grade in [student]:
    print(f"First Name: {first_name}, Last Name: {last_name}, Grade: {grade}")

podium = ("Alice", "Bob", "Charlie")
first_place, second_place, third_place = podium
print(f"First Place: {first_place})")
print(f"Second Place: {second_place})")
print(f"Third Place: {third_place})")