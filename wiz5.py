

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

    @property
    def label_length(self):
        return len(self.name) + len(self.surname)



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

def create_contacts(card_type="base", n=2):
    cards = []

    for i in range(n):
        if card_type == "base":
            c = BaseContact(name=faker.first_name(), surname=faker.last_name(), phone=faker.phone_number(), email=faker.email())
        else:
            c = BusinessContact( name=faker.first_name(), surname=faker.last_name(), phone=faker.phone_number(), email=faker.email(), firm=faker.company(), position=faker.job(),  phone2=faker.phone_number())
        cards.append(c)
        print(f'Długość imienia i nazwiska w wizytówce : '+ str(c.label_length))
    return cards

faker = Faker("pl_PL")
x = create_contacts()
print(x)

