'''

PROBLEM DESCRIPTION:

    1. You have a Rotated Sorted Array with N DISTINCT Elements
    2. Your task is to find out how many times the array has been rotated


THOUGHT PROCESS:

    1. From Minimum-In-RSA.py I know how to find the minimum element in a Rotated Sorted Array
    2. Minimum element is basically the pivot of rotation
    3. Hence, its index = the number of rotation


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
    minValueIndex = -1

    while (low <= high):
        mid = (low+high)//2
        if (arr[low] <= arr[high]):                      # Indicates Search Space Is Completely Sorted
            if (arr[low] < minValue):                    # Then arr[low] is the smallest within the Search Space
                minValue = arr[low]
                minValueIndex = low
            break

        if (arr[low] <= arr[mid]):
            if (arr[low] < minValue):
                minValue = arr[low]
                minValueIndex = low
            low = mid + 1
        else:
            if (arr[mid] < minValue):
                minValue = arr[mid]
                minValueIndex = mid
            high = mid - 1
    
    return minValueIndex



# For Testing Purpose
'''

A = [4, 5, 6, 0, 1, 2]
rotationFrequency = findMinimumOfRSA(A, len(A))
print(rotationFrequency)

'''