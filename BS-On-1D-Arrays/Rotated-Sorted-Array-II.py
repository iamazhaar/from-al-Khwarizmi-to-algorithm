'''

PROBLEM DESCRIPTION:

    1. You have a Rotated Sorted Array (Might Contain DUPLICATES)
    2. You have key X
    3. Your task is to determine whether X is in the Array or not


WHY Rotated-Sorted-Array-I.py WON'T WORK?

    -> Because, there is a perticular type of corner case that can't be handled by the previous searching algo. For instance, take [3, 1, 2, 3, 3, 3, 3, 3, 3] or [3, 3, 3, 3, 3, 3, 1, 2, 3]. Here, for 1st iteration low=0, high=n-1, mid = 4. Now A[low] = A[mid] = A[high] = 3. Hence, I can't correctly identify which half is actually SORTED HALF. But if i can somehow modify the previous solution such that it can handle this case as well then I'm done.


THOUGHT PROCESS:

    1. Searching for index in a SORTED DATASET -> BINARY SEARCH (MODIFIED)
    2. Calculate MID. If A[MID] == Key, RETURN True
    3. If not, I need to check if A[low] = A[mid] = A[high]. If so, I trim down the search space by low = low + 1 and high = high - 1. Beacuse as MID isn't the key and all three are equal hence current low and high is also not the key.
    4. After this I have to identify a SORTED HALF (either left or right half)
    3. Once I get a SORTED HALF I need to check if X exists within the SORTED HALF
    4. If exists then eliminate the other half


ANALYSIS:

    1. Time Complexity: O(log n)
    2. Space Complexity: O(1)


NOTES:

    1. The logic will be changed accordingly if the DATASET is sorted in DESCENDING order

'''



def searchingRotatedSortedArray(arr, key):
    low = 0
    high = len(arr) - 1

    while (low <= high):
        mid = (low+high)//2
        if (arr[mid] == key):
            return True
        
        if (arr[low] == arr[mid] and arr[mid] == arr[high]):
            low = low + 1
            high = high - 1
            continue

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
    
    return False



# For Testing Purpose
'''

rotatedArray = [3, 1, 2, 3, 3, 3, 3, 3, 3]
idx = searchingRotatedSortedArray(rotatedArray, 1)
print(idx)

'''