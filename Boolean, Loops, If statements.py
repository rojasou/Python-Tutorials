# Booleans
print(True)
print("True")

print(type(True)) # This type is a Bool
print(type("True")) # This type is a String

# Testing whether these statements are true
print(5 == 5)
print(5 == 6)

# Incorporating the 'if' statement with boolean
x = 10
y = 5
if x % y == 0:
    print(True)
else:
    print(False)

# While loop
number = 1
while number < 4:
    print(number)
    if number == 2:
        break
    number = number + 1

# Incorporating the else statement to while loop
number = 1
while number < 4:
    print(number)
    number = number + 1
else:
    print("The number is no longer less than 4")

# Elif statement
number = 1
if number > 0:
    print("positive number")
elif number == 0:
    print("zero")
else:
    print("negative number")


