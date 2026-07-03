import random
import string

print("===== PASSWORD GENERATOR =====")

# User input
length = int(input("Enter password length: "))

# Character sets
lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
numbers = string.digits
symbols = string.punctuation

all_characters = lowercase + uppercase + numbers + symbols

# Generate password
password = ""

for i in range(length):
    password += random.choice(all_characters)

print("\nGenerated Password:")
print(password)