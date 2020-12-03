#
# REC_POS = 1        # индекс словаря в записи
# PRODUCT_NAME = 0   # индекс ключа 'название'
# PRODUCT_PRICE = 1  # индекс ключа 'цена'
# PRODUCT_COUNT = 2  # индекс ключа 'количество'
# PRODUCT_UNIT = 3   # индекс ключа 'ед'
#
# database = [
#     (1, {'название': 'компьютер', 'цена': 20000, 'количество': 5, 'ед': 'шт.'}),
#     (2, {'название': 'принтер', 'цена': 2000, 'количество': 2, 'ед': 'шт.'}),
#     (3, {'название': 'сканер', 'цена': 2000, 'количество': 2, 'ед': 'ед.'}),
#     (4, {'название': 'принтер', 'цена': 8000, 'количество': 4, 'ед': 'шт.'})
# ]
#
# product_card = {}
# product_params = [
#     'название',
#     'цена',
#     'количество',
#     'ед'
# ]
#
# counter = 1
# while True:
#     name = input('Введите название товара (или END для выхода): ')
#     if name == 'END':
#         break
#     price = input('Введите цену товара: ')
#     count = input('Введите количество товара: ')
#     unit = input('Введите единицу измерения товара: ')
#
#     product_card = {
#         product_params[PRODUCT_NAME]: name,
#         product_params[PRODUCT_PRICE]: price,
#         product_params[PRODUCT_COUNT]: count,
#         product_params[PRODUCT_UNIT]: unit
#     }
#     database.append(tuple((counter, product_card)))
#     counter += 1
#
# product_analysis = {}
# for product_param in product_params:
#     param_result = []
#
#     for product in database:
#         key_value = product[REC_POS][product_param]
#         if key_value not in param_result:
#             param_result.append(key_value)
#
#     product_analysis[product_param] = param_result
#
# for param in product_params:
#     print(param, product_analysis[param])

goods_all = []  # будем заполнять список кортежами
count = int(input("Введите число, сколько будете вводить товаров>> "))
goods_dict1 = {}  # будем заполнять список кортежами для второго условия задания
count1 = 0
for i in range(count):
    name = input(f"{i+1}й товар. Введите - название >>")
    price = int(input(f"{i+1}й товар. Введите - цена >>"))
    quantity = int(input(f"{i+1}й товар. Введите - количество >>"))
    unit = input(f"{i+1}й товар. Введите - еденица измерения >>")
    goods_dict = {
        "название": name,
        "цена": price,
        "количество": quantity,
        "еденица измерения": unit
    }
    goods_all.append(goods_dict)

    goods_dict1.setdefault("название", [])
    goods_dict1["название"].append(name)
    goods_dict1.setdefault("цена", [])
    goods_dict1["цена"].append(price)
    goods_dict1.setdefault("количество", [])
    goods_dict1["количество"].append(quantity)
    goods_dict1.setdefault("еденица измерения", [])
    goods_dict1["еденица измерения"].append(unit)

# первое условие задания - структура товара список кортежей
for i in goods_all:
    print(f"{count1+1}{i}")
    count1 += 1
# второе условие задания - Аналитика словоря
for key, val in dict.items(goods_dict1):
    print(f"{key} {val}")






# print(type(goods_all))
