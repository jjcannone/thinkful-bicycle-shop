class Bicycle(object):
  def __init__(self, model_name, weight, cost):
    self.model_name = model_name # Have a model name
    self.weight = weight # Have a weight
    self.cost = cost # Have a cost to produce

class BikeShop(object):
  def __init__(self, shop_name, margin):
    self.shop_name = shop_name # Have a name
    self.margin = margin # Sell bicycles with a margin over their cost
    self.inventory = {}
    self.price = {}
    self.profit = 0
  
  def stock_bike(self, bike, count):
    self.inventory[bike] = count
    self.price[bike] = ( bike.cost * 1 + self.margin )

  def process_purchase(self, bike):
    self.calculate_profit(bike.cost)
    self.inventory[bike] -= 1
  
  def calculate_profit(self,cost):
    self.profit += cost * self.margin

class Customer(object):
  def __init__(self, name, fund):
    self.name = name # Have a name
    self.fund = fund # Have a fund of money to buy a bike
    self.options = [] # which bikes are under budget and available

  def purchase(self,shop,model):
    self.fund -= ( model.cost * 1 + shop.margin )
