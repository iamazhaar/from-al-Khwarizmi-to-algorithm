'''

PROBLEM DESCRIPTION:

    1. You have a SORTED DATASET (Won't work for UNSORTED DATASET)
    2. You have an integer X
    3. Your task is to find the first & last occurrence of X in the SORTED ARRAY
    4. If X is not present in the array then the first & last occurrence will be -1


THOUGHT PROCESS:

    1. I'm basically searching for some index in a SORTED DATASET -> So, BINARY SEARCH TYPE
    2. Observing more carefully, the first occurrence is basically the LowerBound(X) IFF LowerBound(X) == X
    3. If LowerBound(X) != X || LowerBound(X) == Size then actually X doesn't exist in the SORTED DATASET
    4. If LowerBound(X) doesn't exist, the first & last occurrence both is -1
    5. If first occurrence exists then the last occurrence also exists
    6. Observing carefully, the last occurrence is basically the UpperBound(X) - 1


ANALYSIS:

    1. Time Complexity: O(log n)
    2. Space Complexity: O(1)


NOTES:

    1. The logic will be changed accordingly if the DATASET is sorted in DESCENDING order

'''



lower = lambda ele, x: ele >= x
upper = lambda ele, x: ele > x

def boundSearch(arr, x, compare):
    low = 0
    high = len(arr) - 1
    bound = len(arr)

    while (low <= high):
        mid = (low+high)//2
        if (compare(arr[mid], x)):
            bound = mid
            high = mid - 1
        else:
            low = mid + 1

    return bound



def firstLastOccurrence(arr, ele):
    firstOccurrence = -1
    lastOccurrence = -1
    lowerBound = boundSearch(arr, ele, lower)
    if (lowerBound != len(arr) and arr[lowerBound] == ele):
        firstOccurrence = lowerBound
        lastOccurrence = boundSearch(arr, ele, upper) - 1
    
    return (firstOccurrence, lastOccurrence)



# For Testing Purpose
'''

A = [1, 2, 4, 6, 8, 8, 8, 10]
occurrences = firstLastOccurrence(A, 8)
print(occurrences)

'''