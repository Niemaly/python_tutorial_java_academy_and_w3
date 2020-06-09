run = True
while(run):
    try:
        number1 = int(input("wprowadź pierwszą liczbę\n"))
        number2 = int(input("wprowadź drugą liczbę\n"))

        print((number2+number1)/2)
        run = False
    except:
        print("Niewłaściwe dane")
