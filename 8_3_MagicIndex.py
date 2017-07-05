# A magic index in an array A[1...n-1] is defined to be an index such that A[i] = i. Given a sorted array of distinct integers, write a 
# method to find a magic index, if one exists, in array A. What if the values are not distinct?

#1 brute force

#2 given that the array is sorted thought, sounds a lot like the classic binary search problem

def magicFast(array):
    return magic(array, 0, len(array)-1)

def magic(array, start, end):
    if end < start: return -1
    mid = (start+end)/2
    if array[mid] == mid:
        return mid
    elif array[mid] > mid:
        return magic(array, start, mid-1)
    else:
        return magic(array, mid+1, end)

#3 not distinct

def magicFast(array):
    return magic(array, 0, len(array)-1)

def magic(array, start, end):
    if end < start: return -1
    mid = (start+end)/2
    midValue = array[mid]
    
    if midValue == mid: return midValue
    
    leftIndex = min(midValue, mid-1)
    left = magic(array, start, leftIndex)
    if left>=0: return left

    rightIndex = max(rightIndex+1, midValue)
    right = magic(array, rightIndex, end)

    return right

