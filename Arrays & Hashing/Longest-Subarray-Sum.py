'''

PROBLEM DESCRIPTION:

1. You have an ARRAY OF INTEGERS
2. You have an integer as SUBARRAY-SUM
3. You have to find and print the LENGTH of the LONGEST CONTIGUOUS SUBARRAY whose SUM <= SUBARRAY-SUM
4. If no subarray has SUM <= SUBARRAY-SUM then the answer is: 0

'''
'''

BRUTE FORCE ALGORITHM -> TC = O(n^2), SC = O(1)

THOUGHT PROCESS:
1. Find the all possibile SUBARRAYS
2. Calculate the SUM of all possible SUBARRAYS
3. Initialize a MAX-LENGTH variable = 0
4. For each SUBARRAY, If SUM <= SUBARRAY-SUM, update the MAX-LENGTH variable as MAX-LENGTH = max(MAX-LENGTH, CURRENT SUBARRAY LENGTH)
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
            if (currentSubArrSum <= targetedSum):
                maxLen = max(maxLen, j-i+1)

    print(f"The Longest Subarray of Length {maxLen} Can be Found With Sum Less Than or Equals to {targetedSum}")




# For Testing Purpose
'''

A = [1, 1, 1, 1, 1]
sum = 5
longestSubarr(A, sum)

'''