class Employee:
    

    def __init__ (self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return (f'{self.first} {self.last}')

    

    def __repr__(self):
        return "Employee('{}', '{}', '{}')".format(self.first, self.last, self.pay)
        #return (f'({self.first}, {self.last}, {self.pay})')
    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email)
        #return (f'{self.fullname()} - {self.email}')

emp_1 = Employee ('Martin' , 'Ivanov', 100000)
emp_2 = Employee ('Test', 'User', 60000)

print (emp_1)

#print (repr(emp_1))
#print (str(emp_1))

