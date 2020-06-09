run = True
while(run):

    try:
        name = input("wprowadź imię\n")

        if name.isdecimal() or len(name)<3:
            raise Exception

        if name == "Barnaba":
            print("imię jest męskie")
        elif name[-1] =='a':
            print("imię jest żeńskie")
        else:
            print("imię jest męskie")
        
        run = False

    except:
        print("błędne dane")