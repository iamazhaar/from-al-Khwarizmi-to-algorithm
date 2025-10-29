'''

PROBLEM DESCRIPTION:

1. You have an ARRAY of N integers in NON-DECREASING order
2. You have another ARRAY of M integers in NON-DECREASING order
3. Your task is to merge the two given array into one NON-DECREASING array.


THOUGHT PROCESS:

1. Observing carefully, it's the same merging technique I used in MERGE SORT
2. Initialize two pointers i=0 (pointing to the first array) and j=0 (pointing to the second array)
3. Initialize a new array of length (N+M)
4. Loop through while(i<N and j<M) and store the smallest value in new array -> Increment the corresponding pointer
5. When the loop terminates just append the remaining values to the new array
6. RETURN the new array
7. T.C. of this Two Pointer Approach = O(N+M) and S.C. = O(N+M)


NOTES:
1. The following Two Pointer Algorithm only works whern the both given ARRAY is SORTED in a specific order

'''



def mergeArray(arr1, n, arr2, m):
    newArr = []
    firstPointer = 0
    secondPointer = 0
    while (firstPointer < n and secondPointer < m):
        if (arr1[firstPointer] <= arr2[secondPointer]):
            newArr.append(arr1[firstPointer])
            firstPointer += 1
        else:
            newArr.append(arr2[secondPointer])
            secondPointer += 1
    
    while (firstPointer < n):
        newArr.append(arr1[firstPointer])
        firstPointer += 1
    while (secondPointer < m):
        newArr.append(arr2[secondPointer])
        secondPointer += 1
    
    return newArr



# For Testing Purpose
'''

a1 = [1, 3, 5, 7]
a2 = [2, 2, 4, 8]

sortedArr = mergeArray(a1, len(a1), a2, len(a2))
print(sortedArr)

'''