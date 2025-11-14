'''

PROBLEM DESCRIPTION:

    1. Given a 0-indexed integer array nums, find a peak element, and return its index
    2. If the array contains multiple peaks, return the index to any of the peaks
    3. You may imagine that nums[-1] = nums[n] = -∞
    4. In other words, an element is always considered to be strictly greater than a neighbor that is outside the array


DEFINITION OF PEAK:

    -> A peak element is an element that is strictly greater than its neighbors


THOUGHT PROCESS OF BRUTE FORCE:

    1. I can simply traverse the array and check for each element whether it is the peak
    2. Must handel the edge cases properly because what if the 0 or n-1 index is my answer
    3. If it is RETURN index


ANALYSIS:

    1. Time Complexity: O(n)
    2. Space Complexity: O(1)

'''


def findPeakIndex(nums):
    n = len(nums)
    for i in range(n):
        if ((i==0 or nums[i]>nums[i-1])
            and (i==n-1 or nums[i]>nums[i+1])):
            return i



'''

THOUGHT PROCESS OF EFFICIENT SOLUTION:

    1. As I've kind of a sorted array & I'm looking for some element -> Think of Binary Search
    2. Before writing the actual modification of BS, I'll handel the edge cases
    3. Edge Cases -> If there's only 1 element, that's my peak
                  -> If A[i] > A[i+1], first element is my peak
                  -> If A[n-1] > A[n-2], last element is my peak
    For these edge cases I don't even need to perform BS -> Simple If statement before doing BS
    4. After handeling the edge cases, I'will do BS between index 1 to n-2
    5. low = 1, high = n-2 (As I've already handeled the first and last element before)


ANALYSIS:

    1. Time Complexity: O(log n)
    2. Space Complexity: O(1)

'''



def findPeak(nums):
    n = len(nums)
    if (n==1 or nums[0] > nums[1]):
        return 0
    elif (nums[n-1]> nums[n-2]):
        return n-1
    else:
        low = 1
        high = n-2

        while (low <= high):
            mid = (low+high)//2
            if ((nums[mid]>nums[mid-1]) and (nums[mid]>nums[mid+1])):
                return mid
            elif (nums[mid] > nums[mid-1]):
                low = mid + 1
            else:
                high = mid - 1



# For Testing Purpose
# '''

A = [1, 2, 3, 4, 5, 2, 1]
peakIndex = findPeak(A)
print(peakIndex)

# '''