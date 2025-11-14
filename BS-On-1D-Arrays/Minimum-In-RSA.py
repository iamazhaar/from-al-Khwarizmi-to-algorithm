'''

PROBLEM DESCRIPTION:

    1. You have a Rotated Sorted Array with N DISTINCT Elements
    2. Your task is to RETURN the minimum element in the Rotated Sorted Array


THOUGHT PROCESS:

    1. Searching for minimum value in a SORTED DATASET -> BINARY SEARCH (MODIFIED)
    2. Hence, after finding the mid I must eliminate either left or right segment
    3. As I'm looking for the minimum and it's a rotated sorted array, the minimum can exists in any of the segments
    4. So, which portion to eliminate? First find a SORTED HALF -> store the minimum of this part in the MIN variable -> Eliminate the SORTED HALF.
    5. Keep repeating the process
    6. RETURN MIN


ANALYSIS:

    1. Time Complexity: O(log n)
    2. Space Complexity: O(1)


NOTES:

    1. The logic will be changed accordingly if the DATASET is sorted in DESCENDING order
    2. The following algorithm WON'T WORK if the Rotated Sorted Array contains DUPLICATES
    3. If RSA contains DUPLICATES -> Follow the idea of See Rotated-Sorted-Array-II.py

'''



def findMinimumOfRSA(arr, n):
    low = 0
    high = n - 1
    minValue = float("+inf")

    while (low <= high):
        mid = (low+high)//2
        if (arr[low] <= arr[high]):                              # Indicates Search Space Is Completely Sorted
            minValue = min(minValue, arr[low])                   # Then arr[low] is the smallest within the Search Space
            break

        if (arr[low] <= arr[mid]):
            minValue = min(minValue, arr[low])
            low = mid + 1
        else:
            minValue = min(minValue, arr[mid])
            high = mid - 1
    
    return minValue



# For Testing Purpose
'''

A = [4, 5, 6, 0, 1, 2]
minimum = findMinimumOfRSA(A, len(A))
print(minimum)

'''