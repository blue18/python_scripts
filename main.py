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
print("hello friend")
