# https://www.geeksforgeeks.org/python-list-comprehension/
# Python List comprehension provides a much more short syntax for creating a new list based on the values of an existing list.
# Syntax newList = [ expression(element) for element in oldList if condition ] 

List = [x for x in range(0,11)]
print(List)

# Filtering using list comprehension

List = [x for x in range(0,11) if x%2 ==0 ]
print(List)


# Matrix using list comprehension / Nested list comprehension
matrix = [[j for j in range (0,3)] for i in range(0,3)]
print(matrix)

# List comprehensions vs For Loop
# The list comprehensions are more efficient both computationally and in terms of coding space and time than a for a loop

# You can specify operation with list comprehension
List = [i+10  for i in range(1,11)]
print(List)

# If else in list comprehension
List = ["Even number" if i % 2 == 0
        else "Odd number" for i in range(8)]
print(List)

# Displaying transpose of sq 2D - Matrix
twoDMatrix = [[10, 20, 30],
              [40, 50, 60],
              [70, 80, 90]]
print(len(twoDMatrix))
trans = [[i[j] for i in twoDMatrix] for j in range(len(twoDMatrix))]
print(trans)

# List of sum of digits for all odd numbers in the list
def digitSum(n):
    print("Digit sum called")
    dsum = 0
    for ele in str(n):
        dsum += int(ele)
    return dsum

List = [367, 111, 562, 945, 6726, 873]
newList = [digitSum(i) for i in List if i %2 !=0]
print(newList)
