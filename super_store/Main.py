from models.User import User
from models.Item import Item
from services.ProfileService import ProfileService
from services.InventoryService import InventoryService
from services.OrderService import OrderService
from services.PaymentService import PaymentService
from enums.Role import Role

profile_service = ProfileService()
inventory_service = InventoryService()
payment_service = PaymentService()

# Sample user flow
print("\n--- Register Users ---")
seller = profile_service.register("alice", "password123", Role.SELLER)
buyer = profile_service.register("bob", "securepass", Role.BUYER)

print("\n--- Login Buyer ---")
logged_in_buyer = profile_service.login("bob", "securepass")

print("\n--- Login Seller ---")
logged_in_seller = profile_service.login("alice", "password123")

print("\n--- Seller Adds Items ---")
item1 = Item("101", "Laptop", 50000, 10)
item2 = Item("102", "Mouse", 500, 25)
inventory_service.add_item(logged_in_seller, item1)
inventory_service.add_item(logged_in_seller, item2)

print("\n--- Buyer Lists Items ---")
items = inventory_service.list_items(logged_in_buyer)
for item in items:
    print(f"{item.item_id} - {item.name} - ₹{item.price} - Stock: {item.quantity}")

print("\n--- Buyer Adds to Cart & Buys ---")
order_service = OrderService(inventory_service, logged_in_buyer)
order_service.add_to_cart(item1, 1)
order_service.add_to_cart(item2, 2)
result = order_service.buy_item()
print(result)

if "Total" in result:
    amount = int(result.split(":")[1].strip())
    print("\n--- Buyer Makes Payment ---")
    payment_service.make_payment(logged_in_buyer, amount, "1234567890123456")
