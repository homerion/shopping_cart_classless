from IPython.display import clear_output
def clear():
    clear_output()


class Cart():
    def __init__(self):
        self.items=[]
        self.digits=list('0123456789')

    def add(self,item):
        self.items.append(item)
    def remove(self,item):
        i=''
        flag=False
        for s in item:
            if s in self.digits:
                i.append(s)
                flag = True
            else:
                self.items.remove(item)
                break
        if flag:
            del self.items[int(i)]

    def empty(self):
        if self.items:
            return True
        else:
            return False


class InfoCart(Cart):
    def __init__(self):
        super().__init__()
        self.commands=['Help','Quit','Cart','Buy','List','Remove','Back']
    def print_items(self):
        print("Your Cart:")
        print('====================')
#         if self.empty:
#             print('*Is Empty*')
#         else:
        index=1
        for item in self.items:
            print('{}. {}'.format(index,item))
            index+=1
    def print_shop(self):
        print('\n\n\n')
        print('====================')
        print("Type an item to add it to the cart, or type 'Back'.")
        print('\n')
    def print_removal(self):
        print('\n\n\n')
        print('====================')
        print("Type an item or its number to remove it from the cart, or type 'Back'.")
        print('\n')

def print_main():
    print('You can type any of the following at any time:')
    print('==============================================')
    print("1. Type 'Help' to bring up these options.")
    print("2. Type 'Quit' to end the program.")
    print("3. Type 'Cart' or 'List' to bring up the items in your cart.")
    print("4. Type 'Buy' to add items to your cart.")
    print("5. Type 'Remove' to remove items from your cart.")
    print('==============================================')

def quit(cart):
    print("You would like to buy:")
    print('======================')
    if cart.items == []:
        print('...Nothing.')
        print('\n\n\n')
    else:
        index=1
        for item in cart.items:
            print('{}. {}'.format(index,item))
            index+=1
        print('\n\n')
        print('Have a nice day!')

def shop():
    shopper=InfoCart()
    flag=True
    while True:
        if flag:
            clear()
            print_main()
            u_input=input("What would you like to do? ").title()
        elif u_input=='Back':
            clear()
            print_main()
            u_input=input("What would you like to do? ").title()
        else:
            clear()
        if u_input=="Help":
            clear()
            flag=True
            pass
        elif u_input=="Quit":
            clear()
            quit(shopper)
            break
        elif u_input=="Shop" or u_input=="Buy":
            while True:
                clear()
                shopper.print_items()
                shopper.print_shop()
                u_input=input("What would you like to do? ").title()
                if u_input in shopper.commands:
                    flag=False
                    break
                else:
                    shopper.add(u_input)
        elif u_input=="Cart" or u_input =="List":
            clear()
            shopper.print_items()
            u_input=input("What would you like to do? ").title()
            if u_input not in shopper.commands:
                flag=True
                continue
            else:
                flag=False
        elif u_input=="Remove":
            clear()
            while True:
                clear()
                shopper.print_items()
                shopper.print_removal()
                u_input=input("What would you like to do? ").title()
                if u_input in shopper.commands:
                    flag=True
                    break
                elif u_input in shopper.items:
                    shopper.remove(u_input)

shop()
