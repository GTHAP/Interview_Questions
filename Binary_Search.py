# Binary serach will only work on a sorted list/array.
# Binary search iterative solution
# Time complexity - O(log(n)
# Space complexity - O(1)

def binarySearch(array, target):
    start = 0
    end = len(array) - 1 
    if target > array[end]:
        return print("Number is greater")
    if target < array[start]:
        return print("Number is lesser")
    while start <= end:
        middleIndex = (start + end) // 2
        if target == array[middleIndex]:
            return print(middleIndex, "True")
        elif target < array[middleIndex]:
            end = middleIndex - 1 
        elif target > array[middleIndex]:
            start = middleIndex + 1
    return print("False")
    
array = [10,50,52,64,92,101,103,110] 
target = 110
binarysearch(array, target)
