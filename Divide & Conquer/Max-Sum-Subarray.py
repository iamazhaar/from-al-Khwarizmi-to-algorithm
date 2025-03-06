# Problem: Maximum Sum Subarray


import numpy as np
A = np.array([-1, 3, 4, -5, 9, -2])


# Brute Force Approach -> O(n^2)

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




# Divide and Conquer Approach -> O(n*logn)

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
    


x = maxSubarray(A, 0, len(A)-1)
print(f"The maximum sum is: {x[0]}\nThe maximum sum is found in the original array between index [{x[1]}, {x[2]}]")
