class Employee:
    

    def __init__ (self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        
    def fullname(self):
        return (f'{self.first} {self.last}')
    
    def email(self):
        return (f"{self.first}_{self.last}@company.com")



emp_1 = Employee ('Martin' , 'Ivanov', 100000)
emp_2 = Employee ('Test', 'User', 60000)
emp_1.first = 'Ivan'
print (emp_1.first)
print (emp_1.email())
print (emp_1.fullname())