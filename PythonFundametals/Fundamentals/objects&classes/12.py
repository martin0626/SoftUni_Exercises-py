class Employee:
    

    def __init__ (self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
    @property   
    def fullname(self):
        return (f'{self.first} {self.last}')
    @property
    def email(self):
        return (f"{self.first}_{self.last}@company.com")
    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print ('Delete Name!')
        self.first = None
        self.last = None



emp_1 = Employee ('Martin' , 'Ivanov', 100000)
emp_2 = Employee ('Test', 'User', 60000)

print (emp_1.first)
print (emp_1.email)
print (emp_1.fullname)
del emp_1.fullname