#!/usr/bin/python3
# May 6, 2022


# List
userList = ["bob", "bill", "bruce"]

# Tuple
phoneNumbers = (9710001234, 9710002222)

# Strings
message = "hello friend"

# Set
someSet = {10, 2, "a", "d"}

# Dictionary
myDictionary = {1: 'apple', 2: 'orange'}


def compare(x, y):
    """Comparing values"""
    if x == y:
        return True
    else:
        return False


print(compare.__doc__)
print(compare(7, 7))
print(userList)
print(phoneNumbers)
print(someSet)
print("hello friend")
message = input("What is your name?")
