# 113 Преобразование коллекций
"""
my_string = "Моя строка"
my_tuple = ("Мой", "кортеж")
print(list(my_string))
print(list(my_tuple))
print(my_string[0])
print(my_tuple[0])

my_string = "Моя строка"
my_list = ["Мой", "список"]
print(tuple(my_string))
print(tuple(my_list))
"""

# Итераторы и итерируемые объекты
"""
a = range(10)
b = [1,2,3]
c = enumerate(b)

for i in a:
    print(i)

for i in b:
    print(i)

for i in c:
    print(i)

print(a[0])
print(b[0])
# print(c[0]


# словарь Словарь, как и список — изменяемый тип данных.
my_dict = {
    "first": "Первый",
    "second": "Второй",
    3: "Третий"

}
print(my_dict["second"])
print(my_dict[3])

# Объявить пустой словарь можно так
my_empty_dict = {}

# Словарь, как и список — изменяемый тип данных. Например, чтобы добавить новую пару ключ-значение в словарь можно сделать так
my_dict = {}
my_dict["new_key"] = "Новое значение"

# Если в квадратных скобках указать существующий ключ, его значение будет заменено на новое

my_dict = {"key": 15}
my_dict["key"] = "Новое значение"

my_dict = {"key": 15}
key_var = "key"
print(my_dict[key_var])
"""

# В этом уроке надо написать программу, в которой объявлена переменная first_dict. Тип переменной first_dict — словарь.
# В этом словаре должно быть три ключа:
# Первый ключ должен быть строкой, а его значение должно быть целым числом. Значение строки и числа могут быть любыми.
# Второй ключ должен быть любым кортежем, а его значение — любым списком.
# Третий ключ должен быть числом с плавающей запятой, а его значение — любой строкой
# Программа должна вывести на экран значение каждого из ключей.

first_dict = {
    str("key1"): int(11),
    ("key2",): list("any_list"),
    float(1.5):str("any_string")
}
print(first_dict["key1"])
print(first_dict[("key2",)])
print(first_dict[1.5])
