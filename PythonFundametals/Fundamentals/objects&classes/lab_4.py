class Zoo:
    number = 0

    def __init__ (self, name):
        self.name = name
        self.mammals = []
        self.fishes = []
        self.birds = []
    
    def add_animals (self, spices, name):
        if spices == 'mammal':
            self.mammals.append(name)
        elif spices == 'fish':
            self.fishes.append(name)
        elif spices == 'bird':
            self.birds.append(name)
        Zoo.number += 1
    def get_info (self, spices):
        result = ''
        if spices == 'mammal':
            result += f'Mammals in {self.name}: {", ".join(self.mammals)}\n'
        elif spices == 'fish':
            result += f'Fishes: {", ".join(self.fishes)}\n'
        elif spices == 'bird':
            result += f'Birds: {", ".join(self.birds)}\n'
        result += f'Total animals: {Zoo.number}'

        return result
zoo_name = input()      
zoo = Zoo(zoo_name)
count = int(input())

for n in range (count):
    spiece, animal = input().split()
    zoo.add_animals(spiece, animal)

spice_needed = input()
print (zoo.get_info(spice_needed))
