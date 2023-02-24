# Q1) Write a function to print "hello_USERNAME!" 
# USERNAME is the input of the function. The first line of the code has been defined as below.

def hello_name(user_name):
    """This function print hello to user"""
    print('hello_' + user_name + "!")

hello_name("allisond756")

# Q2) Write a python function, first_odds that prints the odd numbers from 1-100 
# and returns nothing

def first_odds():
    """this function print odd numbers from 1-100 and returns nothing"""
    for value in range(1,101):
        if value % 2 == 0:
            continue
        else:
            print(value)
    
first_odds()

# Q3) Please write a Python function, max_num_in_list to return the max number of a given list. 
# The first line of the code has been defined as below.

def max_num_in_list(a_list):
    """function returns the max number in a list"""
    return max(a_list)

a_list = [12,5,89,142,65,8,13,47]
print(max_num_in_list(a_list))

# Q4) Write a function to return if the given year is a leap year. 
# A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. 
# The return should be boolean Type (true/false).

def is_leap_year(a_year):
    """This function tells you if a certain year is a leap year or not"""
    if (int(a_year) % 4 == 0) and (int(a_year) % 100 != 0):
        return True
    elif int(a_year) % 400 == 0:
        return True
    else:
        return False
    
print(is_leap_year("2020"))
print(is_leap_year("2023"))
print(is_leap_year("2008"))

# Q5) Write a function to check to see if all numbers in list are consecutive numbers. 
# For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive 
# numbers. The return should be boolean Type.

def is_consecutive(b_list):
    """this function checks to see if a list consists of consecutive numbers"""
    if b_list == list(range(b_list[0],b_list[-1]+1)):
        return True
    else:
        return False

        
b_list = [1,2,3,4,5,9]
print(is_consecutive(b_list))
