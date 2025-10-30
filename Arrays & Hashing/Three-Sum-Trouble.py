'''

PROBLEM DESCRIPTION:
1. You have an ARRAY of N integers and a TARGET SUM
2. Your task is to find ALL UNIQUE TRIPLETS -> three values (at distinct positions) whose SUM = TARGET SUM


BRUTE FORCE:
1. Extreme naive solution is to run nested loops and explore all the possible triplets -> T.C. = O(n^3 * log M)
2. To get the UNIQUE TRIPLETS, I store the tuples in a SET
3. If I assume the set is implemented as a balanced BST, insertion takes O(log M).
4. In Python, though, set is hash-based → average O(1)
5. So, Theoretical Worst-Case: O(n^3 * log M)
6. But, Python Average Case: O(n^3)
7. S.C. = O(M) [M = number of unique triplets]


NOTES:
1. The ARRAY doesn't need to be sorted. Works for SORTED+UNSORTED array

'''



def brute3Sum(arr, size, sum):
    tripletSet = set()
    for i in range(size):
        for j in range(i+1, size):
            for k in range(j+1, size):
                if (arr[i]+arr[j]+arr[k] == sum):
                    tripletSet.add( tuple(sorted( (arr[i], arr[j], arr[k]) )) )

    return tripletSet



# For Testing Purpose
'''

A = [-1, 0, 1, 2, -1, -4]
triplets = brute3Sum(A, len(A), 0)
print(triplets)

'''



'''

BETTER SOLUTION:
1. The better solution of this problem will be to use HASHING
2. In Brute Force, I was running three loops to get 3 items of any triplets
3. Over here, I'm gonna use loops to get the first & second items of any triplets and then to find the third item I'm gonna use HASHING
4. Initialize a HASHMAP -> It basically stores the occurrences of each elements
5. Using HASHMAP to find 3rd item -> 3rd item = TARGET SUM - 1st item - 2nd item. Now if I see 3rd item exists in the HASHMAP then I have a triplet


TIME COMPLEXITY:
1.  -> Outer two loops: O(n²)
    -> Each insertion in set: O(log M)
    -> Each lookup/insertion in hashmap: O(1)
    -> Sorting each triplet: O(1)
Hence, Theoretical Worst-Case: O(n^2 * log M)

2.  O(N+M) 
    -> Assuming M unique triplet
    -> N items in HASHMAP


BEST SOLUTION:
1. For the best solution (most optimized) -> See Two Pointers/Three-Sum-Trouble.py


NOTES:
1. The ARRAY doesn't need to be sorted. Works for SORTED+UNSORTED array

'''



def better3Sum(arr, size, sum):
    tripletSet = set()

    hashmap = {}
    for i in range(size):
        if (arr[i] not in hashmap):
            hashmap[arr[i]] = 1
        else:
            hashmap[arr[i]] += 1
    
    for i in range(size):
        hashmap[arr[i]] -= 1
        for j in range(i+1, size):
            hashmap[arr[j]] -= 1
            thirdItem = sum - arr[i] - arr[j]
            if (thirdItem in hashmap and hashmap[thirdItem] != 0):
                tripletSet.add( tuple(sorted( (arr[i], arr[j], thirdItem) )) )

            hashmap[arr[j]] += 1

        hashmap[arr[i]] += 1
    
    return tripletSet



# For Testing Purpose
'''

A = [-1, 0, 1, 2, -1, -4]
triplets = better3Sum(A, len(A), 0)
print(triplets)

'''