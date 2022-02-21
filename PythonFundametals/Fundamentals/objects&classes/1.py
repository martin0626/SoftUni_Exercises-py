class Person :

    def __init__ (self, n, g, a):
        self.name = n
        self.gender = g
        self.age = a


    def talk(self):
        print ('Hi I am', self.name)

    def vote (self):
        if self.age < 18:
            print ('I am not eligiable to vote')
        else:
            print ('I am eligiable to vote')

obj1 = Person ('Sam', 'Male', 22)
obj2 = Person ('Jesse', 'Female', 16)
obj1.vote()
obj1.talk()

obj2.vote()
obj2.talk()