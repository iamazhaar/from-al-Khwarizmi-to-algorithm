'''

PROBLEM DESCRIPTION:

1. You have an ARRAY of N integers in NON-DECREASING order
2. You have an integer S denoting the Target Sum
3. You task is to find out 2 DISTINCT INDICES i, j such that A[i] + A[j] = S and i < j
4. If no such pair exists print -1


THOUGHT PROCESS:

1. Brute force solution is to use a nested loop -> T.C. = O(n^2)
2. Efficient solution is to use -> Two Pointers Approach or Arrays & Hashing Approach
3. Let's use Two Pointer Approach
4. Initialize 2 POINTER i=0 and j=n-1
5. Run a loop while(i < j)
6. Check if A[i] + A[j] = S, if so print i, j
7. If A[i] + A[j] < S -> Increment i
8. If A[i] + A[j] > S -> Decrement j
9. T.C. of Two Pointer Approach = O(n)


NOTES:
1. The following Two Pointer Algorithm only works when the ARRAY is SORTED

'''



def twoSumTrouble(arr, sum):
    n = len(arr)
    firstPointer = 0
    secondPointer = n-1

    while (firstPointer < secondPointer):
        if (arr[firstPointer] + arr[secondPointer] == sum):
            print(firstPointer, secondPointer)
            return
        elif (arr[firstPointer] + arr[secondPointer] < sum):
            firstPointer += 1
        else:
            secondPointer -= 1
    
    print(-1)



# For Testing Purpose
'''

A = [1, 3, 5, 7]
twoSumTrouble(A, 10)

'''