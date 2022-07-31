# http://www.geeksforgeeks.org/check-for-majority-element-in-a-sorted-array/
# Question: Write a code to find if a given integer x appears more than n/2 times in a sorted array of n integers. 

def binarysearch(x, arr,start, end):
    if end < start:
        return -1
    mid = (end+start) //2
    if (x == arr[mid]) and (mid == 0 or arr[mid-1]<x): # Modification to find first index
        return mid
    elif x< arr[mid]:
        return binarysearch(x,arr,start, mid-1)
    else:
        return binarysearch(x,arr,mid+1, end)

input =[1, 2, 3, 3, 3, 3, 10]
x=3
first_index = binarysearch(6,input,0,len(input)-1)
last_index = first_index + (len(input)//2)
if input[last_index] == x:
    print(f"{x} is a major element")
else:
    print(f"{x} is not a major element")