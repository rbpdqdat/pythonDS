import datetime # we will use this for date objects

class Person:

    def __init__(self, name, surname, birthdate, address, telephone, email):
        self.name = name
        self.surname = surname
        self.birthdate = birthdate

        self.address = address
        self.telephone = telephone
        self.email = email
        #self.age = today.year - self.birthdate.year
        self._age = None
        self.age_last_recalculated = None

        self.recalculate_age()

    def recalculate_age(self):
        today = datetime.date.today()
        self._age = 5
        self.age_last_recalculated = today 

    def age(self):    
        print('Age = {}'.format(self._age))  
        if (datetime.date.today() > self.age_last_recalculated):
            self.recalculate_age()
            print('Recalculated Age: {}!'.format(self._age))
        else:
            print('No need to recalculate: {} Age value is current.'.format(self._age))
        return self._age


stan = Person('Stan','Schmidt','1/4/1942','Cotton St','555-555-5555','t@s.com')

print('dir(stan) {}'.format(dir(stan)))
print('dir(Person) {}'.format(dir(Person)))
print('__str__(stan) {}'.format(str(stan)))
print('str(stan) {}'.format(str(stan)))
print('type(stan) {}'.format(type(stan)))
print('type(Person) {}'.format(type(Person)))
