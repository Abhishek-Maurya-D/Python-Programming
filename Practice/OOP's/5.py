# Create a class called Order which stores item & its price.
# use Dunder function __gt__() to convey that:
# order1 > order2 if price of order1 > price of order2

class Order:
    def __init__(self, item, price):
        self.item = item
        self.price = price
    
    def __gt__(odr1, odr2):
        return odr1.price >odr2.price

odr1 = Order("Chips", 20)
odr2 = Order("Tea", 15)

print(odr1 > odr2) # true