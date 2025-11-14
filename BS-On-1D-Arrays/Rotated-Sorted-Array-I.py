'''

PROBLEM DESCRIPTION:

    1. You have a Rotated Sorted Array with N DISTINCT Elements
    2. You have key X
    3. Your task is to SEARCH for X in the Rotated Sorted Array and RETURN the index
    4. If X doesn't exist RETURN -1


WHY STANDARD BINARY SEARCH WON'T WORK?

    -> Because I don't have a completely sorted array of N elements rather I've a Rotated Sorted Array where the elements from index 0 to (n-1) aren't completely sorted.


THOUGHT PROCESS:

    1. Searching for index in a SORTED DATASET -> BINARY SEARCH (MODIFIED)
    2. As the array isn't completely sorted, hence after calculating the MID I have to identify a SORTED HALF (either left or right half)
    3. Once I get a SORTED HALF I need to check if X exists within the SORTED HALF
    4. If exists then eliminate the other half


ANALYSIS:

    1. Time Complexity: O(log n)
    2. Space Complexity: O(1)


NOTES:

    1. The logic will be changed accordingly if the DATASET is sorted in DESCENDING order
    2. The following algorithm WON'T WORK if the Rotated Sorted Array contains DUPLICATES -> See Rotated-Sorted-Array-II.py

'''



def searchingRotatedSortedArray(arr, key):
    low = 0
    high = len(arr) - 1

    while (low <= high):
        mid = (low+high)//2
        if (arr[mid] == key):
            return mid
        elif (arr[low] <= arr[mid]):
            if (arr[low] <= key and key <= arr[mid]):
                high = mid - 1
            else:
                low = mid + 1
        else:
            if (arr[mid] <= key and key <= arr[high]):
                low = mid + 1
            else:
                high = mid - 1
    
    return -1



# For Testing Purpose
'''

rotatedArray = [7, 8, 9, 1, 2, 3, 4, 5, 6]
idx = searchingRotatedSortedArray(rotatedArray, 1)
print(idx)

'''