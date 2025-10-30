'''

PROBLEM DESCRIPTION:
1. You have an ARRAY of N integers and a TARGET SUM
2. Your task is to find ALL UNIQUE TRIPLETS -> three values (at distinct positions) whose SUM = TARGET SUM


THOUGHT PROCESS:
1. As I'm looking for A[i]+A[j]+A[k] = TARGET SUM
2. Here, if I keep A[i] as constant then A[j]+A[k] = TARGET SUM - A[i]
3. That just the Two-Sum-Trouble Problem that I have already solved previously
4. So, I can find A[j], A[k] using the 2Pointer Technique & I will get my triplet

TIME & SPACE COMPLEXITY:
1. T.C. = O(n^2)
2. S.C. = O(M) assuming there are M number of unique triplets

NOTES:
1. For the 2Pointer Algorithm to work the ARRAY need to be sorted (Won't work for unsorted array)

'''



def optimal3Sum(arr, size, targetSum):
    arr.sort()
    uniqueTriplets = []

    for i in range(size-2):
        if (i==0 or (i>0 and arr[i] != arr[i-1])):
            currentSum = targetSum - arr[i]
            firstPointer = i + 1
            secondPointer = size - 1

            while (firstPointer < secondPointer):
                if (arr[firstPointer]+arr[secondPointer] == currentSum):
                    uniqueTriplets.append( (arr[i], arr[firstPointer], arr[secondPointer]) )

                    while (firstPointer < secondPointer and arr[firstPointer] == arr[firstPointer+1]):
                        firstPointer += 1
                    while (firstPointer < secondPointer and arr[secondPointer] == arr[secondPointer-1]):
                        secondPointer -= 1
                    
                    firstPointer += 1
                    secondPointer -= 1

                elif (arr[firstPointer]+arr[secondPointer] < currentSum):
                    firstPointer += 1
                else:
                    secondPointer -= 1

    return uniqueTriplets



# For Testing Purpose
'''

A = [-1, 0, 1, 2, -1, -4]
triplets = optimal3Sum(A, len(A), 0)
print(triplets)

'''