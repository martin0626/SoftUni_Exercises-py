class Employee:
    

    def __init__ (self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return (f'{self.first} {self.last}')

    def rich(self):
        if self.pay > 60000:
            print (self.first, self.last, 'is a rich boy')

    def __add__ (self, other):
        return self.pay + other.pay
    def __len__(self):
        return len(self.fullname())


emp_1 = Employee ('Martin' , 'Ivanov', 100000)
emp_2 = Employee ('Test', 'User', 60000)

print (emp_1 + emp_2)
print (len(emp_1))