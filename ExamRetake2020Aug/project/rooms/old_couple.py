from project.appliances.fridge import Fridge
from project.appliances.stove import Stove
from project.appliances.tv import TV
from project.rooms.room import Room


class OldCouple(Room):

    def __init__(self, family_name, pension_one, pension_two):
        self.sum_pension = pension_two + pension_one
        super().__init__(name=family_name, budget=self.sum_pension, members_count=2)
        self.room_cost = 15
        self.appliances = [TV(), TV(), Fridge(), Fridge(), Stove(), Stove()]
        self.calculate_expenses(*self.appliances)
