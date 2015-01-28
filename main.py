from bicycles import Bicycle, BikeShop, Customer, Frame, Wheel, Manufacturer
from random import randint

def list_inventory(shop):
  for bike in shop.inventory:
    print "{}: {} (${:,.2f})".format(bike.model_name, shop.inventory[bike], shop.price[bike]) 
    
if __name__ == '__main__':
  # Set up the bike shop.  Stock 6 models, and surcharge 20%.
  shop = BikeShop("LoPresti's Bike Shop",0.20)
  print 'Welcome to {}...\n'.format(shop.shop_name)
  
  # Define bike manufacturers.  Each to make three models of bike.
  # Each to apply a surcharge that is passed to the bike shop.
  jbc = Manufacturer("Johnstown Bike Company",0.10)
  rbw = Manufacturer("Richland Bike Works", 0.15)
  
  # Define wheel types.
  jabba = Wheel("Jabba",80,37) # obligatory Star Wars reference
  brock = Wheel("Brock",55,47) # tough-as-nails hockey player for Johnstown Chiefs
  grady = Wheel("Grady",40,57) # high-school friend
  
  # Define frame models.
  flyer = Frame("Flyer","carbon",15,250)
  mondo = Frame("Mondo","steel",30,390)
  reynolds = Frame("Reynolds","aluminum",20,175) # common brand of Al foil
  
  # Define bicycle models.
  # Sub shops:  Kopriva (sadly, long gone) and Em's (still open in Johnstown, PA)
  # Gym teachers:  Hambright (boys) and Renzi (girls) -- high school
  # Mascots:  Chief (ECHL Johnstown Chiefs) and Ram (Richland HS)
  kopriva = Bicycle("Kopriva",flyer,brock,jbc)
  ems = Bicycle("Ems",flyer,grady,jbc)
  hambright = Bicycle("Hambright",mondo,jabba,rbw)
  renzi = Bicycle("Renzi",reynolds,jabba,rbw)
  chief = Bicycle("Chief",reynolds,brock,jbc)
  ram = Bicycle("Ram",mondo,grady,rbw)
  
  # Stock the bicycle shop. (0-3 facilitates testing of short-stock situations.)
  shop.stock_bike(kopriva, randint(0,3))
  shop.stock_bike(ems, randint(0,3))
  shop.stock_bike(hambright, randint(0,3))
  shop.stock_bike(renzi, randint(0,3))
  shop.stock_bike(chief, randint(0,3))
  shop.stock_bike(ram, randint(0,3))
  
  # Define customers. Three friends from high school.
  david = Customer("David",200)
  doug = Customer("Doug",500)
  bryan = Customer("Bryan",1000)

  # Print the initial inventory of the bike shop for each bike it carries.
  print "\nOur current inventory (Bicycle: Number Available ($Price)):\n"
  list_inventory(shop)

  # Print the name of each customer, and a list of the bikes offered by
  # the bike shop that they can afford given their budget. Make sure you
  # price the bikes in such a way that each customer can afford at least
  # one.
  print "\nToday's customers (and their budgets) are:"
  for customer in [ david, doug, bryan ]:
    print "\n{} (${}) can afford:".format(customer.name, customer.fund)
    for bike in shop.inventory:
      if ( shop.price[bike] <= customer.fund ) and ( shop.inventory[bike] > 0 ):
        print "The {} (${:,.2f}) ({} available)".format(bike.model_name, 
                                                   shop.price[bike],
                                                   shop.inventory[bike]
                                                  )
        customer.options.append(bike)

  # Have each of the three customers purchase a bike then print the name of the
  # bike the customer purchased, the cost, and how much money they have left over
  # in their bicycle fund.
  print '\nLet\'s get these fine people some bikes!\n'
  for customer in [ david, doug, bryan ]: 
    if len(customer.options) > 0:
      print "Customer {}, {} option{}...".format(customer.name, len(customer.options),
                                                 "s" if len(customer.options) > 1 else "")
      buy_bike = customer.options[randint(0,1000) % len(customer.options)]
      customer.purchase(shop,buy_bike)
      shop.process_purchase(buy_bike)
      print "{} gets the {} for ${:,.2f}, and has ${:,.2f} left.\n".format(customer.name,
                                                                         buy_bike.model_name,
                                                                         shop.price[buy_bike],
                                                                         customer.fund)
    else:
      print "No luck for Customer {} -- we're out of bikes in that price range.".format(customer.name)
      print "Please come back soon, {}.  We get new stock every week.\n".format(customer.name)

  # After each customer has purchased their bike, the script should print out the
  # bicycle shop's remaining inventory for each bike, and how much profit they have
  # made selling the three bikes.
  print 'After a busy day of sales at {}...\n'.format(shop.shop_name)
  print "Our end-of-day inventory (Bicycle: Number Available ($Price)):\n"
  list_inventory(shop)
  print "\nWe made a profit of ${:,.2f}".format(shop.profit)
