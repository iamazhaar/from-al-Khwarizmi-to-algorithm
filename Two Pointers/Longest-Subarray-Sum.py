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



'''

THOUGHT PROCESS FOR BETTER SOLUTION: 
1. Let's try to get a better solution in terms of TC (You can think in terms of SC as well depending on your optimization critaria)
2. Can we think of an solution with TCs as O(n*logn) or O(n) or O(sqrt(n)) or maybe O(1)?
3. We can if we use the concepts of TWO-POINTERS. (NOTE: THIS IS A SLIDING WINDOW PROBLEM)
4. First initialize two pointers -> LEFT & RIGHT
5. Initialize MAX-LENGTH & CURRENT SUM to 0
6. The idea is to maintain a valid subarray using two pointers: LEFT and RIGHT
7. We keep expanding the RIGHT pointer to increase the MAX-LENGTH
8. If CURRENT SUM exceeds SUBARRAY-SUM, we shrink from the LEFT to make it valid again
9. Update MAX-LENGTH with the longest valid subarray found so far

'''

# A MORE BETTER APPROACH -> TC = O(n), SC = O(1)

def longestSubArr(arr, targetedSum):
    n = len(arr)
    left = 0
    maxLen = 0
    subArrSum = 0

    for right in range(n):
        subArrSum += arr[right]

        while (subArrSum > targetedSum and left <= right):
            subArrSum -= arr[left]
            left += 1

        maxLen = max(maxLen, right-left+1)
    
    print(f"The Longest Subarray of Length {maxLen} Can be Found With Sum Less Than or Equals to {targetedSum}")



# For Testing Purpose
'''

A = [4, 1, 2, 1, 5]
target = 4
longestSubArr(A, target)

'''