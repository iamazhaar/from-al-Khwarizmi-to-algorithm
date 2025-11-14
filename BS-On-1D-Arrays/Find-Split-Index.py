'''
PROBLEM DESCRIPTION:

    1. Given a 0-indexed integer array containing n unique values
    2. For some index i, the values are in decreasing order from index 0 to (i-1), and then again from i to (n-1)
    3. It is guaranteed that the value of index 0 is smaller than the value of index (n-1)
    4. Given such an array, design an algorithm to find the index i with a better time complexity than O(n)


THOUGHT PROCESS:

    1. The problem gives us two decreasing segments and one crucial guarantee: arr[0] < arr[n-1]
    2. In essence, I need to find the starting index of the 2nd decreasing segment
    3. Hence, somehow i need to determine which segment i'm courrently standing at
    4. In the 1st segment, all elements are <= arr[0]
    5. In the 2nd segment, all elements are >= arr[n-1]
    6. And as arr[0] < arr[n-1], I can simply say if (arr[mid]>arr[n-1]) mid pointer is currently in 2nd segment,
    Otherwise 1st segment
    7. But to get the starting index of 2nd segment I need to go left -> high = mid - 1

    
ANALYSIS:

    1. Time Complexity: O(log n)
    2. Space Complexity: O(1)
    
'''



def findSplitIndex(arr):
    n = len(arr)
    low = 0
    high = n - 1
    splitIndex = n

    while (low <= high):
        mid = (low + high)//2
        if (arr[mid] >= arr[n-1]):
            splitIndex = mid
            high = mid - 1
        else:
            low = mid + 1
    
    return splitIndex



# For Testing Purpose
'''

A = [5, 4, 1, 12, 10, 9, 7, 6]
splitIndex = findSplitIndex(A)
print(splitIndex)

'''