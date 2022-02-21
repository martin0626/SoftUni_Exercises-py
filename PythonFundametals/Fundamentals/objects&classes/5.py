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
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday (day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True



emp_1 = Employee ('Martin' , 'Ivanov', 100000)
emp_2 = Employee ('Test', 'User', 60000)
emp_str_1 = 'John-Doe-70000'
new_emp_1 = Employee.from_string(emp_str_1)

import datetime
my_date = datetime.date(2020, 7, 11)

print (Employee.is_workday(my_date))