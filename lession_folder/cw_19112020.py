# print("hello world")
"""
workers = []
for i in range(0,3):
    print("index", i)

    worker = {
    "surname": "Murylev",
    "age": 39,
    "covid_test": "True"
    }
    workers.append(worker)
print(workers)


books_in_list = ["gogo" , "tolsyoy"]
books_in_list.insert(2, "dfsdfsa")


for index in range(len(books_in_list)):
    # print(f"В пакете есть книга {books_in_list[index]} с индексом {index}")
    print(f"{index}")



# 28,11,2020
# todo словарь словарю словаря перебор по значению
dict_some = {
    "a":2,
    "b":4,
    "c":5
}
dict_some["добавляем"] = 99
for key , value in dict_some.items():
    print(key, value, sep="____разделитель____")

print(dict_some.keys()) # получаем значение ключей
print(dict_some.values()) # получаем значения

# проверка на да нет в одной строке
while True:
    next = input("Добавить ? Да/Нет\n>>")
    if next.lower() in ("да", "нет"):
        next = next.lower() == "да"
        break
    else:
        print("Неверный ввод, повторите")


# def some_f():
#     a = 1 + 2
#     return a
# print(some_f())
#
# def some_f(): # без ретурна не работает
#     a = 1 + 2
# print(some_f())


def ext_func(var_1):
    def int_func(var_2):
        return var_1 + var_2
    return int_func

f_obj = ext_func(200) # f_obj - функция
print(f_obj(300))
"""

def s_calc():
    r_val = float(input("Укажите радиус: "))
    h_val = float(input("Укажите высоту: "))
    # площадь боковой поверхности цилиндра:
    s_side = 2 * 3.14 * r_val * h_val
    # площадь одного основания цилиндра:
    s_circle = 3.14 * r_val ** 2
    # полная площадь цилиндра:
    s_full = s_side + 2 * s_circle
    return s_full

s_val = s_calc()
print(s_val)
