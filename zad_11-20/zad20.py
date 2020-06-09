import math
run = True
while(run):
    try:
        number1 = float(input("wprowadź długość pierwszej przyprostokątnej\n"))
        number2 = float(input("wprowadź długość drugiej przyprostokątnej\n"))

        number3 = math.sqrt(number1*number1+number2*number2)

        print("długość przeciwprostkątnej wynosi: ", number3)
        run = False
    except:
        print("Niewłaściwe dane")
