'''

PROBLEM DESCRIPTION:

    1. Given an array of N integers.
    2. Sort the array in ascending order.

    
THOUGHT PROCESS:

    1. Divide the array into two halves — left and right.
    2. Recursively sort both halves.
    3. Merge the two sorted halves into a single sorted array.
    4. Repeat until the entire array is sorted.

    
ANALYSIS:

    1. Time Complexity: Best = Average = Worst = O(n log n)
    2. Space Complexity: O(n) (not in-place)
    3. Stability: Stable

    
NOTES:

    1. The logic will change accordingly if I need to sort in descending order
    2. It's a Recursive sorting algorithm, in perticular DIVIDE & CONQUER type

'''


def merge(left, right, mergingArr):
    nL = len(left)
    nR = len(right)
    i = j = k = 0
    while (i < nL and j < nR):
        if (left[i] <= right[j]):
            mergingArr[k] = left[i]
            i += 1
        else:
            mergingArr[k] = right[j]
            j += 1
        k += 1
    
    while (i < nL):
        mergingArr[k] = left[i]
        i += 1
        k += 1
    
    while (j < nR):
        mergingArr[k] = right[j]
        j += 1
        k += 1



def mergeSort(arr):
    n = len(arr)
    if (n < 2):
        return
    mid = n // 2
    left = arr[ :mid ]
    right = arr[ mid: ]

    mergeSort(left)
    mergeSort(right)
    merge(left, right, arr)



# For Testing Purpose
'''

A = [3, 1, 2, 0, 5, 4]
mergeSort(A)
print(A)

'''