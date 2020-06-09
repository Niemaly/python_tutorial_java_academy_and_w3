import math
run = True
while(run):
    try:
        number1 = int(input("wprowadź pierwszą liczbę\n"))
        number2 = int(input("wprowadź drugą liczbę\n"))

        print(number1 ,"podniesiona do potęgi", number2 , "=  " ,math.pow(number1, number2))
        run = False
    except:
        print("Niewłaściwe dane")
