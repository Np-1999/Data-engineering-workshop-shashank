# Dictionaries are key value pairs and are indexed by keys. It is a mutable datastructure
# Tuples can be used as a keys if it contains immutable values
# Python dictionaries are implemented as hash tables.
# Recommended reading for hashing : https://www.geeksforgeeks.org/hashing-set-1-introduction/
# https://stackoverflow.com/a/9022835/8597871
pincodes = {'Nikhil':4123, 'NP':4455}

print(pincodes.get('Nikhil'))

pincodes['Nikhil'] = 4223 # Updating value for key Nikhil

print(pincodes.get('Nikhil'))

del pincodes['Nikhil'] # Deleting value for key Nikhil
print(pincodes)

if 'NP' in pincodes:
    print("Key is present in pincodes")


# Creating dict using array of tuple

pincodes = dict([('Nikhil',4112),('NP',4455)])
print(pincodes)

# Creating dict using dict comprehensions

squares ={val:val**2 for val in range(0,10)}
print(squares)

# Using keyword arguments
pincodes = dict(Nikhil=4455, NP=12345)

print(pincodes)

val_of_nikhil = pincodes.pop('Nikhil') # Returns value of key and deletes key

print(val_of_nikhil)


pincodes['PN'] = 1122 # Inserting new key
print(pincodes)
print(f" Last item of the list {pincodes.popitem()}")  # popitem deletes last element whereas pop deletes item with specified key


pincodes = {'Nikhil':4123, 'NP':4455}
pincodes2 = {'TD':4111, 'SJ': 4127, 'NP':1122}

pincodes.update(pincodes2) # Updates list with value from another list

print(pincodes)

print(pincodes.keys()) # Returns keys from dictionary

print(pincodes.values()) # Returns values from dictionary

print(pincodes.items()) # Returns a list of tuple

x = ('key1','key2')
y= 1     
print(pincodes.fromkeys(x,y)) # Returns a dictionary with keys from x and value of y
print(pincodes)

pincodes.setdefault('RP',4113)  # Returns the value of a key (if the key is in dictionary). If not, it inserts key with a value to the dictionary.
print(pincodes.get('RP'))
print(pincodes)


pincodes.clear() # Clears list
print(pincodes)

