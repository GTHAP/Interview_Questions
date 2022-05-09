# This is just an example of how to deal with coding interview questions. 
# This is a simple question and can be approached in multiple ways. 

# A simple function to get the smallest number. No sorting or Min/Max function/algorithm used. 
# Time Complexity - O(N^2)
# Space Complexity - O(1)

def smallestNumber(numberList):
    start = 0
    next = 1
    smallest = 0
    while next <= len(numberList) - 1:
        if numberList[start] < numberList[next]:
            smallest = numberList[start]
            next += 1
        elif numberList[start] > numberList[next]:
            smallest = numberList[next]
            start += 1
        else:
            next += 1
    return smallest
    
numberList = [9,3,2,4,6,6,7,8,100,101,99]
print(smallestNumber(numberList))

# Optimized solution. 
# Time Complexity - O(N)
# Space Complexity - O(1)

def smallestNumber(numberList):
    start = 1
    smallest = 0
    if numberList[0] < numberList[start]:
        smallest = numberList[0]
    if numberList[start] < numberList[0]:
        smallest = numberList[start]
    while start <= len(numberList) - 1:
        if numberList[start] < smallest:
            smallest = numberList[start]
        start += 1
    return smallest
    
numberList = [9,3,2,4,6,6,7,8,100,101,99]
print(smallestNumber(numberList))
