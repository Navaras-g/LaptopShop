print("\n")
print("*****************************************************************************************************************************************")
print("*****************************************************************************************************************************************")
print("*** \t\t\t\t\t\t         WELCOME TO THE TECH   \t\t\t\t\t\t\t      ***")
print("*** \t\t\t\t\t\t             INVENTORY         \t\t\t\t\t\t\t      ***")
print("*****************************************************************************************************************************************")
print("*****************************************************************************************************************************************") 
print("\n")
print("Tech Inventory is the ultimate destination for people wanting to buy their favorite laptops, at the best value for their money.")
print("Take a look at our stock! :")
print("\n")


#Importing and Accessing the datetime module of python

import datetime


def readfile(filename):
    
    '''

    Reads the laptop information from a file and stores it in the empty dictionary.

    It returns dictionary containing laptop information, where the keys are laptop names
    and the values are attributes like company, price, quantity,
    processor, and graphics for each laptop.
    
    '''

    laptopinfo = {}
    read = open(filename, "r")
    lines = read.readlines()
    read.close()

    for i in lines:
        items = i.strip().split(",")
        laptopname = items[0]
        company = items[1]
        price = items[2]
        quantity = int(items[3])
        processor = items[4]
        graphics = items[5]
        laptopinfo[laptopname] = {
            "company": company,
            "price": price,
            "quantity": quantity,
            "processor": processor,
            "graphics": graphics
        }

    return laptopinfo



def display(laptopinfo):
    
    '''

    This function takes laptopinfo(name of the dictionary) as parameter and prints
    all its information on the user's screen.
    It loops through the dictionary to display values.

    '''
    
    print("*****************************************************************************************************************************************")
    print("| S.N. |    Laptop Name       |      Company Name    |    Price     |     Quantity     |       Processor      |        Graphics         |")
    print("*****************************************************************************************************************************************")

    l = 1
    for name, details in laptopinfo.items():
          print(f"   {l:<4}  {name:<21}  {details['company']:<21}  {details['price']:<13}  {details['quantity']:<19} {details['processor']:<22} {details['graphics']:<23}| ")
          l=l+1
    print("*****************************************************************************************************************************************")

    

#Running the readfile function that reads the text file and stores it in a dictionary, then running function to display the data:

laptopinfo = readfile("stock.txt")
    
display(laptopinfo)
    


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

    # Opening the text file and writing the order note/invoice:
    
    file = open(f"{distributorname}_Order.txt", "w")
    file.write("===================== Order Bill =========================\n")
    file.write(f"Name of the laptop: {laptopname}\n")
    file.write(f"Name of the distributor: {distributorname}\n")
    file.write(f"Name of the company: {companyname}\n")
    file.write(f"Purchase Date and Time: {purchasedatetime_str}\n")
    file.write("----------------------------------------------------------\n")
    file.write(f"Net Amount: ${netamount:.2f}\n")
    file.write(f"VAT Amount: ${vatamount:.2f}\n")
    file.write("----------------------------------------------------------\n")
    file.write(f"Amount after VAT: ${amountaftervat:.2f}\n")
    file.write("----------------------------------------------------------\n")
    file.write("Thank you for your order!\n")
    file.write("==========================================================\n")
    file.close()



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
    

    # Write the sales note to a file
    
    file = open(f"{laptopname}_Sell.txt", "w")
    file.write("====================== Sales Bill ========================\n")
    file.write(f"Name of the Laptop Sold: {laptopname}\n")
    file.write(f"Company Name: {companyname}\n")
    file.write(f"Customer Name: {customername}\n")
    file.write(f"Purchase Date and Time: {purchasedatetime_str}\n")
    file.write("----------------------------------------------------------\n")
    file.write(f"Total Amount (without shipping): ${totalamount:.2f}\n")
    file.write(f"Shipping Cost: ${shippingcost:.2f}\n")
    file.write("----------------------------------------------------------\n")
    file.write(f"Total Amount (with shipping): ${amountaftershipping:.2f}\n")
    file.write("----------------------------------------------------------\n")
    file.write("Thank you for your purchase!\n")
    file.write("==========================================================\n")
    file.close()



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





#Main block of code where user is asked to choose between order, sell or termination of program.

def mainloop():
    
    '''

    This function is the main entry point where the program loops until and unless the user is satisfied with buying or
    selling the laptops.
    The program asks the user to input 1,2 or 3 in order to buy, sell or exit respectively. Entering 1 calls order function, 2 calls
    sell function and 3 terminates the loop using "break" statement and ends the program.

    The stock is updated based on what user chooses to do, and displayed on the screen.
    
    '''
    
    ask = True
    while ask:
        
        yeet = input("Would you like to make a purchase or sell a laptop? (Type '1' to order laptop, '2' to sell laptop and '3' to exit): ")

        
        if yeet == "1":
            order(laptopinfo)
            
        elif yeet == "2":
            sell(laptopinfo)
            
        elif yeet == "3":
            print("\n")
            print("*****************************************************************************************************************************************")
            print("\t\t\t\t\t Thank you for the transaction! Please do remember us again!")
            print("*****************************************************************************************************************************************")
            break
        else:
            print("Invalid input. Please enter '1', '2' or '3'.")
            continue


        #Updating the stock.txt file with updated values and displaying it to the user:
        
        file = open("stock.txt", "w")

        for name, details in laptopinfo.items():
            file.write(f"{name},{details['company']},{details['price']},{details['quantity']},{details['processor']},{details['graphics']}\n")

        file.close()

        display(laptopinfo)


mainloop()
