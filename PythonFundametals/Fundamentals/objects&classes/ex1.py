class Storage:
    storage = []
    def __init__ (self, capacity):
        self.capacity = capacity

    def add_product (self, product):
        if len(Storage.storage) < self.capacity:
            Storage.storage.append(product)

    def get_products (self):
        return Storage.storage

store = Storage(4)
store.add_product('apple')
store.add_product('banana')
store.add_product('potato')
store.add_product('tomato')
store.add_product('bread')
print(store.get_products())

