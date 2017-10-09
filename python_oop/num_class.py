class Numbers:
    '''Numbers class'''
    MULTIPLIER = 5
    def __init__(self,x,y):
        '''Initating Numbers class with 2 variables'''
        self.x = x
        self.y = y

    @classmethod
    def multiply(cls, a):
        #class method can be called without a class instance
        return a * cls.MULTIPLIER

    @staticmethod
    def subtract(b,c):
        #static method - no access to 'self' or cls'
        # unless you use the full class name
        return b-c

    @property    
    def value(self):
        return (self.x,self.y)

    @value.setter
    def value(self, xy_tuple):
        self.x, self.y = xy_tuple

    @value.deleter
    def value(self):
        del self.x
        del self.y


num = Numbers(3,4)
print(num.value) #property acts like an attribute no need for 'num.value()'
print("Number multiply 'num' instance of class methdod * 4 = {}".format(num.multiply(4)))
print("Number multiply no instance of class method * 8 = {}".format(Numbers.multiply(8)))
print()
print("Number x = {}".format(num.x))
print("Number y = {}".format(num.y))