# This is my first attempt at creating a frequency array and the counting sort algorithm.
# This is not a good solution.
# Will work on this further.  

def createFrequencyArray(array):
    if len(array) == 0:
        return None
    frequencyArray = []
    for _ in range(max(array) + 1):
        frequencyArray.append(0)
    count = 1
    start = 0
    while start <= len(array) - 1:
        if array[start] not in frequencyArray:
            if frequencyArray[array[start]] == 0:
                frequencyArray[array[start]] = count
            elif frequencyArray[array[start]] > 0:
                frequencyArray[array[start]] += count
        elif array[start] in frequencyArray:
            if frequencyArray[array[start]] == 0:
                frequencyArray[array[start]] = count
            elif frequencyArray[array[start]] > 0:
                frequencyArray[array[start]] += count
        start += 1
    return frequencyArray

def createSortedArray(array):
    frequencyArray = createFrequencyArray(array)
    sortedArray = []
    for i in range(1, len(frequencyArray)):
        number = i
        total = frequencyArray[i]
        for _ in range(0, total):
            sortedArray.append(number)
    return sortedArray
            

array = [1,1,3,2,1,2,9,5]
createFrequencyArray(array)
createSortedArray(array)
