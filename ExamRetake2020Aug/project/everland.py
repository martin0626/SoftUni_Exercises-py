class Everland:

    def __init__(self):
        self.rooms = []

    def add_room(self, room):
        self.rooms.append(room)

    def get_monthly_consumptions(self):
        total = 0
        for room in self.rooms:
            total += room.expenses + room.room_cost
        return f'Monthly consumptions: {total:.2f}$.'

    def population(self):
        return sum([r.members_count for r in self.rooms])

    def pay(self):
        result = ''
        for room in self.rooms:
            pay = room.expenses + room.room_cost
            if room.budget >= pay:
                room.budget -= pay
                result += f'{room.family_name} paid {pay:.2f}$ and have {room.budget:.2f}$ left.\n'

            else:
                result += f"{room.name} does not have enough budget and must leave the hotel.\n"
                self.rooms.remove(room)

        return result[:-1]

    def status(self):
        result = f'Total population: {self.population()}\n'
        for room in self.rooms:
            result += f"{room.family_name} with {room.members_count} members. Budget: {room.budget:.2f}$, Expenses: {room.expenses:.2f}$\n"
            if room.children:
                n = 1
                for child in room.children:
                    result += f"--- Child {n} monthly cost: {child.get_monthly_expense():.2f}$\n"
                    n += 1
            if hasattr(room, 'appliances'):
                result += f"--- Appliances monthly cost: {sum([a.get_monthly_expense() for a in room.appliances]):.2f}$\n"
        return result[:-1]
