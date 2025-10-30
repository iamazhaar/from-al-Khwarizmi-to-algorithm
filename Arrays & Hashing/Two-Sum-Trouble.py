'''
PROBLEM DESCRIPTION:

1. You have a LIST OF INTEGERS
2. You have an integer as TARGETED SUM
3. You have to find if it is possible to find TWO VALUES from the LIST (at distinct positions) whose SUM == TARGETED SUM
4. If possible PRINT the distinct INDICES i,j WHERE i<j
5. If MULTIPLE SOLUTIONS EXISTS, you may PRINT ANY ONE of the valid answers
6. If no such pair exists, then PRINT -1.

'''
'''

BRUTE FORCE ALGORITHM -> TC = O(n^2), SC = O(1)

THOUGHT PROCESS:
1. For each item in the list, find all its possible PAIRS
2. ADD them up and see, if SUM == TARGETED-SUM
3. If it is then print the DISTINCT INDICES and RETURN
4. If not just continue with the LOOP
5. Finally PRINT -1 when the loop ENDS

'''

# BRUTE FORCE ALGORITHM

def twoSum(arr, targetedSum):
    n = len(arr)
    for i in range(n):
        for j in range(i+1, n):
            if (arr[i] + arr[j] == targetedSum):
                print(f"The Distinct Indices Are: {i}, {j}")
                return
    print(-1)



'''

THOUGHT PROCESS FOR BETTER SOLUTION:
1. To achieve a better solution, we can think in terms of either TIME COMPLEXITY or SPACE COMPLEXITY
2. Let's think in terms of TC. 
3. Ok, what are the better TCs then O(n^2)?
4. Can we think of an approach with O(n*logn) or O(n) or O(sqrt(n)) or maybe with O(1) time complexity?
5. If we think a little bit, we will find out that there is an approach with O(n) TC if we use a HASHMAP (DICTIONARY in PYTHON)
6. Initialize a HASHMAP
7. For each element in the list find out the difference x between Targeted Sum & Current Element
8. IF x EXISTS in the HASHMAP then we got what we're looking for (2 DISTINCT INDICES)
9. ELSE we're going to put the (Current Element, Indices of Current Element) as (key, value) pair in the HASHMAP


FOR MOST OPTIMIZED SOLUTION -> SEE Two Pointers/Two-Sum-Trouble.py

'''

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