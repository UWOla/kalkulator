from pakiet_calc.calculator import *
import pyfiglet

if __name__ == "__main__":

    baner = pyfiglet.figlet_format("Kalkulator")
    print(baner)

    while True:
        wybor = (input("Wybierz opcję:\nd - dodawanie\no - odejmowanie\nm - mnożenie\nz - dzielenie\np - potęga^2\n--> "))
        if wybor == "d":
            dodawanie()
        elif wybor == "o":
            odejmowanie()
        elif wybor == "m":
            mnozenie()
        elif wybor == "z":
            dzielenie()
        elif wybor == "p":
            potega()
        else :
            print("Nie ma takiej możliwości!")