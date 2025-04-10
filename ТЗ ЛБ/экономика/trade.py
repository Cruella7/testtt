from client import Client
from manager import Manager
from order import Order

class Trade:
    """
    Класс о данных торгового процесса
    """
    def __init__(self, trade_id: int):
        """
        Списки менеджеров, клиентов и заказов
        """
        self.trade_id = trade_id
        self.managers = []
        self.clients = []
        self.orders = []

    def add_manager(self, manager: Manager):
        """
        Добавление менеджера в список менеджеров компании
        """
        self.managers.append(manager)

    def add_client(self, client: Client):
        """
        Добавление  клиента в список клиентов компании
        """
        self.clients.append(client)

    def add_order(self, order: Order):
        """
        Добавление заказа в список заказов компании
         """
        self.orders.append(order)

    def __str__(self):
        return str(self.trade_id)

    def read_managers(self, managers_fname):
        with open(managers_fname, "r") as managers_f:
            for line in managers_f:
                manager_id, name, city, comm = line.split(";")
                manager_id = int(manager_id)
                comm = float(comm)
                manager = Manager(manager_id, name, city, comm)
                self.managers.append(manager)
    def Kovrov_managers(self):
        """ """
        res = []
        for manager in self.managers:
            if manager.city.upper() == 'КОВРОВ':
                res.append(manager)
        return res

if __name__ == '__main__':
    """
    Чтение из файлов
    """
    trade = Trade(1)
    trade.read_managers("manager.txt")
    trade.read_managers("manager.txt")
    trade.read_clients("client.txt")
    trade.read_orders("order.txt")
    """
    Вывод
    """
    print('Ковровские продавцы') #заголовка
    print('manager_id name city comm') #заголовки столбцов
    for manager in trade.Kovrov_managers(): #вывод из списка менеджеров информации о каждом менеджере
        print(manager)
    print()
