def ordernote(laptopname, distributorname, companyname, purchasedatetime, netamount):
    
    '''

    Generates an order note/invoice for a laptop purchase and saves it to a text file.

    The function writes the order note to a file and does not return any value.
        
    '''
    


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



def salenote(laptopname, companyname, customername, purchasedatetime, totalamount, shippingcost):

    '''

    Generates an sale note/invoice for a laptop sold and saves it to a text file.

    The function writes the sale note to a file and does not return any value.
        
    '''
    
    

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


     #Updating the stock.txt file with updated values and displaying it to the user:
        
        file = open("stock.txt", "w")

        for name, details in laptopinfo.items():
            file.write(f"{name},{details['company']},{details['price']},{details['quantity']},{details['processor']},{details['graphics']}\n")

        file.close()

        
