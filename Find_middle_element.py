# Find the middle element of a Singly Linked List in one pass
# Time complexity - O(N)
# Space complexity - O(1)

# Singly Linked List class definition
# class SLL:
#    def __init__(self, value):
#        self.value = value
#        self.next = next

def findMiddle(sllObject):
    current1 = sllObject
    current2 = sllObject
    if current1 is not None:
        while current1 is not None and current1.next is not None:
            current1 = current1.next.next
            current2 = current2.next
    return current2.value
