'''

PROBLEM DESCRIPTION:

1. You have a SORTED DATASET (Won't work for UNSORTED DATASET)
2. You have an integer as KEY
3. You have to locate the POSITION of the KEY in the given DATASET
4. RETURN the POSITION


THOUGHT PROCESS:

1. As I've a SORTED DATASET I find two MID-INDEX(mid1, mid2) first
2. Check whether the KEY is in the mid1 or mid2 INDEX (If it is return the POSITION)
3. If not then the KEY is either in the LEFTMOST SEGMENT, RIGHTMOST SEGMENT, MIDDLE SEGMENT
4. Suppose the dataset is sorted in ASCENDING order and If KEY < 1st MID element then KEY must be in the LEFTMOST SEGMENT -> update the RIGHT pointer
5. If KEY > 2nd MID element then KEY must be in the RIGHTMOST SEGMENT -> update the LEFT pointer
6. Otherwise KEY is in the MIDDLE SEGMENT -> update the LEFT & RIGHT pointer


NOTES:
1. The logic will be changed accordingly if the DATASET is sorted in DESCENDING order
2. This algorithm can also be written in a recursive manner however both have the same TC
3. Quaternary Search and Higher Order Searching Algorithm are not popular because they are inefficient in real-world scenarios
4. Inefficient because though they split the dataset into many parts in each iteration but increase the number of comparisons per iteration
5. Consequently, each iteration becomes slower

'''


# Ternary Search Algorithm -> TC = O(log N), SC = O(1)  [Base of Logarithm = 3]

def ternarySearch(dataset, key):
    left = 0
    right = len(dataset) - 1

    while (left <= right):
        mid1 = left + ((right - left) // 3)
        mid2 = right - ((right - left) // 3)

        if (dataset[mid1] == key):
            return mid1
        if (dataset[mid2] == key):
            return mid2
        
        if (key < dataset[mid1]):
            right = mid1 - 1
        elif (key > dataset[mid2]):
            left = mid2 + 1
        else:
            left = mid1 + 1
            right = mid2 - 1

    return -1



# For Testing Purpose
'''

arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 8.5, 9, 9.9, 10]
result = ternarySearch(arr, 9.9)
print(result)

'''