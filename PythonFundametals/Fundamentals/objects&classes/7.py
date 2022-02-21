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
        return (f'{self.first} {self.last}')
    
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

class Manager(Employee):
    
    def __init__(self, first, last, pay, employees = None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []

        else:
            self.employees = employees

    def add_emp (self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
    def remove_emp (self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print ('-->', emp.fullname())

mgr_1 = Manager('Sue', 'Smith', 90000, [dev_1])
mgr_1.add_emp(emp_1)

print (mgr_1.email)


mgr_1.print_emps()