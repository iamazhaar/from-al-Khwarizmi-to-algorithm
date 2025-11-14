'''

PROBLEM DESCRIPTION:

    1. You have a SORTED DATASET (Won't work for UNSORTED DATASET)
    2. You have an integer X
    3. Your task is to find the number of occurrences of X in the SORTED ARRAY
    4. If X is not present in the array then the number of occurrences = 0


THOUGHT PROCESS:

    1. I need to find the first & last occurrence of X first
    2. Then the number of occurrences of X is: (last-first)+1
    3. Similar to the previous problems I have solved -> First-Last-Occurrences.py or Bound-Search.py
    4. But here I'm gonna solve it by finding the first occurrence of X using BINARY SEARCH
    5. Then I'm find the last occurrence of X using BINARY SEARCH
    6. RETURN the number of occurrences = lastOccurrence - firstOccurrence + 1


ANALYSIS:

    1. Time Complexity: O(log n)
    2. Space Complexity: O(1)

    
NOTES:

    1. The logic will be changed accordingly if the DATASET is sorted in DESCENDING order

'''


def firstOccurrence(arr, x):
    low = 0
    high = len(arr) - 1
    initialOccurrence = -1

    while (low <= high):
        mid = (low+high)//2
        if (arr[mid] == x):
            initialOccurrence = mid
            high = mid - 1
        elif (arr[mid] > x):
            high = mid - 1
        else:
            low = mid + 1
    
    return initialOccurrence



def lastOccurrence(arr, x):
    low = 0
    high = len(arr) - 1
    finalOccurrence = -1

    while (low <= high):
        mid = (low+high)//2
        if (arr[mid] == x):
            finalOccurrence = mid
            low = mid + 1
        elif (arr[mid] > x):
            high = mid - 1
        else:
            low = mid + 1

    return finalOccurrence



def firstLastOccurrence(arr, x):
    initial = firstOccurrence(arr, x)
    final = -1
    if (initial != -1):
        final = lastOccurrence(arr, x)
    
    return (initial, final)



# For Testing Purpose
'''

A = [1, 2, 4, 6, 8, 8, 8, 10]
occurrences = firstLastOccurrence(A, 8)
print(occurrences)

'''