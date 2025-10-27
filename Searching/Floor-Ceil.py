'''

PROBLEM DESCRIPTION:

1. You have a SORTED ARRAY (Won't work for UNSORTED DATASET)
2. You have an integer X
3. You have to find the Floor & Ceil of X from the SORTED ARRAY
4. If Floor or Ceil doesn't exist RETURN -1


DEFINITION OF FLOOR & CEIL:

Floor(X) is the largest element in the array such that the element <= X
Ceil(X) is the smallest element in the array such that the element >= X


THOUGHT PROCESS:
1. I'm searching for some largest or smallest element in a SORTED ARRAY -> So, BINARY SEARCH TYPE
2. Observing more carefully, Ceil(X) is basically the LowerBound(X). I just need to return the element instead of the index


NOTES:
1. The logic will be changed accordingly if the DATASET is sorted in DESCENDING order
2. Definition remains the same though for DESCENDING order

'''


def findFloor(arr, x):
    low = 0
    high = len(arr) - 1
    floor = -1

    while (low <= high):
        mid = (low+high)//2
        if (arr[mid] <= x):
            floor = arr[mid]
            low = mid + 1
        else:
            high = mid - 1
    
    return floor



def findCeil(arr, x):
    low = 0
    high = len(arr) - 1
    ceil = -1

    while (low <= high):
        mid = (low+high)//2
        if (arr[mid] >= x):
            ceil = arr[mid]
            high = mid - 1
        else:
            low = mid + 1

    return ceil


# For Testing Purpose
'''

A = [10, 20, 30, 40, 50]
floorX, ceilX = findFloor(A, 25), findCeil(A, 25) 
print(floorX, ceilX)

'''