# using conditionals to 

# Compare 2 ages and indicate which age is older, younger or same age

# Age of Peter and age of Matt comparing both

print("Please type the age of Peter")
PeterAge=int(input())
print("Please type the age of Matt")
MattAge=int(input())

if PeterAge>MattAge:
    print("Petter is older than Matt")
elif PeterAge==MattAge:
    print("Peter & Matt have the same age")
else:
    print("Peter is younger thant Matt")