class SchoolMember:
    '''Represents any school member.'''

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('(Initialized SchoolMember: {})'.format(self.name))

    def tell(self):
        '''Tell the details'''
        print('Name: "{}" Age: "{}"'.format(self.name, self.age), end = " ")

class Teacher(SchoolMember):
    '''Represents a teacher..subclass'''
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print('(Initialized Teacher: {})'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Salary: "{:d}"'.format(self.salary))

class Student(SchoolMember):
    '''Represents a student...subclass'''
    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print('(Initialized Student: {})'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Marks: "{}'.format(self.marks))

t = Teacher('Ms. Goodall', 75, 45000)
s = Student('Swoop', 22, 65)

print()

members = [t, s]
for member in members:
    member.tell()


'''
Special Note!!!
Since we are defining a __init__ method in Teacher and Student subclasses, 
Python does not automatically call the constructor of the base class SchoolMember, 
you have to explicitly call it yourself!
In contrast, if we have not defined an __init__ method in a subclass, Python will 
call the constructor of the base class automatically.'''