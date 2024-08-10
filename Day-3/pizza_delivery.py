print("Welcome to Sanjeev Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
small_pizza = 150
medium_pizza = 250
large_pizza = 350
if size == "S":
   pepperoni = input("Do you want pepperoni to serve? Y or N: ")
   if pepperoni == "Y":
      bill = small_pizza + 20
      extra_cheese = input("Do you want extra cheese? Y or N: ")
      if extra_cheese == "Y":
         bill += 15
      else:
         bill += 0   
   else:
      bill = small_pizza

elif size == "M":
   pepperoni = input("Do you want pepperoni to serve? Y or N: ")
   if pepperoni == "Y":
      bill = medium_pizza + 30
      extra_cheese = input("Do you want extra cheese? Y or N: ")
      if extra_cheese == "Y":
         bill += 20
      else:
         bill += 0   

elif size == "L":
   pepperoni = input("Do you want pepperoni to serve? Y or N: ")
   if pepperoni == "Y":
      bill = large_pizza + 40
      extra_cheese = input("Do you want extra cheese? Y or N: ")
      if extra_cheese == "Y":
         bill += 25
      else:
         bill += 0
else:
   print("Invalid size. Please choose S, M or L.")


print(f"Your final bill is {bill}Rs")
   
