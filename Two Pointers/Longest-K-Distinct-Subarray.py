'''

PROBLEM DESCRIPTION:
1. You are given an ARRAY of integers of length N and an integer K
2. Your task is to find the LENGTH of the longest contiguous subarray that contains at most K distinct elements.


THOUGHT PROCESS:
1. This is basically a SLIDING WINDOW 2POINTER problem
2. But I also need to use HASHMAP to keep track of the number of distinct elements I've got so far -> len(HASHMAP)
3. Initialize two pointer both at index 0 and start traversing the ARRAY
4. As long as distinctCount <= K -> update it's frequency in HASHMAP (expanding window)
5. As distinctCount > K -> Keep shrinking the window untill distinctCount <= K
6. Keep track of the MAX LENGHT at each iteration
7. RETURN MAX LENGTH at the end of the loop


TIME & SPACE COMPLEXITY:
    -> T.C. = O(n) 
    -> S.C. = O(k) [k=the highest number of distinct elements I can have]

'''



def longestKdistinctSubarray(arr, size, maxDistinct):
    hashmap = {}
    firstPointer = 0
    maxSubarrayLength = 0

    for secondPointer in range(firstPointer, size, 1):
        hashmap[arr[secondPointer]] = hashmap.get(arr[secondPointer], 0) + 1

        while (len(hashmap) > maxDistinct):
            hashmap[arr[firstPointer]] -= 1
            if (hashmap[arr[firstPointer]] == 0):
                del hashmap[arr[firstPointer]]
            
            firstPointer += 1

        maxSubarrayLength = max(maxSubarrayLength, secondPointer-firstPointer+1)
    
    return maxSubarrayLength



# For Testing Purpose
'''

A = [6, 6, 5, 6, 1, 2]
maxSize = longestKdistinctSubarray(A, len(A), 2)
print(maxSize)

'''