# Datatypes

x = "Some Characters" # String
y = 43 # Integer
z = 43.75 # Float

l = [x, y, z] # Mutable
t = (x, y, z) # Immutable
s = {x, y, z} # No Duplicate Items, Mutables

l.append("Hello")
l.append("Bye")

s.update(["Hello", "Bye"])

t = t + ("Hello", "Bye")

print(l)
print(t)
print(s)
