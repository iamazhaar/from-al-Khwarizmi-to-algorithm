'''

PROBLEM DESCRIPTION:
1. You are given a SORTED ARRAY of N elements, and some QUERIES
2. In each query, you are given a pair [x, y]
3. You have to count how many numbers A[i] are there such that x <= A[i] <= y
4. For instance, if the array is [10, 20, 20, 45, 79] and you're given a query [20, 50], then answer will be 3 because there are in total 3 numbers that's value is between 20 and 50.
5. Hence, For each query [x, y], output a single integer P denoting the number of elements in the ARRAY 
such that x <= A[i] <= y


THOUGHT PROCESS:
1. First, I will find the lower bound of x
2. Then, I will find the upper bound of y
3. upperBound - lowerBound = the number of elements in the ARRAY such that x <= A[i] <= y


TIME & SPACE COMPLEXITY:
    -> T.C. = O(log N)
    -> S.C. = O(1)

'''



lower = lambda ele, x: ele >= x
upper = lambda ele, y: ele > y
 
def boundSearch(arr, size, value, compare):
    low = 0
    high = size - 1
    bound = size
 
    while (low <= high):
        mid = (low+high)//2
        if (compare(arr[mid], value)):
            high = mid - 1
            bound = mid
        else:
            low = mid + 1
    
    return bound
 
 

# For Testing Purpose
'''

arr = [10, 20, 20, 45, 79]
n = len(arr)
q = int(input("Sir, please enter the number of test cases: "))

for i in range(q):
    x, y = map(int, input().split())
 
    upperBound = boundSearch(arr, n, y, upper)
    lowerBound = boundSearch(arr, n, x, lower)
    print(upperBound-lowerBound)

'''