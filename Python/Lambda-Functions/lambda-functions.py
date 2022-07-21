# https://www.freecodecamp.org/news/lambda-function-in-python-example-syntax/
# Python Lambda Functions are anonymous function means that the function is without a name. 
# As we already know that the def keyword is used to define a normal function in Python. 
# Similarly, the lambda keyword is used to define an anonymous function in Python. 

# Syntax: lambda arguments: expression

# Can have any number of arguments but only one expression, which is evaluated and returned
# syntactically restricted to single expression

# Basic lambda function


string = 'GeeksForGeeks'
print_string = lambda string: string

print(print_string(string))

# Lambda with map
numbers = [1,2,3,4,5,6,7,8]
doubles = list(map(lambda x: x*2, numbers))
print(doubles)

# Lambda with filter
even_numbers = list(filter(lambda x: x%2==0, numbers))
print(even_numbers)

# Return lambda function from a function
def multiplyBy(n):
    return lambda x: x*n

double = multiplyBy(2)
triple = multiplyBy(3)

print(double(2))
print(triple(2))