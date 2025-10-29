'''

PROBLEM DESCRIPTION:

1. You are given two integer arrays A and B of sizes N and M respectively, and an integer K
2. Both arrays are sorted in non-decreasing order
3. Your task is to find any pair of indices (i, j) such that:
    -> i is a valid index in array A (1<=i<=N)
    -> j is a valid index in array B (1<=j<=M)
    -> the sum A[i]+B[j] is closest to K (i.e., it minimizes |A[i]+B[j]-K| )
4. If there are multiple answers, output any


THOUGHT PROCESS:

1. Brute force solution is to use a nested loop -> T.C. = O(n^2)
2. Efficient solution is to use -> Two Pointers Approach
3. Why? Because, since both arrays are sorted, if we increase an element from A or B, the sum A[i] + B[j] increases — monotonically. That monotonicity allows us to avoid brute-force (no need to check every pair).
4. Start from one end of A and the opposite end of B
5. Then at each iteration compute currentSum = A[i] + B[j]
6. If currentSum == K -> got the pair of (i, j) -> BREAK
7. If currentSum < K  -> move i forward
8. If currentSum > K  -> move j backward
9. Track the minimum |currentSum - K|
10. RETURN (i, j)


TIME COMPLEXITY:
The following 2Pointer algorithm has a time complexity of O(N+M)


NOTES:
1. The following Two Pointer Algorithm only works when both the ARRAYS are SORTED

'''



def twoSumRevisited(arr1, arr2, sum):
    closeFactor = float("+inf")
    i, j = -1, -1
    firstPointer = 0
    secondPointer = len(arr2) - 1

    while (firstPointer < len(arr1) and secondPointer >= 0):
        currentSum = arr1[firstPointer] + arr2[secondPointer]
        factor = abs(currentSum - sum)
        if (factor < closeFactor):
            closeFactor = factor
            i, j = firstPointer, secondPointer
        
        if (currentSum == sum):
            break
        elif (currentSum < sum):
            firstPointer += 1
        else:
            secondPointer -= 1
        
    return (i+1, j+1)



# For Testing Purpose
'''

A = [-5, -2, -1, 5]
B = [-5, 0, 1, 1]

pairOfIndices = twoSumRevisited(A, B, 0)
print(pairOfIndices)

'''