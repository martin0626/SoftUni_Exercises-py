class Employee:


    def __init__ (self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        print (self.first, self.last)

    def rich(self):
        if self.pay > 60000:
            print (self.first, self.last, 'is a rich boy')


emp_1 = Employee ('Martin' , 'Ivanov', 100000)
emp_2 = Employee ('Test', 'User', 60000)
print (emp_1.first, emp_1.last, 'Payment:' ,emp_1.pay)
emp_1.rich()
emp_2.rich()
print (emp_1.fullname())