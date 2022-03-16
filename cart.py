class Cart:
    def __init__(self):
        self.total = 0
        self.in_cart = []
    
    def add_item(self, item):
        self.total += item.price
        self.in_cart.append(item)

    def remove_item(self, item_name):
        for item in self.in_cart:
            if item.name == item_name:
                self.total -= item.price
                item = self.in_cart[len(self.in_cart - 1)]
                self.in_cart.pop()

                