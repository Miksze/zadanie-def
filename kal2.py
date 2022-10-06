

import logging



def add(a, b):
    logging.warning(f"Dodaję {a} i {b}")
    return a + b

def sub(a, b): 
    logging.warning(f"Odejmuję {a} i {b}")
    return a - b

def inc(a, b):
    logging.warning(f"Mnożę {a} i {b}")
    return a * b

def div(a, b):
    logging.warning(f"Dzielenie {a} i {b}")
    return a / b


def get_data():
    operation = input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: ")
    
        
    
    a = float(input("Podaj pierwszą wartość : "))
    b = float(input("Podaj drugą wartość : "))
    return operation, a, b

operation = {"1": add, "2": sub, "3": inc, "4": div}


def kalk():

    op, a, b = get_data()



    result = operation[op](a, b)
    print("Wynik to:", result)

if __name__ == "__main__":
    print('__name__ = ', __name__)
    


    kalk()