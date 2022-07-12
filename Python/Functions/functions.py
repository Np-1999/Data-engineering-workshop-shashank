from typing import List


def add(x:int, y:int) -> int:
    return x+y

# Default arguments

def add_ten(y:int,x:int =10) -> int: # once we have a default argument, all the arguments to its right must also have default values. # i.e. def add_ten(y:int =10,x:int ) this won't work
    return x+y

# Keyword arguments
def sub(x:int, y:int) -> int:
    return x-y
print(sub(y=10,x=12))  # In keyword argument caller specify the parameter name and value so no need to remember the order of parameters

# Variable length arguments
# *args (Non-keyword arguments) # it is not compulsory to use args 
# **kwargs (Keywoed arguments) # it is not compulsory to use kwargs

def print_strings(*strings):
    for x in strings:
        print(x)
print_strings("NIK","NP","Nikhil")

def print_key_values(**key_val):
    """ Prints key value pair """
    for key, value in key_val.items():
        print(f"{key} = {value}")
print_key_values(name="NP", pincode="4111")

# Docstring
# The first string after the function is called the Document String
print(print_key_values.__doc__)


# Python uses call by sharing for calling functions https://stereobooster.com/posts/call-by-name-by-reference-by-sharing/
# You can change values of mutable objects in function so that they are also changed outside the function too. Such as list, dictionary etc.
# For immutable object, the link between caller variable and function is broken and they no longer related as shown in function increment_x

x = 0

def increment_x(y:int)->None:   # New copy of x is created here with the reference  y  and has same value as x and there is no link between x and y
    y=y+1

increment_x(x)
print(x)

# Caling function with mutable datatype
list_a = [10,50,100,200]

def first_2k(list_a) -> None:
    list_a[0] = 2000 # This is mutations
    list_a = [123,456] # This is reassignment # This statement will have no effect outside this function as assignment operator will create a new refrence and have its local scope stored in list_a.
first_2k(list_a)
print(list_a)