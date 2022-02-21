class Catalogue:
    products = []
    def __init__ (self, name):
        self.name = name
        
    def add_product (self, product):
        self.products.append(product)
        
    
    def get_by_letter(self, first_letter):
        chosen_products = [x for x in self.products if x[0] == first_letter]
        return chosen_products
    def unp (self):
        return '\n'.join(sorted(self.products))
    
    def __str__ (self):
        return f'Items in the {self.name} catalogue:\n{self.unp()}'
    

catalogue = Catalogue('Furniture')
catalogue.add_product('Sofa')
catalogue.add_product('Mirror')
catalogue.add_product('Desk')
catalogue.add_product('Chair')
catalogue.add_product('Carpet')
print(catalogue.get_by_letter('C'))
print(catalogue)