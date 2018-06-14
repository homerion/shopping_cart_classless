from IPython.display import clear_output

def print_help():
    '''
    Clears the cart output then outputs the help menu
    '''
    print('=================')
    print("1. Type 'Help' to bring up this menu.")
    print("2. Type 'Quit' at any time to exit the program.")
    print("3. Type 'Cart' to bring up the cart dialogue.")
    print("=================")

def print_cart(cart):
    print("Your Cart:")
    print("==============")
    if cart == []:
        print('*Is Empty*')
    else:
        for i in range(len(cart)):
            print("{}. {}".format(i+1,cart[i]))

def remove_cart(cart):
    print_cart(cart)
    print('\n\n')
    print("==============")
    print("You can remove an item by typing it's name.")

def delete_item(cart,item):
    while item in cart:
        cart.remove(item)
    print("I removed {} for you.".format(item.title()))

def buy_info(cart):
    print_cart(cart)
    print('\n\n')
    print("==============")
    print("You can add an item by typing it's name, or type 'back'.")

def add_item(cart,item):
    cart.append(item)

def quit(cart):
    clear_output()
    print_cart(cart)
    print('\n\n')
    print("Have a nice day!")

def cart_info():
    print('=================')
    print("1. Type 'Inquire' to find what is in your cart.")
    print("2. Type 'Buy' to add an item to your cart.")
    print("3. Type 'Remove' to delete an item from your cart.")
    print("4. Type 'Back' for the previous screen.")
#     print("0. Type 'Quit' to quit.") <- have this functionallity in but don't say
    print("=================")

cart=[]
while True:
    print_help()
    u_input=input("What do you want to do? ").lower()
    if u_input=='help':
        clear_output()
        print_help()
        continue
    elif u_input=='quit':
        quit(cart)
        break
    elif u_input=='cart':
#         flag=True
        while True:
            clear_output()
            cart_info()
            cart_input=input("What do you want to do? ").lower()
#             if flag:

#                 flag=False
#                 cart_input=input("What do you want to do? ").lower()
            clear_output()
            if cart_input=='inquire':
                print_cart(cart)
                cart_input=input("What do you want to do? ").lower()
                clear_output()

            elif cart_input=='buy':
                while True:
                    buy_info(cart)
                    item_input=input("What do you want to buy? ").lower()
                    if item_input=='back':
                        break
                    else:
                        add_item(cart,item_input.title())
#                         flag=True
                    clear_output()
            elif cart_input=='remove':
                remove_cart(cart)
                if len(cart)<1:
                    print("You don't have anything to delete!")
                    ass=input('Thank about what you did. ')
#                     flag=True
                    clear_output()
                else:
#                     flag=True
                    print(cart)
                    item_sel=input("What do you want to delete? ")
                    if item_sel.title() in cart:
                        delete_item(cart,item_sel.title())

#                     elif
#                         int(item_sel) in range(1,len(cart)+1):
#                         delete_item(cart,cart[int(item_sel)])

                    else:
                        print("I can't delete THAT! ")

            elif cart_input=='back':
                break



        
