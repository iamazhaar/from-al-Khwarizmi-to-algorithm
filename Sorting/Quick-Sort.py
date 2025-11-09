'''

PROBLEM DESCRIPTION:

    1. Given an array of N integers.
    2. Sort the array in ascending order.

    
THOUGHT PROCESS:

    1. Base case: If the segment has 0 or 1 element, it's already sorted — return.
    2. Choose a PIVOT (e.g., first, last, median, or random).
    3. Partition the segment so ELEMENT ≤ PIVOT end up LEFT and ELEMENT > PIVOT end up RIGHT.
    4. Place the PIVOT in its final position.
    5. Recursively sort the left partition and the right partition.
    6. When all recursive calls return, the segment is sorted.

    
ANALYSIS:

    1. Time Complexity: Best = Average = O(n log n), Worst = O(n²)
    2. For Randomized Version of Quick Sort: Best = Average = Worst = O(n log n)
    2. Space Complexity: Best = O(log n), Worst = O(n) (Worst Case Can Always Be Avoided By Using The Randomized Version)
    3. In-Place Sorting Algorithm (As worst case is always avoided and log n is almost constant for large n)
    4. Stability: Unstable

    
NOTES:

    1. The logic will change accordingly if I need to sort in descending order
    2. It's a Recursive sorting algorithm, in perticular DIVIDE & CONQUER type
    3. Choice of pivot affects performance — a good pivot gives average O(n log n), a poor pivot can lead to O(n²)

'''



import random

def partition(arr, start, end):
    pivot = arr[end]
    pIndex = start

    for i in range(end):
        if (arr[i] <= pivot):
            arr[pIndex], arr[i] = arr[i], arr[pIndex]
            pIndex += 1
    
    arr[pIndex], arr[end] = arr[end], arr[pIndex]
    return pIndex



def randomizedPartition(arr, start, end):
    pivotIndex = random.randint(start, end)
    arr[pivotIndex], arr[end] = arr[end], arr[pivotIndex]

    return partition(arr, start, end)



def quickSort(arr, start, end):
    if (start >= end):
        return
    
    pIndex = randomizedPartition(arr, start, end)
    quickSort(arr, start, pIndex-1)
    quickSort(arr, pIndex+1, end)



# For Testing Purpose
'''

A = [3, 1, 2, 0, 5, 4]
quickSort(A, 0, len(A)-1)
print(A)

'''