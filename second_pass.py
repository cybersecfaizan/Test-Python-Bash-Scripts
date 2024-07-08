#!/usr/bin/python

import secrets

# Prompts user to select the length of their password.
while True:
    try:
        pass_len=int(input("Enter a length for your password: "))
        break;
    except ValueError:
        print("Please enter a valid number")
