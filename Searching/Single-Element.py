'''

PROBLEM DESCRIPTION:

1. You have a SORTED ARRAY
2. All the elements appear EXACTLY TWICE except ONE element
3. Your task is to find that ONE SINGLE element


THOUGHT PROCESS:

1. Let's take an example to develop the idea, A = [1, 1, 2, 2, 3, 3, 4, 5, 5, 6, 6]
                                                   E  O  E  O  E  O  E  O  E  O  E

2. If I'm standing on an element where A[i] != A[i+1] && A[i] != A[i-1] then A[i] is the SINGLE element -> RETURN A[i]
3. If I'm standing on an EVEN index and the next element is the same as the element in EVEN index -> the single element in on the RIGHT HALF -> So, eliminate the LEFT HALF
4. If I'm standing on an ODD index and the next element is the same as the element in ODD index -> the single element in on the LEFT HALF -> So, eliminate the RIGHT HALF

'''



def singleElement(arr, n):
    if (n == 1):
        return arr[0]
    if (arr[0] != arr[1]):
        return arr[0]
    if (arr[n-1] != arr[n-2]):
        return arr[n-1]
    
    low = 0
    high = n - 1
    while (low <= high):
        mid = (low+high)//2
        if (arr[mid] != arr[mid+1] and arr[mid] != arr[mid-1]):
            return arr[mid]
        elif ( (mid % 2 == 0 and arr[mid] == arr[mid+1]) or (mid % 2 == 1 and arr[mid] == arr[mid-1]) ):
            low = mid + 1
        else:
            high = mid - 1



# For Testing Purpose
'''

A = [1, 1, 2, 3, 3, 4, 4, 5, 5, 6, 6]
single = singleElement(A, len(A))
print(single)

'''