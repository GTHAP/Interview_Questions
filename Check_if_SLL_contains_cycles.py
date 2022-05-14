# Check if Singly Linked List contains cycles.
# Time complexity - O(N)
# Space complexity - O(N)

# Singly Linked List class definition.
# class SLL:
#    def __init__(self, value):
#        self.value = value
#        self.next = next

def checkForCycle(sllObject):
    current1 = sllObject
    addressList = []
    while current1 is not None:
        if current1 not in addressList:
            addressList.append(current1)
        else:
            return True, current1, current1.value
    return False
