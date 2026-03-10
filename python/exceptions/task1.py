def check_age(age):

    """ write a program that print the age its even or odd"""

    if age < 0:
        raise ValueError("Age cannot be negative")

    if age % 2 == 0:
        print("The age is even")
    else:
        print("The age is odd")

try:
    age = int(input("Enter your age: "))
    check_age(age)
except ValueError as e:
    print("Error:", e)
