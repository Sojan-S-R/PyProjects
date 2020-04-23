#-- Function to catch the sum from zero to entered number
def sum_function():
    sum = 0
    inputNumber = int(input("Enter the number: "))
    for x in range(0,inputNumber):
        sum = sum + x
    print("Sum of all numbers from 0 to {0} is {1}".format(inputNumber,sum))

#-- Function to print the Multiplication table of given number
def multiplication_table():
    inputNumber = int(input("Enter the number: "))
    factor = int(input("Enter the factor to which multiplication is needed: "))
    for x in range(0,factor+1):
        product = inputNumber*x
        print("{0} x {1} = {2}".format(inputNumber,x,product))

multiplication_table()
