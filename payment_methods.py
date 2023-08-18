from decimal import Decimal
from payment import Payment


class CreditCardPayment(Payment):
    def pay(self, amount: Decimal):
        print(f"Successfully paid ${amount} to merchant using a Credit Card.")


class GooglePayPayment(Payment):
    def pay(self, amount: Decimal):
        print(f"Successfully paid ${amount} to merchant using Google Pay.")


class PayPalPayment(Payment):
    def pay(self, amount: float):
        print(f"Successfully paid ${amount} to merchant using PayPal.")
