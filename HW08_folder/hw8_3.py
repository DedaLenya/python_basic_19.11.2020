"""3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять список.
Класс-исключение должен контролировать типы данных элементов списка.
Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно,
пока пользователь сам не остановит работу скрипта, введя, например, команду “stop”.
При этом скрипт завершается, сформированный список выводится на экран.
Подсказка: для данного задания примем, что пользователь может вводить только числа и строки.
При вводе пользователем очередного элемента необходимо реализовать проверку типа элемента и вносить его в список,
только если введено число. Класс-исключение должен не позволить пользователю ввести текст
(не число) и отобразить соответствующее сообщение. При этом работа скрипта не должна завершаться."""


class Zerrocheck(ValueError):
    def __init__(self, text):
        self.txt = text


some_list = []
while True:
    a = input("Число или что то еще, как надоест - S>>")
    try:
        if not a.isdigit():
            raise Zerrocheck('Не число, в список внесено не будет')
        some_list.append(a)
    except Zerrocheck as mr:
        print(mr)
    if a == 'S':
        break
print(some_list)
