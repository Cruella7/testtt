class Trade:
    def __init__(self):
        self.salesmen = []
        self.clients = []
        self.orders = []
    def add_order(self, order):
        self.orders.append(order)
class SalesMan:
    def __init__(self, id, name, city, comm, kol):
        self.id = id
        self.name = name
        self.city = city
        self.comm = comm
        self.kol=kol

class Client:
    def __init__(self, id, name, city, rating, salesman_id):
        self.id = id
        self.name = name
        self.city = city
        self.rating = rating
        self.salesman_id = salesman_id
class Order:
    def __init__(self, id, salesman_id, client_id, date, amt):
        pass

class Summa:
    def __int__(self, s_men,s_clients,s_orders):
        self.s_men = s_men
        self.s_clients = s_clients
        self.s_orders = s_orders

# main
globals(i)
s = 0
for SalesMan.id in SalesMan:

print(s)



