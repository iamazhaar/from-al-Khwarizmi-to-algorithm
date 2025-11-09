'''

PROBLEM DESCRIPTION:

    1. Given an array of N integers.
    2. Sort the array in ascending order.

    
THOUGHT PROCESS:

    1. Find the maximum value in the array
    2. Create a count array to store the frequency of each element
    3. Convert the count array into a cumulative (prefix sum) array to determine positions
    4. Place each element in its correct position in the output array using the cumulative counts
    5. After all elements are placed, the array becomes sorted in ascending order

    
ANALYSIS:

    1. Time Complexity: Best = Average = Worst = O(n + k) WHERE
       n = number of elements in the input array &
       k = range of input values
    2. Space Complexity: O(n + k) WHERE 
       n = output array space
       k = count array space
    3. Not In-Place
    4. Stability: Stable

    
NOTES:

    1. The logic will change accordingly if I need to sort in descending order
        -> Convert to cumulative count (from right to left)
        -> Rest of the logic remains same
        -> Algorithm also remains stable
    2. Non-Comparison-Based Sorting Algorithm
    3. Particularly efficient when the range of input values is small compared to the number of elements to be sorted
    4. Suitable for arrays where the range (k) of input values is not significantly larger than the number of elements (n)
    5. Not suitable when k>>n, as it increases memory usage/space complexity
    6. Every value must be a NON-NEGATIVE integer otherwise it's not possible without modification

'''




def countingSort(arr):
    maxElement = max(arr)
    frequencyArr = [0]*(maxElement+1)
    for ele in arr:
        frequencyArr[ele] += 1
    
    for i in range(1, len(frequencyArr)):
        frequencyArr[i] = frequencyArr[i] + frequencyArr[i-1]
    
    sortedArr = [0]*len(arr)
    for i in range(len(arr)-1, -1, -1):
        ele = arr[i]
        frequencyArr[ele] = frequencyArr[ele] - 1
        sortedArr[ frequencyArr[ele] ] = ele
    
    return sortedArr
    


# For Testing Purpose
'''

A = [3, 1, 2, 0, 5, 4]
sortedArr = countingSort(A)
print(sortedArr)

'''