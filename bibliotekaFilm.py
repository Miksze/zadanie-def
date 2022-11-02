
class Biblioteka:
   def __init__(self, tytul, rok, gatunek, odtworzenia):
       self.tytul = tytul
       self.rok = rok
       self.gatunek = gatunek
       self.odtworzenia = odtworzenia
   def info(self):
       print(f" {self.tytul} ({self.rok})")
   
   

class BibliotekaSeriale(Biblioteka):
   def __init__(self, numer_odcinka, numer_sezonu,*args, **kwargs):
       super().__init__(*args, **kwargs)
       self.numer_odcinka = numer_odcinka
       self.numer_sezonu = numer_sezonu
   def info(self):
       print(f" {self.tytul} S{self.numer_sezonu}E{self.numer_odcinka}")

baza = [ Biblioteka( tytul="Top Gun", rok="2022", gatunek="akcja", odtworzenia=""),
         BibliotekaSeriale( tytul="Star Trek", rok="1990", gatunek="sf", numer_odcinka="5", numer_sezonu="2", odtworzenia="")
       ]

def get_movies():
    film = []
    for i in baza:
        if i.numer_sezonu == 0:
          film.append(i)
    return film

def get_series():
    serial = []
    for i in baza:
        if i.numer_sezon >= 1:
            serial.append(i)
    return serial

def search(tytul):
    for i in baza:
        if i.tytul == tytul:
            return i

# def generate_views():
#     x = random.choice(baza)
#     x = random.randint(1, 100)
#     return x

print(baza)
