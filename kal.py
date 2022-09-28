dzialanie = int(input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: "))

if dzialanie > 4:
    print("źle wybrane działanie")
    pass
else:
    x = float(input("Podaj pierwszą wartość "))
    y = float(input("Podaj drugą wartość "))

#dzialanie = 1
    import logging
    logging.basicConfig(level=logging.DEBUG)

    def kal():
    
        if dzialanie == 1:
            wynik = x + y
            logging.info("dodaję %g i %g" % (x, y))
            print("Wynik to %g" % wynik)
        elif dzialanie == 2:
            wynik = x - y
            print("Wynik to %g" % wynik)
        elif dzialanie == 3:
            wynik = x * y
    

            print("Wynik to %g" % wynik)
        elif dzialanie == 4:
            wynik = x / y
            print("Wynik to %g" % wynik)
    
    kal()