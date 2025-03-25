'''

PROBLEM DESCRIPTION:

1. You have a DATASET (Sorted or Unsorted Doesn't Matter)
2. You have an integer as KEY
3. You have to locate the POSITION of the KEY in the given DATASET
4. RETURN the POSITION

'''
'''

BRUTE FORCE ALGORITHM -> TC = O(n), SC = O(1)

THOUGHT PROCESS:
1. Start traversing the DATASET from the beginning
2. CHECK each element whether it's equal to the KEY
3. If it's equal RETURN the POSITION

'''

def linearSearch(dataset, key):
    n = len(dataset)
    for i in range(n):
        if (dataset[i] == key):
            return i
        
    return -1



# For Testing Purpose
'''

arr = [5, 1, -3, 2, 7]
result = linearSearch(arr, 7)
print(result)

'''