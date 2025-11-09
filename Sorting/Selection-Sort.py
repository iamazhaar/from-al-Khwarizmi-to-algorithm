'''

PROBLEM DESCRIPTION:

    1. Given an array of N integers.
    2. Sort the array in ascending order.

    
THOUGHT PROCESS:

    1. Repeat for N-1 passes.
    2. In each pass, find the smallest element in the unsorted part.
    3. Swap it with the first element of the unsorted part.
    4. After all passes, the array becomes sorted in ascending order.

    
ANALYSIS:

    1. Time Complexity: Best = Average = Worst = O(n²)
    2. Space Complexity: O(1) (in-place)
    3. Stability: Unstable

    
NOTES:

    1. The logic will change accordingly if I need to sort in descending order

'''



def selectionSort(arr, n):
    for i in range(n-1):
        minIndex = i
        for j in range(i+1, n):
            if (arr[j] < arr[minIndex]):
                minIndex = j

        temp = arr[i]
        arr[i] = arr[minIndex]
        arr[minIndex] = temp
    
    return arr



# For Testing Purpose
'''

A = [3, 1, 2, 0, 5, 4]
sortedArr = selectionSort(A, len(A))
print(sortedArr)

'''