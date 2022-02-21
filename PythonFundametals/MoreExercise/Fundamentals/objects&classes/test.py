class Employee:
    num = 0
    position = "Labourer"
    def __init__(self, first, last, time ):
        self.first = first
        self.last = last
        self.time = time
         
        Employee.num += 1


    def emp_info(self):
        return (f'{self.first} {self.last} - {Employee.position}')

class Manager(Employee):
    
    def __init__(self, first, last, time):
        Employee.__init__(self, first, last, time)
        
    def position_mgr (self):
        Employee.position = 'Manager'
class Merchandaiser(Employee):
    def __init__(self, first, last, time):
        Employee.__init__(self, first, last, time)
        
    def position_mrc (self):
        Employee.position = 'Merchandaiser'


emp_1 = Employee('Martin', 'Ivanov', 10)
emp_2 = Employee('Marin', 'Iridiz', 1)
emp_3 = Employee('Gosho', 'Lazarov', 3)
emp_4 = Employee('Alexander', 'Gerorgiev', 4)

mgr_1 = Manager('Ivan', 'Ivanov', 9)
mgr_2 = Manager('Ivan', 'Ivanov', 12)
mgr_3 = Manager('Ivan', 'Ivanov', 9)
mgr_4 = Manager('Ivan', 'Ivanov', 13)

print(emp_1.emp_info())
print(emp_2.emp_info())
print(emp_3.emp_info())
print(emp_4.emp_info())

mgr_1.position_mgr()
print (mgr_1.emp_info())
print (mgr_2.emp_info())
print (mgr_3.emp_info())
print (mgr_4.emp_info())


mrc_1 = Merchandaiser('Martin', 'Ivanov', 10)
mrc_2 = Merchandaiser('Marin', 'Iridiz', 1)
mrc_3 = Merchandaiser('Gosho', 'Lazarov', 3)
mrc_4 = Merchandaiser('Alexander', 'Gerorgiev', 4)
mrc_1.position_mrc()
print (mrc_1.emp_info())
print (mrc_2.emp_info())
print (mrc_3.emp_info())
print (mrc_4.emp_info())




#if type(mgr_1) is Manager:
    #mgr_1.position_mgr()
    #print (mgr_1.emp_info())

