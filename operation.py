def ordernote(laptopname, distributorname, companyname, purchasedatetime, netamount):
    
    '''

    Generates an order note/invoice for a laptop purchase and saves it to a text file.

    The function writes the order note to a file and does not return any value.
        
    '''
    
    # Formatting the purchasedatetime to a string, and calculating amount after VAT:
    
    purchasedatetime_str = purchasedatetime.strftime("%Y-%m-%d %H:%M:%S")
    
    vatrate = 0.13
    vatamount = netamount * vatrate
    amountaftervat = netamount + vatamount


def order(laptopinfo):
    
    '''
    Places an order for a laptop from the given stock and generates an order note.

    This function prompts the user to provide the laptopname, distributorname, and desired quantity. It
    then calculates the amount based on the laptop's price and quantity and generates an invoice.
    The invoice contains the current date and time.
    It also updates the quantity in the stock after the order is placed.
    '''
    
    loop = True
    while loop:
        try:
            laptopname = input("Please input the name of the laptop you want to order: ")
            distributorname = input("Please input the name of the distributor: ")

            if distributorname == '':
                print("Distributor name cannot be empty. Please re-enter the name:")
                continue

            if laptopname in laptopinfo:
                # To prohibit user to enter negative number
                num = True
                while num:
                    quantity = int(input("Please input the amount you want to order: "))
                    if quantity > 0:
                        break
                    else:
                        print("Invalid quantity. Please enter a positive number.")
                
                netamount = quantity * float(laptopinfo[laptopname]['price'])
                purchasedatetime = datetime.datetime.now()

                # Calling ordernote function
                ordernote(laptopname, distributorname, laptopinfo[laptopname]['company'], purchasedatetime, netamount)

                # Updating the quantity of the sold laptop in the dictionary
                laptopinfo[laptopname]['quantity'] = laptopinfo[laptopname]['quantity'] + quantity
                
                 # Reading the order note file and printing its content
                with open(f"{distributorname}_Order.txt", "r") as file:
                    text = file.read()
                print(f"Your Order details are given below:\n{text}")

                print("*****************************************************************************************************************************************")
                print(f"{quantity} {laptopname} laptop(s) ordered from {distributorname} for ${netamount:.2f}. VAT will be added to the bill.")
                print("Stock has been updated with the latest quantity.")
                print("*****************************************************************************************************************************************")
                print("\n")
                break
            else:
                print("Please enter a valid laptop name.")
                continue
        except Exception:
            print("An error occurred. Please try again.")
            continue



def salenote(laptopname, companyname, customername, purchasedatetime, totalamount, shippingcost):

    '''

    Generates an sale note/invoice for a laptop sold and saves it to a text file.

    The function writes the sale note to a file and does not return any value.
        
    '''
    
    # Formatting purchasedatetime to a string, and calculating amount after shipping cost
    
    purchasedatetime_str = purchasedatetime.strftime("%Y-%m-%d %H:%M:%S")
    
    amountaftershipping = totalamount + shippingcost


def sell(laptopinfo):
    
    '''
    This function initiates the selling process of a laptop to a customer and generates a bill.

    This function prompts the user to provide the customername, laptopname, and desired quantity. It
    then calculates the amount based on the laptop's price and quantity, adds shipping cost,
    and generates an invoice. The invoice will also contain the proper date and time.
    It also updates the quantity in the stock after the laptop is sold to a customer.
    '''

    sales = True
    while sales:
        
        try:
            laptopname = input("Please input the name of the laptop you wish to sell: ")

            if laptopname in laptopinfo:
                
                while True:
                    quantity = int(input("Please enter the quantity of laptop you want to sell: "))
                    if quantity > 0:
                        break
                    else:
                        print("Invalid quantity. Please enter a positive number.")

                if quantity <= laptopinfo[laptopname]['quantity']:
                    shippingcost = 50
                    totalamount = quantity * float(laptopinfo[laptopname]['price'])
                    customername = input("Please enter the name of the customer: ")
                    purchasedatetime = datetime.datetime.now()

                    # Calling salenote function
                    salenote(laptopname, laptopinfo[laptopname]['company'], customername, purchasedatetime, totalamount, shippingcost)

                    # Updating the quantity of the sold laptop in the laptops dictionary
                    laptopinfo[laptopname]['quantity'] = laptopinfo[laptopname]['quantity'] - quantity

                     # Reading the sales note file and printing its content
                    with open(f"{laptopname}_Sell.txt", "r") as file:
                        text = file.read()
                    print(f"Your Sales details are given below:\n{text}")

                    print("*****************************************************************************************************************************************")
                    print(f"{quantity} {laptopname} laptop(s) has been sold to {customername} for ${totalamount + shippingcost:.2f}. Thank you for your purchase!")
                    print("Stock has been updated with the latest quantity.")
                    print("*****************************************************************************************************************************************")
                    print("\n")
                    break
                else:
                    print("Please enter a valid quantity.")
                    continue
            else:
                print("Please input a valid laptop name.")
                continue
        except ValueError:
            print("Invalid input! Please enter a valid quantity data (integer).")
            continue
