l = [1, 2, 3]  # Creating the List

# Length of the list:

print(len(l))  # Getting the length of the list

# Comparing/Checking the list:

print(1 in l)  # Checking if 1 is in the list
print([1, 2, 3] == l)  # Checking if the list is [1, 2, 3]
print([2, 4, 6] != l)  # Checking if the list is not [2, 4, 6]

# Indexing:

print(l[0])  # Getting the First element in the list
print(l[2])  # Getting the Third element in the list
print(l[-1])  # Getting Last element in the list
print(l[1:3])  # Getting the First element (included) to Fourth element in the list
print(l[:2])  # Getting the First element (included) to Third element in the list

# Changing the list:

l.append(4)  # Using append to add the list
l.remove(4)  # Using remove to remove the list
l.extend([0, -1])  # Joining the list with another list

l.pop()  # To remove last element in the list
l.insert(0, 4)  # Adding element at specific index in the list

l.sort(reverse=True)  # Using sort(reverse=True) to reverse the list
l.reverse()  # Reversing the list
