from enums.Role import Role
from models.User import User

class InventoryService:
    def __init__(self):
        self.items = []

    def add_item(self, user, item):
        if user.role != Role.SELLER:
            print("Only sellers can add items.")
            return False
        
        self.items += [item]
        print("Item added successfully.")
        return True

    def update_item(self, user, item_id, quantity):
        if user.role != Role.SELLER:
            print("Only sellers can update items.")
            return False

        for item in self.items:
            if item.item_id == item_id:
                item.quantity = quantity
                print("Item updated successfully.")
                return True

        print("Item not found.")
        return False

    def list_items(self, user):
        if user.role not in [Role.SELLER, Role.BUYER]:
            print("Unauthorized access to item listing.")
            return []

        return self.items

    