run = True
while(run):
    try:
        number1 = int(input("wprowadź pierwszą liczbę\n"))
        number2 = int(input("wprowadź drugą liczbę\n"))
        number3 = int(input("wprowadź trzecią liczbę\n"))

        list = [number1, number2, number3]
        list.sort()
        print("największa liczba to:", list[-1])
        run = False

    except:
        print("wprowadź liczbę całkowitą")
