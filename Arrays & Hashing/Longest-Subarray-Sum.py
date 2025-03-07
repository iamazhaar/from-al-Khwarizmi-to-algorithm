'''

PROBLEM DESCRIPTION:

1. You have an ARRAY OF INTEGERS
2. You have an integer as SUBARRAY-SUM
3. You have to find and print the LENGTH of the LONGEST CONTIGUOUS SUBARRAY whose SUM == SUBARRAY-SUM
4. If no subarray has SUM == SUBARRAY-SUM then the answer is: 0

'''
'''

BRUTE FORCE ALGORITHM -> TC = O(n^2), SC = O(1)

THOUGHT PROCESS:
1. Find the all possibile SUBARRAYS
2. Calculate the SUM of all possible SUBARRAYS
3. Initialize a MAX-LENGTH variable = 0
4. For each SUBARRAY, If SUM == SUBARRAY-SUM, update the MAX-LENGTH variable as MAX-LENGTH = max(MAX-LENGTH, CURRENT SUBARRAY LENGTH)
5. Print the MAX-LENGTH variable

'''

# BRUTE FORCE ALGORITHM

def longestSubarr(arr, targetedSum):
    n = len(arr)
    maxLen = 0
    for i in range(n):
        currentSubArrSum = 0
        for j in range(i, n):
            currentSubArrSum += arr[j]
            if (currentSubArrSum == targetedSum):
                maxLen = max(maxLen, j-i+1)

    print(f"The Longest Subarray of Length {maxLen} Can be Found With Sum Less Than or Equals to {targetedSum}")



'''

THOUGHT PROCESS FOR BETTER SOLUTION:
1. Let's try to get a better solution in terms of TC (You can think in terms of SC as well depending on your optimization critaria)
2. Can we think of an solution with TCs as O(n*logn) or O(n) or O(sqrt(n)) or maybe O(1)?
3. We can if we use a HASHMAP. Why?
4. Suppose, the array = [.....................]
5. Initialize MAX-LENGTH = 0, PREFIX-SUM = 0, and HASHMAP to store PREFIX-SUM
6. Iterate through the array and update PREFIX-SUM
7. Update MAX-LENGTH if PREFIX-SUM == SUBARRAY-SUM
8. Update MAX-LENGTH if (PREFIX-SUM - SUBARRAY-SUM) in HASHMAP (This makes sure you don't miss any valid SUBARRAY found somewhere in the middle)
9. Store the first occurrence of each PREFIX-SUM in HASHMAP (This ensures STEP-8 will work)
10. Continue iterating until the end of the array and print MAX-LENGTH.

'''

# A MORE BETTER APPROACH -> TC = O(n), SC = O(n)

def longestSubArr(arr, targetedSum):
    n = len(arr)
    hashmap = {}
    maxLen = 0
    prefixSum = 0
    for i in range(n):
        prefixSum += arr[i]
        if (prefixSum == targetedSum):
            maxLen = max(maxLen, i+1)
        if ((prefixSum-targetedSum) in hashmap):
            maxLen = max(maxLen, i-hashmap[prefixSum-targetedSum])
        hashmap[prefixSum] = i

    print(f"The Longest Subarray of Length {maxLen} Can be Found With Sum Less Than or Equals to {targetedSum}")



# For Testing Purpose
'''

A = [1, 2, 6, 4, 3, 2, 3, 1, 4, 2]
sum = 12
longestSubArr(A, sum)

'''