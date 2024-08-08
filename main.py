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

