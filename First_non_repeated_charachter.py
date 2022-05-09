# Time complexity - O(N + M)
# Space complexity - O(N)

def firstNonRepeatingCharachter(string):
    stringList = list(string)
    charachterCount = {}
    for i in stringList:
        charachterCount.update ({ stringList.count(i) : i })
    for i in charachterCount.keys():
        if i == 1:
            return charachterCount.get(i)
    return None

string = "aabbbcaabddc"
firstNonRepeatingCharachter(string)
