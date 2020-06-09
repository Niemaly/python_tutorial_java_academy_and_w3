#odczytaj wyraz wyświetl jego pierwszą literę

word = input("podaj wyraz\n")
try:
    print(word[0])
except:
    print("nie podałeś wyrazu!!")