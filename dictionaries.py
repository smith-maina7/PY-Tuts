# Lets have a look at dictionaries
# Dictionaries
# Dictionaries are mutable, unordered collections of key-value pairs.
# Dictionaries are defined by enclosing the key-value pairs in curly braces ({}).   
# Dictionaries can contain any type of data, including other dictionaries, lists, and tuples.
# Dictionaries can be nested, meaning you can have dictionaries within dictionaries.    
# Dictionaries are mutable, meaning you can change their content.
# Dictionaries can contain duplicate keys, but only the last value for a key will be kept.
person = {
    "name": "Emily",
    "age": 28,
    "profession": "Engineer",
}

# Accessing values in a dictionary
print(person["name"])


#adding a new key-value pair
person["email"] = "emily@example.com"
print(person)

#updating a value
person["profession"] = "Senior Engineer"
print(person)

#deleting a key-value pair
del person["age"]
print(person)


# loops through a dictionary
for key, value in person.items():
    print(f"{key}: {value}")
