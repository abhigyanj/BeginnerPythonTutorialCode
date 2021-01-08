print("Comparing Numbers")
print("-" * 50)

a = float(input("Enter a number:\n"))
b = float(input("Enter an another number:\n"))

if a > b:
    print(str(a) + " is greater than " + str(b))
elif a < b: 
    print(str(a) + " is less than " + str(b))
else:
    print(str(a) + " is equal to than " + str(b))

