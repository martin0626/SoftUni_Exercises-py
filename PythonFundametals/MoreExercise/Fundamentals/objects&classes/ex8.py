class Vehicle:
    def __init__ (self, type, model, price, owner = None):
        self.type = type
        self.model = model
        self.price = price
        self.owner = owner
    def buy (self, money, owner):
        if self.price <= money and self.owner == None:
            return f'Successfully bought a {self.type}. Change: {(money - self.price):.2f}'
            self.owner = owner 
        elif self.price > money:
            return 'Sorry, not enough money'
        elif self.owner != None:
            return 'Car already sold'

    def sell(self):
        if self.owner == None:
            return 'Vehicle has no owner'
        else:
            self.owner = None
    def __repr__(self):
        if self.owner != None:
            return f'{self.model} {self.type} is owned by: {self.owner}'
        else:
            return f'{self.model} {self.type} is on sale: {self.price}'

vehicle_type = "car"
model = "BMW"
price = 30000
vehicle = Vehicle(vehicle_type, model, price)
vehicle.buy(15000, "Peter")
vehicle.buy(35000, "George")
print(vehicle)
vehicle.sell()
print(vehicle)


