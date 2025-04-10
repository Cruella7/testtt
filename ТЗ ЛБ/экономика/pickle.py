import pickle
import shelve
from order import Order
def crfile():
    orders = []
    with open("sofa.txt", "wb") as orders_f:
        pickle.dump(orders, orders_f)
    print("Файл создан")

def openfl():
    try:
        with open("sofa.txt", "rb") as orders_f:
            orders = pickle.load(orders_f)
            print("Файл открыт")
            return orders
    except FileNotFoundError:
        print("Файл не найден")

def addorder():
    try:
        orders = openfl()
        order_id = int(input("Номер заказа: "))
        manager_id = int(input("Номер менеджера: "))
        client_id = int(input("Номер клиента: "))
        order_date = input("Дата заказа: ")
        amount = float(input("Сумма заказа: "))
        order = Order(order_id, manager_id, client_id, order_date, amount)
        orders.append(order)
        with open("sofa.txt", "wb") as orders_f:
            pickle.dump(orders, orders_f)
        print("Заказ добавлен")
    except ValueError:
        print("Неправильный ввод")
def editord():
    """
    Изменение заказа в файле по номеру Manager_ID
    """
    try:
        orders = openfl()
        manager_id = int(input("Номер менеджера для изменения заказа: "))
        for order in orders:
            if order.manager_id == manager_id:
                order_id = int(input("Новый номер заказа: "))
                client_id = int(input("Новый номер клиента: "))
                order_date = input("Новую дату заказа: ")
                amount = float(input("Новую сумму заказа: "))
                order.order_id = order_id
                order.client_id = client_id
                order.order_date = order_date
                order.amount = amount
                with open("sofa.txt", "wb") as orders_f:
                    pickle.dump(orders, orders_f)
                print("Заказ изменен")
                return
        print("Заказ не найден")
    except ValueError:
        print("Неправильный ввод")
def to_html():
    """
    Вывод данных в HTML-файл
    """
    try:
        orders = openfl()
        with open("orders.html", "w") as html_f:
            html_f.write("<html>\n<head>\n<title>Заказы</title>\n</head>\n<body>\n<table>\n<tr><th>Номер заказа</th><th>Номер менеджера</th><th>Номер клиента</th><th>Дата заказа</th><th>Сумма заказа</th></tr>\n")
            for order in orders:
                html_f.write(f"<tr><td>{order.order_id}</td><td>{order.manager_id}</td><td>{order.client_id}</td><td>{order.order_date}</td><td>{order.amount:.2f}</td></tr>\n")
            html_f.write("</table>\n</body>\n</html>")
        print("Данные выведены в файл orders.html")
    except TypeError:
        print("Файл пуст")

def menu():
    while True:
        print("\nМеню:")
        print("1. Создать файл")
        print("2. Открыть файл")
        print("3. Добавить заказ")
        print("4. Изменить заказ")
        print("5. Выйти")
        try:
            choice = int(input("Что будем делать? "))
            if choice == 1:
                crfile()
            elif choice == 2:
                crfile()
            elif choice == 3:
                addorder()
            elif choice == 4:
                editord()
            elif choice == 5:
                break
            else:
                print("Ошибочка,попробуйте еще раз выборать")
        except ValueError:
            print("Неправильный ввод")

if __name__ == '__main__':
    menu()
