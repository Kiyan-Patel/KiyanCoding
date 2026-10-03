try:
    num1, num2=int(input("Enter two number with a comma separating each : "))
    result=num1/num2
    print("Result is ", result)

except ZeroDivisionError:
    print("You cannot divide by 0")

except SyntaxError:
    print("Incorect format you must add a comma in between each number. ")

except:
    print("Wrong input")

else:
    print("No execeptions")

finally:
    ("This code will run no matter what!!!")