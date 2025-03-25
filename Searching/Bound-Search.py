'''

PROBLEM DESCRIPTION:

1. You have a SORTED DATASET (Won't work for UNSORTED DATASET)
2. You have an integer X
3. You have to find the LOWER & UPPER BOUND of X in the given DATASET
4. RETURN the POSITIONS


DEFINITION OF LOWER & UPPER BOUND:
-> Lower Bound is the SMALLEST INDEX such that A[i] >= X
-> Upper Bound is the SMALLEST INDEX such that A[i] > X


THOUGHT PROCESS:

1. Think of the Binary Search algorithm
2. But here we're not just looking for the particular index of X rather we're looking for the SMALLEST INDEX of X
3. Hence we initialize ANS variable and UPDATE it accordingly
4. But if X is greater then the largest element in the DATASET then the BOUND will be the last HYPOTHETICAL INDEX = SIZE
5. So initialize ANS = SIZE of the DATASET and UPDATE it accordingly
6. RETURN the ANS variable


NOTES:
1. The logic will be changed accordingly if the DATASET is sorted in DESCENDING order

'''


# Bound Search Algorithm -> TC = O(log N), SC = O(1)  [Base of Logarithm = 2]

lower = lambda ele, x: ele >= x
upper = lambda ele, x: ele > x

def boundSearch(arr, target, compare):
    low = 0
    high = len(arr) - 1
    ans = len(arr)

    while (low <= high):
        mid = (low + high)//2
        if (compare(arr[mid], target)):
            ans = mid
            high = mid - 1
        else:
            low = mid + 1

    return ans



# For Testing Purpose
'''

A = [10, 20, 30, 40, 50]
result = boundSearch(A, 25, lower)
print(result)

'''