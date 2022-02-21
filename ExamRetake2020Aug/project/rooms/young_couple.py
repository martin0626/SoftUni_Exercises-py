from project.appliances.fridge import Fridge
from project.appliances.laptop import Laptop
from project.appliances.tv import TV
from project.rooms.room import Room


class YoungCouple(Room):

    def __init__(self, family_name, salary_one, salary_two):
        self.sum_salary = salary_two + salary_one
        super().__init__(family_name, self.sum_salary, 2)
        self.room_cost = 20
        self.appliances = [TV(), TV(), Fridge(), Fridge(), Laptop(), Laptop()]
        self.calculate_expenses(*self.appliances)
