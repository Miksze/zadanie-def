from re import X
from faker import Faker
class BaseContact:
   def __init__(self, name, surname, phone, email):
       self.name = name
       self.surname = surname
       self.phone = phone
       self.email = email
   def __repr__(self):
       return f"\n\twizytówka:\nimię: {self.name}\nnazwisko: {self.surname}\nTelefon {self.phone}\nemail: {self.email}"

   def contact(self):
       print(f" Wizytówka priv - wybieram numer {self.phone} i dzwonię do {self.name} {self.surname}")
   @property
   def licz(self):
       return f"liczę długość imienia: {self.name} :{len(self.name)}"

#    @licz.setter
#    def licz(self, value):
#         self.__name=value
        # len(self.__name)

class BusinessContact(BaseContact):
   def __init__(self, firm, position, phone2, *args, **kwargs):
       super().__init__(*args, **kwargs)
       self.firm = firm
       self.position = position
       self.phone2 = phone2
   def __repr__(self):
       return f"\n\twizytówka:\nimię: {self.name}\nnazwisko: {self.surname}\nFirma: {self.firm}\nstanowisko: {self.position}\nemail: {self.email}"

       
   def contact(self):
       print(f"Wybieram numer {self.phone2} i dzwonię do {self.name} {self.surname}")

  

card = BaseContact(name="Jacek", surname="Wójcik", phone="+ 48 700 111 222", email="jw@pol.pl")
card2 = BusinessContact( name="Genowefa", surname="Kowalska", phone="111 111 111", email="jjj@ww.po", firm="driver", position="kupiec", phone2="222 222 222" )

BaseContact.contact(card)
BusinessContact.contact(card2)
print(card.licz)
print(card2.licz)

faker = Faker()
x = int(input("jaką ilość wizytówek wygenerować (podaj wartość) : "))
y = int(input("wybierz rodzaj: 1 - BaseContact, 2 - BusinessContact : "))
for i in range(x):
    if y == 2:
      print(BusinessContact( name=faker.first_name(), surname=faker.last_name(), phone=faker.phone_number(), email=faker.email(), firm=faker.company(), position=faker.job(),  phone2=faker.phone_number()))
    else:
      print(BaseContact(name=faker.first_name(), surname=faker.last_name(), phone=faker.phone_number(), email=faker.email()))

#def create_contacts():

200