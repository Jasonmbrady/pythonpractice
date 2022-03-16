from cart import Cart

class User:
    def __init__(self, data):
        self.f_name = data['f_name']
        self.l_name = data['l_name']
        self.email = data['email']
        self.balance = data['balance']
        self.cart = Cart()
        
    def add_to_cart(self, item):
        self.cart.add_item(item)
        print("New total of all goods in cart: $" + self.cart.total)
        return self

    def remove_from_cart(self, item_name):
        self.cart.remove_item(item_name)
        print("New total of all goods in cart: $" + self.cart.total)
        return self
    
    def add_funds(self, amount):
        self.balance += amount
        print("Your new balance of funds is $" + self.balance)
        return self

    def checkout(self):
        if self.balance >= self.cart.total:
            self.balance -= self.cart.total
            print("You have just bought:")
            for item in self.cart.in_cart:
                print(f'{item.name} for ${item.price}')
            print(f'A total of ${self.cart.total} has been deducted from your balance.')
            print ("Your current remaining balance is $" + self.balance)
            self.cart.in_cart = []
            self.cart.total = 0
        else:
            print("You don't have enough funds!")
        return self