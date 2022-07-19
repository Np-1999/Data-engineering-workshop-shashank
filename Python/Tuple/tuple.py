# https://www.geeksforgeeks.org/tuples-in-python/
# A Tuple is a collection of Python objects separated by commas. 
# In someways a tuple is similar to a list in terms of indexing, nested objects and repetition 
# but a tuple is immutable unlike lists which are mutable.

# Creating a tuple

t1 =()
print(t1)

t2 = "Python", "C"
print(t2)

t3 = ("Python", "C")
print(t3)

# Tuple with one element

t4 = "Python",  # Just need to add comma to let python know it is tuple

# Concatenation of tuples
print(t2+t3)

# Nesting of tuples
t5 = t3 , t4
print(t5)

# Repetition in tuple
t6 = t4*3
print(t6)

# Immutable tuples
# t6[0] = "ll" # Will throw an error
# print(t6)

# We can slice the tuple which will be covered in slice and dice part

# min max in tuple
print(min(t2))
print(max(t2))

# Good Read: https://stackoverflow.com/questions/626759/whats-the-difference-between-lists-and-tuples#