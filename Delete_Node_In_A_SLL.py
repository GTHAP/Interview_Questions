class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

head = ListNode(4)
head.next = ListNode(5)
head.next.next = ListNode(1)
head.next.next.next = ListNode(9)

def deleteNode(node):
    if node.next:
        node.val = node.next.val
        node.next = node.next.next

def printnode(head):
    current = head
    nodelist = []
    while current is not None:
        nodelist.append(current.val)
        current = current.next
        continue
    return nodelist

printnode(head)

deleteNode(head.next)

printnode(head)
