import string
import random
import pyperclip

# Define character sets
s1 = list(string.ascii_lowercase)
s2 = list(string.ascii_uppercase)
s3 = list(string.digits)
s4 = list(string.punctuation)

# Ask user for password size
password_size = input("Enter the size of the password: ")

# Validate input for password size
while True:
    try:
        password_size = int(password_size)
        if password_size < 8:
            print("The size of the password must be 8 or above.")
            password_size = input("Please enter the size again: ")
        else:
            break
    except ValueError:
        print("Please enter a number only.")
        password_size = input("Enter the size of the password: ")

# Ensure at least one character from each category
password = [
    random.choice(s1),
    random.choice(s2),
    random.choice(s3),
    random.choice(s4)
]

# Create a pool of all possible characters
all_characters = s1 + s2 + s3 + s4

# Fill the rest of the password randomly from all character categories
while len(password) < password_size:
    password.append(random.choice(all_characters))

# Shuffle to ensure random order
random.shuffle(password)

# Convert the list to a string
password = "".join(password)

# Output the password
print(password)
print("Password copied to the clipboard")

# Copy the password to the clipboard
pyperclip.copy(password)
