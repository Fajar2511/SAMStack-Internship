from abc import ABC, abstractmethod 

class PaymentGateway(ABC): 
    @abstractmethod
    def process_payment(self, amount): 
        pass

class StripeGateway(PaymentGateway):  
    def process_payment(self, amount):  
        print(f"Processing ${amount} via Stripe")  
class PayPalGateway(PaymentGateway):  # P capital
    def process_payment(self, amount):
        print(f"Processing ${amount} via PayPal")
def checkout(gateway_obj, amount):  
    gateway_obj.process_payment(amount)  

stripe = StripeGateway()
paypal = PayPalGateway()
checkout(stripe, 100)
checkout(paypal, 200)