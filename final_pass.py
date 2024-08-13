#!/usr/bin/python
import random

# Turns user input into String
while True:
    try:
        pass_len = int(input("Enter a length for your password: "))
        break
    except ValueError:
        print("Enter a valid length for your passwords")

# Print randomized characters and special characters
print(''.join(random.choices("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_=+[]{}|;:'\",.<\
>?/~\\", k=pass_len)))
