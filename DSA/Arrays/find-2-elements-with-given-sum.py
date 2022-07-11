# Given an array A[] and a number x, check for pair in A[] with sum as x

def check_pair(a,target):
    for i in range(0,len(a)):
        for j in range (i+1, len(a)):
            if a[i] + a[j] == target:
                return True
    return False


a= [10,5,-10,2,3]
print(check_pair(a,5))


# Solution for geeks for geeks
# def hasArrayTwoCandidates(self,arr, n, x):
# 	    hm=set()
# 	    for number in arr:
# 	        temp = x-number
# 	        if number in hm:
# 	            return "Yes"
# 	        else:
# 	           hm.add(temp)
#         return None

# Solution can be extended to find triplets as below
# def find3Numbers(self,A, n, X):
        
#         for i in range(0,len(A)):
#             temp = X-A[i]
#             hm = set()
#             for j in range(i+1, len(A)):
#                 if temp - A[j] in hm:
#                     return True
#                 hm.add(A[j])