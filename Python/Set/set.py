# A Set is an unordered collection data type that is iterable, mutable and has no duplicate elements. 
# Python’s set class represents the mathematical notion of a set. 
# The major advantage of using a set, as opposed to a list, is that it has a highly optimized method for checking
#   whether a specific element is contained in the set. This is based on a data structure known as a hash table. 
# Since sets are unordered, we cannot access items using indexes like we do in lists.
# Only instances of immutable types can be added to a Python set
 
# Ways to define set
from asyncio import events
from typing import FrozenSet


a = set([1,2,3,4])
b = {1,2,3}
print(type(a))
print(type(b))

# Add an element to set
a.add(4)

# Frozen set are immutable objets that only supports methods that do not modify sets
c = frozenset([1,2,3])
# c.add(4) # This will not work
print(c)

# Set operation union
# Time complexity for union: O(len(s1) + len(s2))
a = set([1,2,3,4])

b = set([5,6,7,8])
c = a.union(b)
# Different syntax for union
c= a |b

print(a)
print(b)
print(c)

# Intersection
# Time complexity O(min(len(s1),len(s2)))

two_to_six = set([2,3,4,5,6])
even_till_six = set([2,4,6])
c= two_to_six & even_till_six
print(c)


# Difference 
# Time complexity O(len(s1))
c = two_to_six - even_till_six
print(c)

# clearing set
c.clear()

# Set operators
# Containment check

if 2 in even_till_six:
    print("True")

# non-containment check

if 3 not in even_till_six:
    print("True")

# equality check & not equality check
# != check can be perfomed as well
if even_till_six == two_to_six:
    print("Unexpected")

# Subset check
if even_till_six <= two_to_six:
    print("Subset")

# Proper subset
if even_till_six < two_to_six:
    print("Proper subset")

# Elements precisely in one set

a = {2,3,4}
b= {2,3,4,5}
c = a ^ b
print(c)

