# This is a design question.
# This is not a good piece of code for a vending machine. 
# Think of this as initial rough work to get your brain warmed up. 
# Much more ellaborate designs are availbale online. 

class VendingMachine:
    def __init__(self):
        self.itemAndQuantity = {}
        self.itemAndPrice = {}
    def fillMachine(self, item, quantity, price):
        self.item = item
        self.quantity = quantity
        self.price = price
        self.itemAndPrice.update({ self.item : self.price })
        self.itemAndQuantity.update({ self.item : self.quantity })
    def getPrice(self, item):
        self.item = item
        for i, j in self.itemAndPrice.items():
            if i:
                return j
            else:
                return "Error"
    def getItem(self, item, payment):
        self.item = item
        self.payment = payment
        for i, j in self.itemAndPrice.items():
            if i:
                if j == self.payment:
                    break
                else:
                    return "Error"
            else:
                return "Error"
        for i, j in self.itemAndQuantity.items():
            if i:
                if j > 0:
                    self.quantity -= 1
                    return self.item
            else:
                return "Error"
