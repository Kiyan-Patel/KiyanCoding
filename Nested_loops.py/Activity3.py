# Input a number

num = int(input("Enter the number : "))

t = num

numLen = 0

# Iterate the loop to find the length

while t > 0:

 numLen = numLen + 1

t = int(t / 10)

# Condition 1: Main 'if' statement

if numLen >= 4:

 numLen = int(numLen / 2)

chk = 0

while num > 0: # Iterate loop

 rem = num % 10

if chk == numLen: # Nested condition 1

 midOne = rem

elif chk == (numLen - 1):

 midTwo = rem

num = int(num / 10)

chk = chk + 1


prod = midOne * midTwo # Product of middle digits

print("\nProduct of Mid digits (" + str(midOne) + "*" + str(midTwo) + ") = ", prod)

# Line 45 Fix: This 'else' MUST line up perfectly with the 'if numLen >= 4:' above
else:

print("\nIt's not a 4 or more than 4-digit number!")