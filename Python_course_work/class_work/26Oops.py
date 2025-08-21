'''
class ststus:
    def __init__(self,name,in_contact=True):
        self.name = name
        self.in_contact = in_contact

    def add_image(self,pic):
        self.pic = pic
        print(f'{self.pic} is added to status')
'''


from abc import ABC, abstractmethod

class Order (ABC):
    @abstractmethod
    def process_order (self):
        pass

class FoodOrder (Order):
    def process_order (self):
        print("Processing Food Order: Check chef availability, estimate time, a")

class GroceryOrder (Order):
    def process_order (self):
        print("Processing Grocery Order: Check inventory per item, bag & dispat")

class MedicineOrder (Order):
    def process_order (self):
        print("Processing Medicine Order: Validate prescription, assign secure")

