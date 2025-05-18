# Starting with while loops
# while loops are used to execute a block of code as long as a condition is true: syntax:

# while condition:
#     # code to execute
# Example:
count = 0
while count < 5:
    print("Count is:", count)
    count += 1  

# Store the correct PIN ("4321")

# Set attempts = 0

# Use a while loop that runs as long as:

# The entered PIN is not correct AND

# Attempts are less than 3

# After each wrong attempt, increase the attempts counter by 1 and show the user how many attempts are left.

# After the loop:

# If the PIN was correct, print success message

# Otherwise, print access denied

correct_pin = "4321"
attempts = 0
max_attempts = 3
pin = ""

while pin != correct_pin and attempts < max_attempts:
    pin = input("Enter your PIN: ")
    attempts += 1
    print(f"Number of attempts remaining: {max_attempts - attempts}")

if pin == correct_pin:
    print("PIN accepted. Welcome!")
else:
    print("Too many incorrect attempts. Access denied.")


# For loops
# for loops are used to iterate over a sequence (like a list, tuple, or string) or other iterable objects.
# The syntax is:
# for variable in iterable:
#     # code to execute
# Example:
items = ["shoes", "socks", "shirts", "pants","knife","fork","spoon","liquid"] 
for item in items:
    if item == "knife" or item == "liquid":
        print(f"Cannot pack {item} - not allowed on the plane")
    else:
        print(f"Packing {item}")
        
# using in to check if something exists in a list
# Example:

items = ["shoes", "socks", "shirts", "pants","fork","spoon",]
banned_items = ["knife", "liquid"]
for item in items:
    if item in banned_items:
        print(f"Cannot pack {item} - not allowed on the plane")
    else:
        print(f"Packing {item}")

# modifying it so that it counts how many items were packed vs how many were banned

items = ["shoes", "socks", "shirts", "pants", "knife", "fork", "spoon", "liquid"]
banned_items = ["knife", "liquid"]

items_banned = 0
items_packed = 0

for item in items:
    if item in banned_items:
        items_banned += 1
    else:
        items_packed += 1

print(f"Total items banned: {items_banned}")
print(f"Total items packed: {items_packed}")

# working with nested loops.
# Nested loops are loops inside other loops.
# syntax:
# for outer_variable in outer_iterable:
#     for inner_variable in inner_iterable:
home = {
    "Living Room": ["Couch", "TV", "Coffee Table"],
    "Bedroom": ["Bed", "Wardrobe", "Lamp"],
    "Kitchen": ["Fridge", "Oven", "Sink"]
}

for room in home:
    print(f"\nFurniture found in {room}:")
    
    for furniture in home[room]:
        print(f" - {furniture}")
    
    total_items = len(home[room])
    print(f"Total items in {room}: {total_items}")
# The break statement
# The break statement is used to exit a loop prematurely.
# Example:


    