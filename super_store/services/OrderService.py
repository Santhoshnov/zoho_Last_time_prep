from enums.Role import Role
from models.User import User

class OrderService:
    def __init__(self, inventory_service, user):
        self.inventory_service = inventory_service
        self.user = user
        self.cart_items = [] 

    def add_to_cart(self, item, quantity):
        if self.user.role != Role.BUYER:
            print("Only buyers can add to cart.")
            return False
        
        self.cart_items += [(item, quantity)]
        print("Item added to cart.")
        return True

    def buy_item(self):
        if self.user.role != Role.BUYER:
            print("Only buyers can place orders.")
            return "Unauthorized"

        total = 0
        for cart_item_pair in self.cart_items:
            cart_item = cart_item_pair[0]
            qty = cart_item_pair[1]

            found = False
            for inv_item in self.inventory_service.items:
                if inv_item.item_id == cart_item.item_id and inv_item.quantity >= qty:
                    inv_item.quantity -= qty
                    total += inv_item.price * qty
                    found = True
                    break

            if not found:
                return "Order Failed: Item not available or insufficient stock"
        
        self.cart_items = [] 
        return "Order Placed. Total: " + str(total)
