class PaymentService:
    def __init__(self):
        self.payments = [] 

    def make_payment(self, user, amount, card_number):
        if len(card_number) != 16 or not all('0' <= c <= '9' for c in card_number):
            print("Invalid card number.")
            return False

        self.payments += [(user, amount)]
        print(f"Payment of ₹{amount} successful for {user.username}.")
        return True
