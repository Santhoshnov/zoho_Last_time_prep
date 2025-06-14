# ─── enums/Role.py ───
from enum import Enum

class Role(Enum):
    BUYER = "BUYER"
    SELLER = "SELLER"

# ─── models/User.py ───
class User:
    def __init__(self, username: str, password: str, role: Role):
        self.__username = username
        self.__password = self.__encrypt(password)
        self.__role = role

    def __encrypt(self, password: str) -> str:
        return ''.join([chr((ord(c) + 3) % 256) for c in password])

    def is_valid_password(self, password_input: str) -> bool:
        return self.__encrypt(password_input) == self.__password

    @property
    def username(self):
        return self.__username

    @property
    def role(self):
        return self.__role

# ─── models/Item.py ───
class Item:
    def __init__(self, item_id: str, name: str, price: float, quantity: int):
        self.__item_id = item_id
        self.__name = name
        self.__price = price
        self.__quantity = quantity

    @property
    def item_id(self):
        return self.__item_id

    @property
    def name(self):
        return self.__name

    @property
    def price(self):
        return self.__price

    @property
    def quantity(self):
        return self.__quantity

    def reduce_stock(self, amount: int):
        if amount > self.__quantity:
            raise ValueError("Not enough stock")
        self.__quantity -= amount

# ─── services/ProfileService.py ───
class ProfileService:
    def __init__(self):
        self.__users = []

    def register(self, username: str, password: str, role: Role):
        if any(user.username == username for user in self.__users):
            print("User already exists")
            return None
        user = User(username, password, role)
        self.__users.append(user)
        print("User registered successfully")
        return user

    def login(self, username: str, password: str):
        for user in self.__users:
            if user.username == username and user.is_valid_password(password):
                print("Login successful")
                return user
        print("Invalid credentials")
        return None

# ─── services/InventoryService.py ───
class InventoryService:
    def __init__(self):
        self.__items = []

    def add_item(self, user: User, item: Item):
        if user.role != Role.SELLER:
            print("Only sellers can add items.")
            return False
        self.__items.append(item)
        print("Item added successfully.")
        return True

    def list_items(self):
        return list(self.__items)

# ─── services/OrderService.py ───
class OrderService:
    def __init__(self, user: User, inventory_service: InventoryService):
        self.__user = user
        self.__inventory_service = inventory_service
        self.__cart = []

    def add_to_cart(self, item_id: str, quantity: int):
        if self.__user.role != Role.BUYER:
            print("Only buyers can add to cart.")
            return False

        item = next((i for i in self.__inventory_service.list_items() if i.item_id == item_id), None)
        if item and item.quantity >= quantity:
            self.__cart.append((item, quantity))
            print("Item added to cart.")
            return True
        print("Item not available or insufficient quantity.")
        return False

    def checkout(self):
        total = 0
        for item, qty in self.__cart:
            item.reduce_stock(qty)
            total += item.price * qty
        self.__cart.clear()
        return total

# ─── services/PaymentService.py ───
class PaymentService:
    def __init__(self):
        self.__transactions = []

    def make_payment(self, user: User, amount: float, card_number: str) -> bool:
        if len(card_number) != 16 or not card_number.isdigit():
            print("Invalid card number.")
            return False
        self.__transactions.append((user.username, amount))
        print(f"Payment of ₹{amount} successful for {user.username}")
        return True

# ─── main.py ───
# Imports would normally come from files/modules
# For this inline version, all above classes are assumed defined already

profile_service = ProfileService()
inventory_service = InventoryService()
payment_service = PaymentService()

print("\n--- Register Users ---")
seller = profile_service.register("alice", "password123", Role.SELLER)
buyer = profile_service.register("bob", "securepass", Role.BUYER)

print("\n--- Login ---")
logged_in_buyer = profile_service.login("bob", "securepass")
logged_in_seller = profile_service.login("alice", "password123")

print("\n--- Seller Adds Items ---")
inventory_service.add_item(logged_in_seller, Item("101", "Laptop", 50000, 10))
inventory_service.add_item(logged_in_seller, Item("102", "Mouse", 500, 25))

print("\n--- Buyer Views Items ---")
items = inventory_service.list_items()
for item in items:
    print(f"{item.item_id} - {item.name} - ₹{item.price} - Stock: {item.quantity}")

print("\n--- Buyer Adds to Cart & Checkout ---")
order_service = OrderService(logged_in_buyer, inventory_service)
order_service.add_to_cart("101", 1)
order_service.add_to_cart("102", 2)
total = order_service.checkout()
print(f"Order placed. Total: ₹{total}")

print("\n--- Buyer Makes Payment ---")
payment_service.make_payment(logged_in_buyer, total, "1234567890123456")
