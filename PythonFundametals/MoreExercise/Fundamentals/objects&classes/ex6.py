class Inventory:
    items = []
    def __init__ (self, capacity):
        self.__capacity = capacity

    def add_item(self, item):
        if self.__capacity > 0:
            self.items.append(item)
            self.__capacity -= 1
        else:
            return ('not enough room in the inventory')
    def get_capacity(self):
        return len(self.items)
    def unp (self):
        return ', '.join(self.items)
    def __repr__ (self):
        return f'Items: {self.unp()}.\nCapacity left: {self.__capacity}'
inventory = Inventory(2)
inventory.add_item('potion')
inventory.add_item('sword')
print(inventory.add_item('bottle'))
print(inventory.get_capacity())
print(inventory)
