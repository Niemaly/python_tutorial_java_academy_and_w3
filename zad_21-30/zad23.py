pi = 3.14
run = True
while run:
    try:
        r = float(input("wprowadź promień koła"))
        x = pi * r*r
        print("pole koła wynosi", x)
        run=False
    except:
        print("podałeś błędne dane")