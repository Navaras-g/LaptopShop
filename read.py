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
