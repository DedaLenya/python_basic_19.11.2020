"""Реализовать функцию, принимающую два числа
(позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку
ситуации деления на ноль."""


def foo_division(number1, number2):
    if number2 == 0:
        print("Деление на 0!!, завершаем ошибкой")
    result = number1 / number2
    print(f"результат деления чисел {result} = ")


foo_division(int(input("Делимое>> ")), int(input("Делитель>> ")))


# def foo_division(number1, number2):
#     try:
#         result = number1 / number2
#     except ZeroDivisionError as e:
#         print("Деление на 0!!, завершаем ошибкой - ", e)
#     print(f"результат деления чисел = {result} ")
#
#
# foo_division(int(input("Делимое>> ")), int(input("Делитель>> ")))
