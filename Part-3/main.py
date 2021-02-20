# Printing Strings:
print('Hello World')

# Printing Variables (That Contain Strings):
msg = 'Hello World'

print(msg)

# Printing Quotes:
msg = 'Hello \' World'  # Escapes the Quotes
msg = "Hello ' World"  # Uses Double Quotes

print(msg)

# Printing Multipule Line Strings:

msg = '''Hello
World
'''  # Using Three Quotes

print(msg)

# Getting Length:

msg = "Hello World"

print(len(msg))  # Length of msg

# Using Indexes:

msg = "Hello Tom"

print(msg[0])  # 1st Character

print(msg[0:5])  # 1st Character to 5th Character
print(msg[:5])

print(msg[6:9])  # 6st Character to Last Character
print(msg[6:])

print(msg[-1])  # Last Character
print(msg[-3:])  # -3rd Character to Last Character

# Using Methods:

msg = "My name is Abhigyan"

print(msg.capitalize())  # Message with First Letter Capital
print(msg.lower())  # Message in Lowercase
print(msg.upper())  # Message in Uppercase

print(msg.count("a"))  # Counts Number of Times String Passed Occurs
print(msg.replace("a", "e"))  # String Where a String is Replaced with a String
print(msg.strip())  # Removes All Whitespaces From Both Sides

# Find more methods at https://www.w3schools.com/python/python_ref_string.asp

# Joining Multipule Strings Together:

msg = "Hello"

print(msg + " World")  # msg and " World"

# .format() and F-strings:

msg = "Hello"

print("{msg}, Tom".format(msg=msg))  # "Hello, " and msg using .format()
print(f"{msg}, Tom")  # "Hello, " and msg using f-strings
