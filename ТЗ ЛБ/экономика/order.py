class Order:
    """
    Класс о данных заказа
    """
    def __init__(self, order_id: int, manager_id: int, client_id: int, order_date: str, amount: float):
        """
        Атрибуты класса:

        идентификатор заказа
        идентификатор менеджера
        идентификатор клиента
        дата заказа
        сумма заказа
        """
        self.order_id = order_id
        self.manager_id = manager_id
        self.client_id = client_id
        self.order_date = order_date
        self.amount = amount
    def __str__(self):
        """
        Метод для получения информации о заказе в строковом формате
        """
        return f"{self.order_id}. {self.manager_id} {self.client_id} {self.order_date} {self.amount:.2f}"

def rd_orders(filename):
    orders = []

    """
    Чтение данных из файла и создание объектов Order
    """
    with open("order.txt", "r", encoding="ansi") as orders_f:
        for line in orders_f:
            order_id, manager_id, cliend_id, order_date, amount = line.split(";")
            order_id = int(order_id)
            manager_id = int(manager_id)
            cliend_id = int(cliend_id)
            amount = float(amount)
            order = Order(order_id, manager_id, cliend_id, order_date, amount)
            orders.append(order)
    return orders

def wr_orders(orders, filename):
    with open("orders_sorted.txt", "w", encoding="utf-8") as orders_sort_f:
        orders_sort_f.write("order_id, manager_id, cliend_id, order_date, amount\n")
        for order in sorted(orders, key=lambda x: x.amount, reverse=True):
            orders_sort_f.write(str(order)+"\n")
print("orders done")
