"""5 . Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран."""


with open("example5.txt", "w", encoding="utf8") as file:
    file.write(input('Введите числа через пробел>>'))
with open("example5.txt", "r", encoding="utf8") as file:
    file = file.readline()
    sum_list = map(int, file.split())
    print(sum(sum_list))
