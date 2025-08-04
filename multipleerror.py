try:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter a number: "))
    result = num1/num2
    print("the result is ",result)

except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("please  enter numeric value only ",e)

except Exception as a:
    print("the exception is:", a)

except :
    print("some error occurred:", )

finally:
    print("i will execute no matter what")

