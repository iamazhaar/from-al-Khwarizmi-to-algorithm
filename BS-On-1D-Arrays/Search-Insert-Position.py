'''

PROBLEM DESCRIPTION:

    1. You have a SORTED ARRAY of distinct values (Won't work for UNSORTED DATASET)
    2. You have a target value X
    3. You need to search for the index of the target value in the array
    4. If the value is present in the array , then return its index
    5. If not then determine the index where it would be inserted in the array while maintaining the sorted order


THOUGHT PROCESS:

    1. Think of the Lower Bound of X
    2. Lower Bound of X is the smallest index where A[i] >= X
    3. Hence, if the value is present in the array then the index of the target value is the lower bound
    4. If not then lower bound is the index where it should be inserted in the array while maintaining the sorted order

    
ANALYSIS:

    1. Time Complexity: O(log n)
    2. Space Complexity: O(1)


NOTES:

    1. The logic will be changed accordingly if the DATASET is sorted in DESCENDING order

'''



def lowerBound(arr, x):
    low = 0
    high = len(arr) - 1
    ans = len(arr)

    while (low <= high):
        mid = (low+high)//2
        if (arr[mid] >= x):
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    
    return ans



# For Testing Purpose
'''

A = [1, 2, 4, 7]
result = lowerBound(A, 1)
print(result)

'''