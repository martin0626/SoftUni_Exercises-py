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
emp_1 = Employee('Martin', 'Ivanov', 5000)
emp_2 = Employee('Corey', 'Schafer', 50000)

print (emp_1.pay)
print (Employee.raise_amount, '*', emp_1.pay)
emp_1.apply_raise()
print (emp_1.pay)
print (Employee.num_of_emp)