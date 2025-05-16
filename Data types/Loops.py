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

