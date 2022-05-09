# Time complexity - O(N + M)
# Space complexity - O(1)

def findMultipleDuplicates(array):
    countTable = {}
    for i in array:
        countTable.update({ i : array.count(i) })
    duplicates = [key for key, value in countTable.items() if value > 1]
    return duplicates

array = [1,3,2,2,1,9,0,1,2,2,7,10]
findMultipleDuplicates(array)
