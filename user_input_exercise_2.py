# Exercise 2 shopping cart program

# items
print(f"Welcome to Lance Shopping Store!\n\n"
      f"This are what we selling:\n"
      f"Item\t\t\tPrice\n"
      f"Milk\t\t\t20.0 pesos\n"
      f"Egg\t\t\t\t11.0 pesos\n"
      f"Hotdog\t\t\t9.0 pesos\n"
      f"Soap Powder\t\t8.0 pesos\n")

selected_item = input("What item you want Mr./Mrs.? ")

if selected_item == "Milk":
    price = 20.0
elif selected_item == "Egg":
    price = 11.0
elif selected_item == "Hotdog":
    price = 9.0
elif selected_item == "Soap Powder":
    price = 8.0
else:
    print("Please select items only mentioned above.")
    exit(0)


quantity = input(f"\nYou have selected {selected_item},"
                       f" how many you want? ")

total_price = float(quantity) * price

payment = float(input(f"\nYou selected item {selected_item} which has a price {price} pesos\n"
                            f"The total price you bought is {total_price}\n"
                            f"Please pay {total_price}\n"))

if payment >= total_price:
    change = payment - total_price
    print(f"\nThanks for buying in Lance Shopping Store!\n"
          f"Here is your {quantity} {selected_item} and here is your change {change} pesos.\n\n"
          f"** You have received {quantity} {selected_item} and change {change} pesos. **")
else:
    print("Please pay the total price exact or above the price!")
    exit(0)


