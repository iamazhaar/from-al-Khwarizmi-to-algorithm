'''

PROBLEM DESCRIPTION:

    1. You are given an ARRAY OF INTEGERS
    2. You have to find the CONTIGUOUS SUBARRAY with MAXIMUM-SUM
    3. Print the MAXIMUM-SUM, the STARTING & ENDING INDICES of the MAX-SUM-SUBARRAY


THOUGHT PROCESS OF BRUTE FORCE ALGORITHM:

    1. For an array of N integers there're N*(N+1)/2 CONTIGUOUS SUBARRAY possible
    2. Initialize a MAX-SUM variable to -infinity
    3. Initialize START, END INDEX variable
    4. Calculate the SUM of all possible SUBARRAYS
    5. For each SUBARRAY, If CURRENT SUBARRAY-SUM > MAX-SUM, update the MAX-SUM, START, END INDEX variable
    5. Print the MAX-SUM & range of indices

    
ANALYSIS:

    1. As I'm checking all the possible N*(N+1)/2 CONTIGUOUS SUBARRAY
       Hence, Time Complexity: O(n^2)
    2. As required auxiliary space doesn't increase with the size of the input
       Hence, Space Complexity: O(1)

'''



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
    5. Maybe the CONTIGUOUS SUBARRAY with MAXIMUM-SUM is in the LEFT PART or RIGHT PART or MIDDLE (LEFT+RIGHT PART)
    6. To cover all the possibilities we calculate LSS, RSS, CSS and then return the MAXIMUM among them
    7. Overall the algorithm is kind of similar to MERGE-SORT algorithm


ANALYSIS:

    1. Recurrence Equation from the corresponding Recurrence Relation, T(n) = 2T(n/2) + n
       Hence, Time Complexity: O(n*log n)
    2. As required auxiliary space doesn't increase with the size of the input
       Hence, Space Complexity: O(1)

'''



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
    


'''

THOUGHT PROCESS BEHIND KADANE'S ALGORITHM (MOST OPTIMIZED):

    1. Initialize CURRENT_SUM = 0 & MAX_SUM = -infinity
    2. Iterate over the element of the array
    3. In each iteration add the element with the CURRENT_SUM
    4. Get the updated MAX_SUM = max(MAX_SUM, CURRENT_SUM)
    5. Then if (CURRENT_SUM < 0), Reset CURRENT_SUM = 0
    6. Return MAX_SUM


ANALYSIS:

    1. I'm just traversing the array one time
       Hence, Time Complexity: O(n)
    2. As required auxiliary space doesn't increase with the size of the input
       Hence, Space Complexity: O(1)

'''



def kadanesAlgorithm(arr):
    n = len(arr)
    maxSum = float("-inf")
    curSum = 0
    start = 0 
    end = 0
    tempStart = 0

    for i in range(n):
        curSum += arr[i]
        if (curSum > maxSum):
            maxSum = curSum
            start = tempStart
            end = i

        if (curSum < 0):
            curSum = 0
            tempStart = i + 1
    
    return (maxSum, start, end)



# For Testing Purpose
# ''''

A = [-1, 3, 4, -5, 9, -2]

x = kadanesAlgorithm(A)
print(f"The maximum sum is: {x[0]}\nThe maximum sum is found in the original array between index [{x[1]}, {x[2]}]")

# '''