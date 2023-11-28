#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    check = (abs(number) % 10) * -1
else:
    check = number % 10
if check > 5:
    print(f"Last digit of {number} is {check} and is greater than 5")
elif check < 6 and check != 0:
    print(f"Last digit of {number} is {check} and is less than 6 and not 0")
elif check == 0:
    print(f"Last digit of {number} is {check} and is zero")
