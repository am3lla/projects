#!/usr/bin/env python3

class InvalidPasswordException(Exception):
    def __init__(self, message):
        self.message = message

try:
    
    password = input("Enter password: ")

    if 8 > len(password):
        raise InvalidPasswordException("Invalid password length")

except InvalidPasswordException as invalidPasswordException:
    print(invalidPasswordException)
