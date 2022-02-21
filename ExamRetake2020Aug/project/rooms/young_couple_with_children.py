from project.appliances.fridge import Fridge
from project.appliances.laptop import Laptop
from project.appliances.tv import TV
from project.rooms.room import Room


class YoungCoupleWithChildren(Room):

    def __init__(self, family_name, salary_one, salary_two, *children):
        self.sum_pension = salary_two + salary_one
        super().__init__(family_name, self.sum_pension, 2 + len(children))
        self.children.extend(children)
        self.room_cost = 30
        self.appliances = [TV(), Fridge(), Laptop()] * (2 + len(self.children))
        self.calculate_expenses(*self.appliances, *children)



