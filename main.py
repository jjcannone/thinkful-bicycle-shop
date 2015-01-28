#
#  Basic Requirements
#
#
#
#  Refactor your solution
#  Once you have everything working, refactor your code to make it more modular. You should:
#
#  Create a file named bicycles.py that contains each of your classes.
#  Create a file named main.py that imports those classes, and uses them.
#  Run main.py and make sure your refactored code still works like it did before.
#
#  Good Luck
#
#  We're going to leave you largely on your own to complete this assignment, and we expect that your solution will not be optimal because you're just starting to work with object oriented programming and it takes time to develop an instinctive sense of what makes for good object oriented design. As we said before, think of your solution to this project mainly as a conversation starter for you and your mentor.
#  ======================================================================================
#Extra Challenge
#
#If you found completing the basic requirements fairly straightforward then you should try to extend your code to model the bicycles in more detail.
#
#Alter your classes
#You should add new classes to represent the following bike parts:
#
#Wheels
#Have a model name
#Have a weight
#Have a cost to produce
#There should be a total of three different wheel types
#Frames
#Can be made of aluminum, carbon, or steel
#Have a weight
#Have a cost to produce
#Then you should modify your Bicycle class. The updated class should:
#
#Bicycle
#Be comprised of two wheels of the same type and a frame
#Have a weight equal to the sum of the weight of the frame and two wheels
#Have a cost to produce equal to the sum of the two wheels' and frame's cost to produce
#You may also need to update your testing script to reflect the changes that you have made here.
#
#Extension Exercise
#
#If the extra challenges were not a problem and you're running ahead of schedule then you could try to extend your model even further to add bicycle manufacturers.
#
#Alter your classes
#You should add one or more classes to represent:
#
#Bicycle Manufacturers
#Have a name
#Produce three models of bikes each
#Have a percentage over cost which they sell bikes to bike shops at
#Then you should modify your Bicycle class again. The updated class should:
#
#Bicycle
#Have a manufacturer
#Update your testing script
#The testing script should be modified so that it:
#
#Creates two bicycle manufacturers, which both produce three different bicycle models
#Makes the bike shops stock their inventory by purchasing bikes from manufacturers
#
# ====================================================================
from bicycles import Bicycle, BikeShop, Customer
from random import randint

def list_inventory(shop):
  for bike in shop.inventory:
    print "{}: {} (${:,.2f})".format(bike.model_name, shop.inventory[bike], shop.price[bike]) 
    
if __name__ == '__main__':
  # Set up the bike shop.  Stock 6 models, and surcharge 20%.
  my_shopname = "LoPresti's Bike Shop"
  print 'Welcome to {}...\n'.format(my_shopname)
  shop = BikeShop(my_shopname,0.20)
  
  # Define bicycle models.
  kopriva = Bicycle("Kopriva",5,99)
  ems = Bicycle("Ems",4,249)
  hambright = Bicycle("Hambright",50,799)
  renzi = Bicycle("Renzi",10,119)
  chief = Bicycle("Chief",8,549)
  ram = Bicycle("Ram",7,339)
 
  # Stock the bicycle shop.
  # TO DO: Find a random integer generator and use those values instead.
  shop.stock_bike(kopriva, randint(0,3))
  shop.stock_bike(ems, randint(0,3))
  shop.stock_bike(hambright, randint(0,3))
  shop.stock_bike(renzi, randint(0,3))
  shop.stock_bike(chief, randint(0,3))
  shop.stock_bike(ram, randint(0,3))
  
  # Define customers.
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
  print 'After a busy day of sales at {}...\n'.format(my_shopname)
  print "Our end-of-day inventory (Bicycle: Number Available ($Price)):\n"
  list_inventory(shop)
  print "\nWe made a profit of ${:,.2f}".format(shop.profit)
