'''

PROBLEM DESCRIPTION:

1. You are given an ARRAY OF INTEGERS
2. You have to find the SUBARRAY that has the MAXIMUM-SUM
3. PRINT the MAXIMUM-SUM, the STARTING & ENDING INDICES of the MAX-SUM-SUBARRAY

'''
'''

BRUTE FORCE ALGORITHM -> TC = O(n^2), SC = O(1)

THOUGHT PROCESS:
1. Find the all possibile SUBARRAYS
2. Calculate the SUM of all possible SUBARRAYS
3. Initialize a MAX-SUM variable to -infinity
4. Initialize START, END INDEX variable
5. For each SUBARRAY, If CURRENT SUBARRAY-SUM > MAX-SUM, update the MAX-SUM, START, END INDEX variable
5. Print the MAX-SUM & range of indices

'''

# BRUTE FORCE ALGORITHM

def maxSumSubArray(arr):
    n = len(arr)
    maxSum = float("-inf")
    sIdx = -1
    eIdx = -1

    for i in range(n):
        currentSum = 0
        for j in range(i, n):
            currentSum += arr[j]
            if (currentSum > maxSum):
                maxSum = currentSum
                sIdx = i
                eIdx = j
    
    print(f"The maximum sum is: {maxSum}\nThe maximum sum is found in the original array between index [{sIdx}, {eIdx}]")



'''

THOUGHT PROCESS FOR BETTER SOLUTION:
1. Let's try to get a better solution in terms of TC
2. Can we think of an solution with TCs as O(n*logn) or O(n) or O(sqrt(n)) or maybe O(1)?
3. Let's think in term of DIVIDE & CONQUER
4. If we divide the array into 2 EQUAL PARTS then there are 3 POSSIBILITIES
5. Maybe the MAX-SUM-SUMARRAY we're looking for in in the LEFT PART or RIGHT PART or IN BETWEEN LEFT+RIGHT PART
6. To cover all the possibilities we calculate LSS, RSS, CSS and then return the MAXIMUM among them
7. Overall the algorithm is kind of similar to MERGE-SORT algorithm

'''

# Divide and Conquer Approach -> TC = O(n*logn), SC = O(1)

def crossingSubarray(A, p, q, r):
    maxSum = A[q]
    sI = q
    eI = q
    currentSum = A[q]
    for i in range(q-1, -1, -1):
        currentSum += A[i]
        if (currentSum > maxSum):
            maxSum = currentSum
            sI = i
    currentSum = maxSum
    for i in range(q+1, r+1):
        currentSum += A[i]
        if (currentSum > maxSum):
            maxSum = currentSum
            eI = i
    return (maxSum, sI, eI)




def maxSubarray(A, p, r):
    if (p==r):
        return (A[p], p, r)
    
    q = (p+r)//2
    L = maxSubarray(A, p, q)
    R = maxSubarray(A, q+1, r)
    C = crossingSubarray(A, p, q, r)

    if (C[0] >= L[0] and C[0] >= R[0]):
        return C
    elif (L[0] >= R[0] and L[0] >= C[0]):
        return L
    else:
        return R
    

# For Testing Purpose
''''

import numpy as np
A = np.array([-1, 3, 4, -5, 9, -2])

x = maxSubarray(A, 0, len(A)-1)
print(f"The maximum sum is: {x[0]}\nThe maximum sum is found in the original array between index [{x[1]}, {x[2]}]")

'''