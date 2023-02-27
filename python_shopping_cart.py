#-------------------------- MENU -------------------------------------------

menu_sample = """
            PRODUCE LIST

        Orange      -  $0.88
        Lime        -  $0.38
        Lemon       -  $0.68
        Banana      -  $0.25
        Tomato      -  $0.44
        Avocado     -  $0.68
        Onion       -  $0.47
        Cilantro    -  $0.88
"""

#-------------------------- DICTIONARIES AND FUNCTIONS --------------------------------

menu_dict={
    'orange': 0.88, 'lime':0.38, 
    'lemon':0.68, 'banana':0.25, 
    'tomato':0.44, 'avocado':0.68, 
    'onion':0.47, 'cilantro':0.88
    }

def view_cart():
    print("""
    Item          Quantity          Subtotal
        """)
    for key in cart:
        print(f"   {key}           {cart[key]['quantity']}x               ${cart[key]['subtotal']}")
    total2 = sum(total)
    total2 = "%.2f"%total2
    print("\n\n")
    print(f"                               Total: ${total2}")

# cart = {item(orange): item_info}
# item_info = {quantity: 2, subtotal: 1.00}

cart = {}
total = []

def add_price1():
    for key, value in menu_dict.items():
        if item.title() == key.title() :
            subtotal1 = value * quantity
            subtotal1 = "%.2f"%subtotal1
            subtotal1 = float(subtotal1)
            item_info['subtotal'] = subtotal1
            print(f"{quantity}x of {item} has been added to your cart.")
        
def list_subtotal():
    for ke, val in cart.items():
        if ke == item:
            get_this = (val['subtotal'])
            total.append(get_this)
    
def del_item():
    takeout = input('Which item do you want to takeout?').title()
    if cart.get(takeout):
         cart.pop(takeout)
         print("*" * divider)
         print(f"{takeout} has been removed from your cart")

#------------------INPUT SHOPPER'S NAME---------------------------

username = input(f"Please enter shopper's name: ").title()
welcome_message = (f'Hello {username}! Welcome to J-Mart!')
divider = len(welcome_message)
print("*" * divider)
print(welcome_message)

#------------------BEGIN SHOPPING--------------------------------
while True:
        begin_shopping = input(f"Would you like to begin your shopping? Y?N? : ").upper()
        if begin_shopping == 'N':
                print("*" * divider)
                print(f"Sorry to see you go! See you next time!")
                quit()
        elif begin_shopping == 'Y':
                break
        else:
                print("Invalid input. Try again.")

print("*" * divider)

#--------------------- PRINT THE MENU ---------------------------

print(menu_sample)
print("*" * divider)

# #--------------------ADD ITEM IN YOUR CART-----------------------

add_item = True
while add_item:
    
    item = input("Input the item you want to add to your cart.> ").title()
    quantity = int(input(f"How many {item}/s do you want to add to your cart?> "))

    print("*" * divider)

    item_info={}
    cart[item] = item_info
    item_info['quantity'] = quantity
    add_price1()
    list_subtotal()
    
    print("*" * divider)

    add_more = input(f"Would you like to add more? Y/N: ").title()
    
    if add_more == 'N':
        add_item = False
    elif add_more == 'Y':
        continue
    else:
         print("Invalid input. Try again.")
         
#---------------WHAT DO YOU WANT TO DO----------------

wdyw = True
while wdyw:
    print("*" * divider)

    print('What do you want to do?')
    to_do_next = input('Delete items (D) - View cart (V) - Check out (C) or Quit (Q) > ').title()
    print("*" * divider)
    if to_do_next == 'V':
        view_cart()
    elif to_do_next == 'D':
         del_item()
        
    elif to_do_next == 'C':
        wdyw = False
    elif to_do_next == 'Q':
        print(f"Sorry to see you go! Hope to see you again soon!")
        quit()
    else:
         print("Invalid input. Try again.")

# --------------------CHECKOUT------------------------------

print("""
      ********* Bill Summary **********""")

view_cart()

print("""
       ********* Thank You! *********""")
print(f"""  
            See you again soon!""")
