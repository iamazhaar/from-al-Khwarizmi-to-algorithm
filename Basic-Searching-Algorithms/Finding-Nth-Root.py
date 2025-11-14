'''

PROBLEM DESCRIPTION:

1. You have two integer N, M 
2. You have to find out the Nth root of M without the help of any built-in functions
3. RETURN an INTEGER that is the Nth root of M
4. If doesn't exist RETURN -1


THOUGHT PROCESS:

1. This a BINARY SEARCH ON ANSWERS type problem
2. I know the range of answers that is 1 to M
3. Gonna apply BINARY SEARCH on the range(1, M) by assigning low = 1, high = M
4. If (MID)^N == M -> RETURN MID
5. If (MID)^N > M -> Eliminate the RIGHT HALF
6. Otherwise eliminate the LEFT HALF

'''



def compute(base, pow, m):
    product = 1
    for i in range(pow):
        product = product * base
        if (product > m):
            return 2
    
    if (product == m):
        return 1
    
    return 0



def nthRoot(m, n):
    low = 0
    high = m
    while (low <= high):
        mid = (low+high)//2
        midN = compute(mid, n, m)
        if (midN == 1):
            return mid
        elif (midN == 2):
            high = mid - 1
        else:
            low = mid + 1
    
    return -1



# For Test Prupose
'''

root = nthRoot(344, 3)
print(root)

'''