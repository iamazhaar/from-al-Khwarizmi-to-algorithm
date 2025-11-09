'''

PROBLEM DESCRIPTION:

    1. Given an array of N integers.
    2. Sort the array in ascending order.

    
THOUGHT PROCESS:

    1. Divide the array into two parts — sorted and unsorted.
    2. Take each element from the unsorted part and store it temporarily.
    3. Insert it into its correct position within the sorted part.
       -> That's why it's called INSERTION SORT.
    4. Repeat until all elements are placed correctly and the array is sorted.

    
ANALYSIS:

    1. Time Complexity: Best = O(n), Average = Worst = O(n²)
    2. Space Complexity: O(1) (in-place)
    3. Stability: Stable

    
NOTES:

    1. The logic will change accordingly if I need to sort in descending order

'''



def insertionSort(arr, n):
    for i in range(1, n):
        value = arr[i]
        hole = i
        while (hole > 0 and arr[hole-1] > value):
            arr[hole] = arr[hole - 1]
            hole = hole - 1
        
        arr[hole] = value
    
    return arr
    


# For Testing Purpose
'''

A = [3, 1, 2, 0, 5, 4]
sortedArr = insertionSort(A, len(A))
print(sortedArr)

'''