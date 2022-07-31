# https://www.geeksforgeeks.org/majority-element/
input = [1,1,1,1,1,2,3]
count = {}
for i in input:
    if(count.get(i) is  None):
        count[i] = 1
    else:
        count[i] = count[i]+1
    if count[i] > len(input)/2:
        print(i)
        break

# This solution takes O(N) time and  O(N) space

# Another solution with O(N) time and O(1) Space
# Moore's voting algorithm: https://www.youtube.com/watch?v=n5QY3x_GNDg

def findcandidate(A):
    candidate_index = 0
    count = 1
    for i in range(0, len(A)):
        if A[candidate_index] == A[i]:
            count +=1
        else:
            count -= 1
        if count == 0:
            candidate_index = i
            count = 1
    return A[candidate_index]

def majority_element(A):
    candidate_element = findcandidate(A)
    count = 0
    for i in A:
        if candidate_element == i:
            count +=1
        if count > len(A)//2:
            return candidate_element
    return -1

print(majority_element(input))
