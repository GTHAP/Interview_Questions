# class node:
#    def __init__(self, data):
#        self.data = data
#        self.next = None
#        self.previous = None

# class doublyLL:
#    def __init__(self):
#        self.head = None
#        self.tail = None

def isPalindrome(doublyLLObj):
    start = doublyLLObj.head
    end = doublyLLObj.tail
    while start != end:
        if start.data == end.data:
            start = start.next
            end = end.previous
        else:
            return False
    return True
