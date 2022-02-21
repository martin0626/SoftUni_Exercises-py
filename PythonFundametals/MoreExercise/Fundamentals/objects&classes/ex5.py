class Class:
    __students_count = 22
    students = []
    grades = []
    def __init__(self, name):
        self.name = name
        
    def add_student (self, name, grade):
        self.__students_count -= 1
        if self.__students_count > 0:  
            self.students.append(name)
            self.grades.append(grade)
    def get_average_grade(self):
        return sum(self.grades) / len(self.grades)
    def unp (self):
        return ', '.join(self.students)
    def __repr__ (self):
        return f'The students in {self.name}: {self.unp()}. Average grade: {self.get_average_grade():.2f}'

a_class = Class('11B')
a_class.add_student('Peter', 4.80)
a_class.add_student('George', 6.00)
a_class.add_student('Amy', 3.50)
print(a_class)