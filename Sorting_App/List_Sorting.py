
#-- Linear Search sort function
#-- To be done later

# -- Function to search sub string in a given string 
def substring_search():
    _input_string = input("Enter the string to search in: ")
    _search_string = input("Enter the string to search: ")
    _split_list = _input_string.split(" ")
    _count = 0
    for x in range(0, len(_split_list)):
        if _split_list[x] == _search_string:
            _count = _count +1
    print("{0} appeared {1} times".format(_search_string,_count))

# -- Palidrome Check function
def palindrome_check():
    number = int(input('Enter the number: '))
    print("original number", number)
    originalNum = number
    reverseNum = 0
    while (number > 0):
        reminder = number % 10
        reverseNum = (reverseNum * 10) + reminder
        number = number // 10
    if (originalNum == reverseNum):
        print("True")
    else:
        print("False")
palindrome_check()


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
=======
def list_search():
    #enter the list size of the list
    _list_size = int(input("Enter the max index of list: "))
    
    #declare the list variable
    _list = []

    #list iteration to fetch the list values
    try:
        for x in range(0,_list_size):
            _list.append(int(input("Enter the {0} th element: ".format(x))))
    except:
        print("Sorry ! Ivalid entry or Not enough entries !")
    if _list[0] == _list[x]:
        print("First and last elements are the same !")
    else:
        print("First and last elements are different !")

# -- Function to return list members that are divisible by 5
def check_div_by_five():
    _list_size = int(input("Enter the list size: "))
    _list = []


    try:
        for x in range(0,_list_size):
            _list.append(int(input("Enter the {0}the element: ".format(x))))
    except:
        print("Sorry ! Invalid Entry or Doesn't match list size !")
    for x in range(0,_list_size):
        if _list[x]%5 == 0:
            print(_list[x])
