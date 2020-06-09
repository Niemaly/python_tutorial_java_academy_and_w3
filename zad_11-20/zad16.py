run = True
while(run):
    try:
        number1 = int(input("wprowadź pierwszą liczbę\n"))
        number2 = int(input("wprowadź drugą liczbę\n"))

        if number1>number2:
            print(number1)
            run = False
        else:
            print(number2)
            run = False
    except:
        print("wprowadź liczbę całkowitą")
