"""2. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего
элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.
Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123]."""

some_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
# result_list.index(el)	Получить позицию (индекс) первого элемента со значением el
new_list = [el for el in some_list if el > some_list[some_list.index(el)-1] and some_list.index(el) >= 1]
print(new_list)
