'''

PROBLEM DESCRIPTION:

    1. Given an array of N integers.
    2. Sort the array in ascending order.

    
THOUGHT PROCESS:

    1. Repeat for N-1 passes.
    2. In each pass, the largest element in the unsorted part will bubble up to the highest index in the unsorted part
       -> That is why it is called BUBBLE SORT
    3. After all passes, the array becomes sorted in ascending order.

    
ANALYSIS:

    1. Time Complexity: Best = Average = Worst = O(n²)
    2. Space Complexity: O(1) (in-place)
    3. Stability: Stable

    
NOTES:

    1. The logic will change accordingly if I need to sort in descending order

'''



def bubbleSort(arr, n):
    for i in range(n-1):
        for j in range(n-1-i):
            if (arr[j] > arr[j+1]):
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
    
    return arr



# For Testing Purpose
'''

A = [3, 1, 2, 0, 5, 4]
sortedArr = bubbleSort(A, len(A))
print(sortedArr)

'''