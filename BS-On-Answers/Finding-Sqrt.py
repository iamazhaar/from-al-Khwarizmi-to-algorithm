'''

PROBLEM DESCRIPTION:

    1. You have a integer N
    2. You have to find out the sqrt(N) without the help of any built-in functions
    3. RETURN an INTEGER that is the sqrt(N)


THOUGHT PROCESS OF BRUTE FORCE:

    1. Start checking from i=0 to i=N as sqrt(N) >= 0 and sqrt(N) <= N
    2. Initialize an ANSWER variable
    3. CHECK each i whether i*i <= N and if it is update the ANSWER variable
    4. RETURN i when the loop ends


ANALYSIS:

    1. Time Complexity: O(n)
    2. Space Complexity: O(1)

'''



def LinearSearchToFindSqrt(n):
    ans = -1
    for i in range(n+1):
        if (i*i <= n):
            ans = i
        else:
            break                       # [As a programmer I optimized the algorithm by adding this else block]
    
    return ans



'''

THOUGHT PROCESS OF BETTER SOLUTION:

    1. Instead of running a FOR loop and checking each values we can run a WHILE loop with i*i<=n condition
    2. Initialize i=0
    3. As the loop exits RETURN i-1


ANALYSIS:

    1. Time Complexity: O(sqrt(n))
    2. Space Complexity: O(1)

'''



def OptimizedLinearSearchToFindSqrt(n):
    i = 0
    while (i*i <= n):
        i += 1
    
    return i - 1



'''

THE MOST EFFICIENT SOLUTION -> THOUGHT PROCESS:

    1. We know the searching range [0, N] -> BINARY SEARCH ON ANSWERS type problem
    2. We find the MID of the range and try to eliminate either the leftmost half or the rightmost half
    3. As a result the search space will get reduced at each iterative step
    4. If MID*MID > N then we know for sure the ANSWER we're looking for is in the leftmost part
    5. Hence we can eliminate the rightmost part
    6. If MID*MID <= N then it might be my answer, put it in the ANSWER variable and eliminate the leftmost part
    7. RETURN ANSWER at the end


ANALYSIS:

    1. Time Complexity: O(log n)
    2. Space Complexity: O(1)

'''



def FindSqrt(n):
    low = 0
    high = n
    ans = -1

    while (low <= high):
        mid = (low + high)//2
        if (mid * mid <= n):
            ans = mid
            low = mid + 1
        else:
            high = mid - 1
    
    return ans



# For Testing Purpose
'''

result = FindSqrt(625)
print(result)

'''