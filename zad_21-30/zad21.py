run = True
while run:
    try:
        number = float(input("wprowadź liczbę\n"))
        run = False
        print("odwrotnością tej liczby jest", 1/number)
    except:
        print("podałeś błędne dane")