def add(a, b):
 return a+b

def subtract(a, b):

 return a - b

def multiply(a, b):

 return a * b

def divide(a, b):

# Triggers a ZeroDivisionError explicitly if b is 0

 if b == 0:

  raise ZeroDivisionError()

 return a / b

def main():

 print("=== Function Calculator ===")

 print("1. Add")

 print("2. Subtract")

 print("3. Multiply")

 print("4. Divide")


 choice = input("Select operation (1-4): ")


if choice not in ['1', '2', '3', '4']:

 print("Invalid operation choice!")

return

# try/except block to catch non-number inputs (ValueError)

try:

 num1 = float(input("Enter first number: "))

 num2 = float(input("Enter second number: "))

except ValueError:

 print("Error: That was not a valid number!")

  return

# try/except block to catch division by zero (ZeroDivisionError)

try:

 if choice == '1':

 print("Result:", add(num1, num2))

elif choice == '2':

 print("Result:", subtract(num1, num2))

elif choice == '3':

 print("Result:", multiply(num1, num2))

elif choice == '4':

 print("Result:", divide(num1, num2))

except ZeroDivisionError:

 print("Error: Cannot divide by zero!")

if __name__ == "__main__":

 main()