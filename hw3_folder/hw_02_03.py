"""Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения,
город проживания, email, телефон. Функция должна принимать параметры
как именованные аргументы. Реализовать вывод данных о пользователе одной строкой."""

# Вариант вывода в строку, через именнованые аргументы превращающиеся в словарь


email = input('имейл>>')
if not email.endswith("@mail.ru"):
    print("Ошибка ввода имейла, всё упало.")
    quit()
name = input('введите имя>>')
year = int(input('год рождения>>'))
city = input('город>>')


def directory(**kwargs):
    print(kwargs)


directory(name=name, year=year, city=city, email=email)

# Вариант вывода читабельный, перебором словаря, через именнованые аргументы превращающиеся в словарь.


def directory(**kwargs):
    print(kwargs)
    for key, value in kwargs.items():
        print("{} is {}".format(key, value))


directory(name="Deda", surname="Lenya", year="1981", city="Екатеринбург", email="ip66net", tel="0006")
