class Bicycle(object):
  def __init__(self, model_name, frame, wheel):
    self.model_name = model_name
    self.frame = frame
    self.wheel = wheel
    self.cost = frame.cost + ( 2 * wheel.cost )
    self.weight = frame.weight + ( 2 * wheel.weight )

class BikeShop(object):
  def __init__(self, shop_name, margin):
    self.shop_name = shop_name
    self.margin = margin
    self.inventory = {}
    self.price = {}
    self.profit = 0
  
  def stock_bike(self, bike, count):
    self.inventory[bike] = count
    self.price[bike] = ( bike.cost * 1 + self.margin )
    return self.inventory[bike], self.price[bike]

  def process_purchase(self, bike):
    self.inventory[bike] -= 1
    return self.calculate_profit(bike.cost), self.inventory[bike]
  
  def calculate_profit(self,cost):
    self.profit += cost * self.margin
    return self.profit

class Customer(object):
  def __init__(self, name, fund):
    self.name = name # Have a name
    self.fund = fund # Have a fund of money to buy a bike
    self.options = [] # which bikes are under budget and available

  def purchase(self,shop,model):
    self.fund -= ( model.cost * 1 + shop.margin )
    return self.fund

class Wheel(object):
  def __init__(self,name,weight,cost):
    self.name = name # Have a model name
    self.weight = weight # Have a weight
    self.cost = cost # Have a cost to produce

class Frame(object):
  def __init__(self,name,material,weight,cost):
    self.name = name
    self.material = material # Can be made of aluminum, carbon, or steel
    self.weight = weight # Have a weight
    self.cost = cost # Have a cost to produce
