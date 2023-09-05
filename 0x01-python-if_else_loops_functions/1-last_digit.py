#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)

# Find the last digit of the number
last_digit = abs(number) % 10
if number < 0:
    last_digit = -last_digit

if last_digit > 5:
    comparison = "and is greater than 5"
elif last_digit == 0:
    comparison = "and is 0"
else:
    comparison = "and is less than 6 and not 0"

print("Last digit of", number, "is", last_digit, comparison)
