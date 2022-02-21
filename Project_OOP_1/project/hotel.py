class Hotel(object):

    def __init__(self, name):
        self.name = name
        self.rooms = []
        self.guests = 0

    @staticmethod
    def from_stars(stars_count: int):
        name = f'{stars_count} stars Hotel'
        return Hotel(name)

    def add_room(self, room):
        if room not in self.rooms:
            self.rooms.append(room)

    def take_room(self, room_number, people):
        for room in self.rooms:
            if room.number == room_number:
                result = room.get_room(people)
                if not result:
                    self.guests += people

    def free_room(self, room_number):
        for room in self.rooms:
            if room.number == room_number:
                self.guests -= room.guests
                room.free_room()

    def free_rooms(self):
        free_rooms = []
        for room in self.rooms:
            if not room.is_taken:
                free_rooms.append(room.number)
        return f'{", ".join([str(r) for r in free_rooms])}'

    def taken_rooms(self):
        taken_rooms = []
        for room in self.rooms:
            if room.is_taken:
                taken_rooms.append(room.number)
        return f'{", ".join([str(r) for r in taken_rooms])}'

    def print_status(self):
        print(f'Hotel {self.name} has {self.guests} total guests\nFree rooms: {self.free_rooms()}\nTaken rooms: {self.taken_rooms()}')