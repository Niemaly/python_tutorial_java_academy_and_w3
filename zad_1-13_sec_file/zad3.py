run = True
while run:
    try:
        number = int(input("wprowadź liczbę\n"))
        print(100*number)
        run = False
    except:
        print("niepoprawne dane")