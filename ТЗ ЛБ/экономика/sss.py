import shelve
from order import Order

def crfile():
    with shelve.open("sofa.db", writeback=True) as orders_db:
        orders_db["orders"] = []
    print("Файл создан")

def openfl():
        with shelve.open("sofa.db", writeback=True) as orders_db:
            orders = orders_db.get("orders", [])
            print("Файл открыт")

def addorder():
        orders = openfl()
        order_id = int(input("Номер заказа: "))
        manager_id = int(input("Номер менеджера: "))
        client_id = int(input("Номер клиента: "))
        order_date = input("Дата заказа: ")
        amount = float(input("Сумма заказа: "))
        order = Order(order_id, manager_id, client_id, order_date, amount)
        orders.append(order)
        with shelve.open("sofa.db", writeback=True) as orders_db:
            orders_db["orders"] = orders
        print("Заказ добавлен")


def editord():
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
                with shelve.open("sofa.db", writeback=True) as orders_db:
                    orders_db["orders"] = orders
                print("Заказ изменен")
                return
        print("Заказ не найден")

def menu():
    while True:
        print("\nМеню:")
        print("1. Создать файл")
        print("2. Открыть файл")
        print("3. Добавить заказ")
        print("4. Изменить заказ")
        print("5. Выйти")
        choice = int(input("Что будем делать? "))
        if choice == 1:
            crfile()
        elif choice == 2:
             openfl()
        elif choice == 3:
            addorder()
        elif choice == 4:
             editord()
        elif choice == 5:
            break
        else:
         print("Ошибочка, попробуйте еще раз выбирать")

if __name__ == '__main__':
    menu()