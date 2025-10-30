'''

PROBLEM DESCRIPTION:
1. You have an ARRAY of N integers and a TARGET SUM
2. Your task is PRINT 3 integers -> the index of the values (at distinct indices) whose SUM = TARGET SUM
3. If there are several solutions, you may PRINT any of them
4. If there are no solutions, PRINT -1


THOUGHT PROCESS:
1. As I'm looking for A[i]+A[j]+A[k] = TARGET SUM
2. Here, if I keep A[i] as constant then A[j]+A[k] = TARGET SUM - A[i]
3. That just the Two-Sum-Trouble Problem that I have already solved previously
4. So, I can find A[j], A[k] using the 2Pointer Technique & I will get my triplet
5. But, I need to return the DISTINCT INDICES of the ORIGINAL ARRAY (As I will SORT it to implement 2Pointer)

TIME & SPACE COMPLEXITY:
1. T.C. = O(n^2)
2. S.C. = O(1)

NOTES:
1. For the 2Pointer Algorithm to work the ARRAY need to be sorted (Won't work for unsorted array)

'''



def tripleSum(arr, size, sum):
    orginalArrMap = []
    for i in range(size):
        orginalArrMap.append( (arr[i], i) )
    sortedArr = sorted(orginalArrMap, key= lambda item: item[0])
 
    for const in range(size-2):
        targetSum = sum - sortedArr[const][0]
        firstPointer = const + 1
        secondPointer = size - 1
 
        while (firstPointer < secondPointer):
            if (sortedArr[firstPointer][0]+sortedArr[secondPointer][0] == targetSum):
                print(sortedArr[const][1] + 1, sortedArr[firstPointer][1] + 1, sortedArr[secondPointer][1] + 1)
                return
            elif (sortedArr[firstPointer][0] + sortedArr[secondPointer][0] < targetSum):
                firstPointer += 1
            else:
                secondPointer -= 1
    
    print(-1)



# For Testing Purpose
'''

A = [2, 1, 1, 2, 2, 1, 1]
tripleSum(A, len(A), 3)

'''