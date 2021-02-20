# Integers - Without Decimal Point
# Floats - With Decimal Point

ints = 1, 2, 3
floats = 1.5, 2.5, 3.5

print(type(1), type(1.5))

# Comparing Values:

x = 5
y = 10

print(x == y)
print(x != y)

print(x < y)
print(x > y)
print(x <= y)
print(x >= y)


# Addition:

total = 19 + 21  # Addion Two Integers

print(total)

# Subtraction:

total = 21 - 19  # Subtraction Two Integers

print(total)

# Multiplication:

total = 21 * 19

print(total)

# Division:

total = 20 / 2

print(total)

# Floor Division:

total = 20 // 2

print(total)

# Modulus:

total = 19 % 2

print(total)

# Exponent:

total = 2 ** 3

print(total)

# Changing Values:

num = 2

num = num + 2  # Addition
num = num - 2  # Subtraction
num = num * 2  # Multiplication
num = num / 2  # Division

num += 2  # Addition
num -= 2  # Subtraction
num *= 2  # Multiplication
num /= 2  # Division

print(num)

# Rounding Values:

print(round(3.14))  # By default rounds to the nearest number
print(round(3.14, 1))  # Rounds to the first decimal digit

# Absolute Values:

print(abs(-10))

# Strings to Int, Float:

str1 = "10"
str2 = "5"

print(int(str1))  # Prints str1 as an int

print(str1 + str2)
print(int(str1) + int(str2))

str3 = "10.5"
str4 = "5.2"

print(float(str3))  # Prints str1 as an float

print(str3 + str4)
print(float(str3) + float(str4))

# Number to string

int1 = 4
int2 = 10

print(str(int1) + str(int2))  # Uses str
