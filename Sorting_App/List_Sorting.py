def linear_sort(list):
    #somecode here
    print("Sorted list comes out here:")

def multiply_or_switch(a,b):
    if a*b < 1000:
        return a*b
    else:
        return a+b

def range_sum():
    _get =input("Enter the range number:")
    _input = int(_get)
    sum = 0
    for x in range(0,_input,):
        print("Previous sum = " + str(sum))
        sum = sum + x
        print("Present sum = " + str(sum))

range_sum()

