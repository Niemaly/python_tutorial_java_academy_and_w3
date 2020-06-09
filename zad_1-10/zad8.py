#napisz program, który będzie zwracał czy podana liczba jest parzysta, czy nie

number = int(input("podaj liczbę\n"))

if number % 2 == 0:
    print("liczba jest parzysta")
else:
    print("liczba jest nieparzysta")