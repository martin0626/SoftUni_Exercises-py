class Employee:
    raise_amount = 1.04
    num_of_emp = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@acompany.com'
        Employee.num_of_emp += 1

    def fullname (self):
        print (self.first, self.last)
    
    def apply_raise (self):
        self.pay = int(self.pay * Employee.raise_amount)
        #OR self.pay = int(self.pay * self.raise_amount)

class Developer(Employee):
    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        #OR Employee.__init__(self, first, last, pay)
        
        self.prog_lang = prog_lang


emp_1 = Employee('Martin', 'Ivanov', 5000)
emp_2 = Employee('Corey', 'Schafer', 50000)

dev_1 = Developer('Martoo', 'Golemiq', 3000, 'Python')
dev_2 = Developer('Ivan', 'Drago', 2000, 'Java')

print (dev_1.email)
print (dev_1.prog_lang)