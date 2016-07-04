from bicycles import Bicycle
from bicycles import Wheel
from bicycles import Frame
from bicycles import BikeShop
from bicycles import Customer
        
if __name__ == '__main__':
    Wheelies = BikeShop("Wheelies")
    
    wheel1 = Wheel("brand1", 12, 20, "BMX")
    wheel2 = Wheel("brand2", 18, 100, "Mountain")
    wheel3 = Wheel("brand3", 24, 250, "Racing")
    
    frame1 = Frame("Aluminum", 34, 45)
    frame2 = Frame("Carbon", 41, 250)
    frame3 = Frame("Steel", 50, 345)
    
    
    Merida = Bicycle("Merida", wheel1, wheel1, frame1)
    Trek = Bicycle("Trek", wheel1, wheel1, frame2)
    Cannondale = Bicycle("Cannondale", wheel2, wheel2, frame1)
    Kona = Bicycle("Kona", wheel2, wheel2, frame3)
    Scott = Bicycle("Scott", wheel3, wheel3, frame1)
    Marin = Bicycle("Marin", wheel3, wheel3, frame2)
    
    Wheelies.add_bike(Merida, 12)
    Wheelies.add_bike(Trek, 15)
    Wheelies.add_bike(Cannondale, 20)
    Wheelies.add_bike(Kona, 25)
    Wheelies.add_bike(Scott, 18)
    Wheelies.add_bike(Marin,10)
    
    print("Initial inventory for Wheelies Corporation: ")
    for bike in Wheelies.bikes:
        print("{}:  {}".format(bike.model, Wheelies.bikes[bike]))
    
    
    customer1 = Customer("Natasha", 200)
    customer2 = Customer("Katie", 500)
    customer3 = Customer("Caroline", 1000)
    
    print("\nHi {}, these are the bikes that are within your budget: ".format(customer1.name))
    Wheelies.bikes_within_budget(customer1)
    
    print("\nHi {}, these are the bikes that are within your budget: ".format(customer2.name))
    Wheelies.bikes_within_budget(customer2)
    
    print("\nHi {}, these are the bikes that are within your budget: ".format(customer3.name))
    Wheelies.bikes_within_budget(customer3)
    
    for bike in Wheelies.bikes:
        if Wheelies.cost(bike) <= customer1.budget:
            Wheelies.sell_bike(bike, customer1)
            print("\n{} just purchased a {} which costed {}. {} now has {} left over in their bicycle fund.".format(customer1.name, bike.model, Wheelies.cost(bike), customer1.name, customer1.budget))
            break
        
    for bike in Wheelies.bikes:
        if Wheelies.cost(bike) <= customer2.budget:
            Wheelies.sell_bike(bike, customer2)
            print("\n{} just purchased a {} which costed {}. {} now has {} left over in their bicycle fund.".format(customer2.name, bike.model, Wheelies.cost(bike), customer2.name, customer2.budget))
            break
        
    for bike in Wheelies.bikes:
        if Wheelies.cost(bike) <= customer3.budget:
            Wheelies.sell_bike(bike, customer3)
            print("\n{} just purchased a {} which costed {}. {} now has {} left over in their bicycle fund.".format(customer3.name, bike.model, Wheelies.cost(bike), customer3.name, customer3.budget))
            break
    
  
    print("Updated inventory for Wheelies Corporation:")
    for bike in Wheelies.bikes:
        print("{}:  {}".format(bike.model, Wheelies.bikes[bike]))

    print("The total profit made by the Wheelies Corporation is: {}".format(Wheelies.profit))