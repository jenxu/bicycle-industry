class Bicycle:
    def __init__(self, model, wheel1, wheel2, frame):
        self.model = model
        self.weight = wheel1.weight + wheel2.weight + frame.weight
        self.produce = wheel1.produce + wheel2.produce + frame.produce
        
class Wheel(Bicycle):
    def __init__(self, model, weight, produce, type_of_wheel):
        self.model = model
        self.weight = weight
        self.produce = produce
        self.type_of_wheel = type_of_wheel
        
class Frame(Bicycle):
    def __init__(self, material, weight, produce):
        self.material = material
        self.weight = weight
        self.produce = produce

class BikeShop:
    def __init__(self, name):
        self.name = name
        self.bikes = {}
        self.profit = 0
        
    def add_bike(self, bike, number):
        self.bikes[bike] = number
        
    def sell_bike(self, bike, buyer):
        self.profit += (bike.produce * 0.20)
        self.bikes[bike]-=1
        buyer.budget-=self.cost(bike)

    def bikes_within_budget(self, customer):
        for bike in self.bikes:
            if self.cost(bike) <= customer.budget:
                print(bike.model)
        
    def cost(self, bike):
        return bike.produce * 1.20

    def shop_profit(self):
        return self.profit
        
class Customer:
    def __init__(self, name, budget):
        self.name = name
        self.budget = budget