#-- Linear Search sort function
#-- To be done later

def linear_sort(list):
    #somecode here
    print("Sorted list comes out here:")

#-- Function to switch output if output is > 100

def multiply_or_switch(a,b):
    if a*b < 1000:
        return a*b
    else:
        return a+b

#-- Gets the sum in the range given

def range_sum():
    _get =input("Enter the range number:")

    try:
        _input = int(_get)
    except:
        print("Sorry ! Wrong format error")

    sum = 0
    for x in range(0,_input,):
        sum = sum + x
        print("Sum of the range function is: " + str(sum))

#-- Prints the characters in the even index

def print_even_index():
    _input = input("Enter the string: ")
    for x in _input:
        index = _input.index(x)
        if index%2 == 0: 
            print(x)
        else:
            print("Odd index skipped !")

#-- Removes chars from an input string upto an input index

def remove_char():
    _input_string = input("Enter the string to operate: ")
    _input_index = int(input("Enter the index: "))
    _length = len(_input_string)            
    print("Processed string is: " + _input_string[_input_index:_length])

#-- List check for last and first numbers

def check_lastAndFirst():
    _input_list = input("Enter the input string: ")
    length = _input_list.count

