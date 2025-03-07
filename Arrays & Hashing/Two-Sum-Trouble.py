'''
PROBLEM DESCRIPTION:

1. You have a LIST OF INTEGERS
2. You have an integer as TARGETED SUM
3. You have to find if it is possible to find TWO VALUES from the LIST (at distinct positions) whose SUM == TARGETED SUM
4. If possible PRINT the distinct INDICES i,j WHERE i<j
5. If MULTIPLE SOLUTIONS EXISTS, you may PRINT ANY ONE of the valid answers
6. If no such pair exists, then PRINT -1.

'''




# BRUTE FORCE ALGORITHM -> TC = O(n^2), SC = O(1)

def twoSum(arr, targetedSum):
    n = len(arr)
    for i in range(n):
        for j in range(i+1, n):
            if (arr[i] + arr[j] == targetedSum):
                print(f"The Distinct Indices Are: {i}, {j}")
                return
    print(-1)




# A MORE BETTER APPROACH -> TC = O(n), SC = O(n)

def twoSumTrouble(arr, targetedSum):
    n = len(arr)
    hashmap = {}
    for i in range(n):
        diff = targetedSum - arr[i]
        if (diff in hashmap):
            print(f"The Distinct Indices Are: {hashmap[diff]}, {i}")
            return
        hashmap[arr[i]] = i
    print(-1)




# For Testing Purpose
'''

A = [1, 5, 8, 9, 9, 10]
target = 18
twoSumTrouble(A, target)

'''