def display_game_info():
    with open("игра.txt", "r") as file:
        game_info = file.read()
        print(game_info)

def display_developer_info():
    with open("разработчик.txt", "r") as file:
        developer_info = file.readline()
        print(developer_info)

def display_language_info():
    with open("инструменты.txt", "r") as file:
        language_info = file.readline()
        print(language_info)

def main_menu():
    while True:
        print("Меню:")
        print("1. Название игры со всем её описание")
        print("2. Разработчик игры \"Барби\"")
        print("3. На каком языке написана игра \"Гонки\"")
        print("4. Выход")

        choice = input("Выберите пункт меню (1-4): ")

        if choice == "1":
            display_game_info()
        elif choice == "2":
            display_developer_info()
        elif choice == "3":
            display_language_info()
        elif choice == "4":
            break
        else:
            print("Некорректный выбор. Попробуйте еще раз.")


if __name__ == "__main__":
    main_menu()