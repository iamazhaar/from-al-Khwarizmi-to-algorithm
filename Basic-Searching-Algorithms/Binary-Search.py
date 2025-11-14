'''

PROBLEM DESCRIPTION:

    1. You have a SORTED DATASET (Won't work for UNSORTED DATASET)
    2. You have an integer as KEY
    3. You have to locate the POSITION of the KEY in the given DATASET
    4. RETURN the POSITION


THOUGHT PROCESS:

    1. As I've a SORTED DATASET I find the MID-INDEX first
    2. Check wheter the KEY is in the MID-INDEX (If it is return the POSITION)
    3. If not then the KEY must appeared before the MID or after the MID
    4. Suppose the dataset is sorted in ASCENDING order and if KEY > MID-ELEMENT then KEY is located after the MID -> fix LEFT pointer
    5. And if KEY < MID-ELEMENT then KEY is located before the MID -> fix RIGHT pointer
    6. So initialize LEFT,RIGHT,POSITION

    
ANALYSIS:

    1. Time Complexity: Best = O(1), Average = Worst = O(log N)
    2. Space Complexity: O(1) (in-place)


NOTES:

    1. The logic will be changed accordingly if the DATASET is sorted in DESCENDING order
    2. This algorithm can also be written in a recursive manner however both have the same TC

'''



def binarySearch(dataset, key):
    left = 0
    right = len(dataset) - 1

    while (left <= right):
        mid = (left + right)//2

        if (dataset[mid] == key):
            return mid
        elif (key > dataset[mid]):
            left = mid + 1
        else:
            right = mid - 1
    
    return -1



# For Testing Purpose
'''

arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 8.5, 9, 9.9, 10]
result = binarySearch(arr, 8.5)
print(result)

'''