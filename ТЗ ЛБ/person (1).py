#класс Person с атрибутами имя, фамилия и квалификация
class Person:
    def __init__(self, name, surname, qualification=1):
        self.name = name
        self.surname = surname
        self.qualification = qualification

    #получение информации о человеке
    def get_info(self):
        return f"{self.name} {self.surname}, qualification: {self.qualification}"
    def __del__(self):
        print(f"До свидания, мистер {self.name} {self.surname}")

# три экземпляра класса Person с разными атрибутами
a = Person("Светлана", "Смирнова", 3)
b = Person("Борис", "Васильев", 2)
c= Person("Дарья", "Ольгова")

#выводим информацию о каждом экземпляре person
print(a.get_info())
print(b.get_info())
print(c.get_info())

# Удалить объект person с самым низким уровнем квалификации
if per1.qualification <= per2.qualification and per1.qualification <= per3.qualification:
    del a
elif per2.qualification <= per1.qualification and per2.qualification <= per3.qualification:
    del b
else:
    del c

input()  # чтобы скрипт не завершился сразу после выполнения