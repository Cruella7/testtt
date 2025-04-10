import pickle

class Order:
    def __init__(self, order_id: int, manager_id: int, client_id: int, order_date: str, amount: float):
        self.order_id = order_id
        self.manager_id = manager_id
        self.client_id = client_id
        self.order_date = order_date
        self.amount = amount

    def __str__(self):
        return f"{self.order_id}. {self.manager_id} {self.client_id} {self.order_date} {self.amount:.2f}"

if __name__ == '__main__':
    orders = []

    with open("sofa.txt", "rb") as orders_f:
        orders = pickle.load(orders_f)

    sorted_orders = sorted(orders, key=lambda x: x.amount, reverse=True)

    with open("sortsofa.txt", "wb") as orders_sorted_f:
        pickle.dump(sorted_orders, orders_sorted_f)

    print("Orders done")