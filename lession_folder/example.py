# def encrypt(message, k):
#     letters = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
#     message = message.upper()
#     result = ''
#     for i in message:
#         index = letters.find(i)
#         if index != -1:
#             # остаток от деления тут используется для того,
#             # чтобы не было выхода за пределы строки letters
#             # и не возникала ошибка IndexError
#             result += letters[(index + k) % len(letters)]
#         else:
#             result += i
#
#
#     print(result)
#
#
# encrypt("остаток от деления тут используется для того,", -1)

# def summ_func(args):
#
#     while True:
#         result = input("Введите числа через пробел, для выхода наберите любой символ >> ").split()
#         try:
#             result = sum(map(int, result))
#         except ValueError:
#             print(f"*****\nВыходим из програмы, итоговая сумма: {(sum(map(int, args)))}")
#             break
#         args.append(result)
#         print(f"Промежуточный итог суммы ведённых чисел: {sum(map(int, args))}")
#
#
# summ_func([])


# def int_func(letters):
#     # letters = input("введите слово латиницей >>")
#     letters = letters.capitalize()
#     print(type(letters))
#     print(letters)
# int_func(letters=input("введите слово латиницей >>"))

"""Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
но с прописной
первой буквой. Например, print(int_func(‘text’)) -> Text."""


# def int_func(lett):
#     lett1 = []
#     for i in lett:
#             lett1.append(i)
#     jo = "".join(lett1)
#     tit = chr(ord(lett1[0]) - 32)
#     print(jo[0]+jo[1:])
#     print(tit)
#
# int_func("sDf")
#

# some_string = input("Строка латиницей>>")
#
#
# def int_func(letters):
#
#     for lett_very in some_string:
#         if 122 >= ord(lett_very) >= 97 or ord(lett_very) == 32:
#             pass
#         else:
#             print("Ошибка. На ввод принимается строка из слов, разделенных пробелом ")
#             return None
#     words = []
#     letters = letters.split(" ")
#     for letters in letters:
#         letters_cap = letters.capitalize()
#         words.append(letters_cap)
#     print(" ".join(words))
#
#
# int_func(some_string)


# def int_func(lett):
#     lett1 = []
#     lett = lett.split()
#
#     for i_lett in lett:
#         big_lett = chr(ord(i_lett[0]) - 32)
#         lett1.append(big_lett)
#         s_lett = i_lett[1:]
#         lett1.append(s_lett)
#         lett1.append(" ")
#     print("".join(lett1))
#
#
# int_func("latin statin fantin")

some_string = input("Строка латиницей>>")


def int_func(lett):
    """

    :param lett:
    :return:
    """
    for lett_very in some_string:
        if 122 >= ord(lett_very) >= 97 or ord(lett_very) == 32:
            pass
        else:
            print("Ошибка. На ввод принимается строка из слов, разделенных пробелом ")
            return None


    lett1 = []
    lett = lett.split()

    for i_lett in lett:
        big_lett = chr(ord(i_lett[0]) - 32)
        lett1.append(big_lett)
        s_lett = i_lett[1:]
        lett1.append(s_lett)
        lett1.append(" ")
    print("".join(lett1))


int_func(some_string)
