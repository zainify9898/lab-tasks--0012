
class CashPayment:
    def pay(self):
        print("Cash payment")

class CardPayment:
    def pay(self):
        print("Card payment")

c1 = CashPayment()
c2 = CardPayment()

payment_list = [c1, c2]

for i in payment_list:
    i.pay()
