"""3. Реализовать программу работы с органическими клетками. Необходимо создать класс Клетка.
В его конструкторе инициализировать параметр, соответствующий количеству ячеек клетки (целое число)..
В классе должны быть реализованы методы перегрузки арифметических операторов: сложение (__add__()),
вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).

Данные методы должны применяться
только к клеткам и выполнять увеличение, уменьшение, умножение и обычное (не целочисленное)
деление клеток, соответственно. В методе деления должно осуществляться округление значения до целого числа.
Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность количества ячеек
двух клеток больше нуля, иначе выводить соответствующее сообщение.
Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется как произведение
количества ячеек этих двух клеток.
Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется как целочисленное
деление количества ячеек этих двух клеток.
целочисленное деление количества ячеек этих двух клеток.

В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду.
Данный метод позволяет организовать ячейки по рядам.
Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу.
Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5.
Тогда метод make_order() вернет строку: *****\n*****\n**.
Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5.
Тогда метод make_order() вернет строку: *****\n*****\n*****.
"""


class OrganicCell:
    def __init__(self, number_cell):
        self.number_cell = number_cell

    def __add__(self, other):
        return OrganicCell(self.number_cell + other.number_cell)

    def __sub__(self, other):
        if self.number_cell - other.number_cell > 0:
            return OrganicCell(self.number_cell - other.number_cell)
        raise ValueError ('Вычитание из первой клетки не возможно, она менее второй')
        # else:
        #     print('Вычитание из первой клетки не возможно, она менее второй')

    def __mul__(self, other):
        return OrganicCell(self.number_cell * other.number_cell)

    def __truediv__(self, other):
        try:
            return OrganicCell(self.number_cell // other.number_cell)
        except ZeroDivisionError:
            print('Деление на ноль')

    def make_order(self, rows):
        bufstr = '\n'.join(['*' * rows for _ in range(self.number_cell // rows)])
        return f'{bufstr}\n{"*" * (self.number_cell % rows)}'

    def __str__(self):
        return f'{self.number_cell}'


cell1 = OrganicCell(11)
cell2 = OrganicCell(5)
cell_plus = cell1 + cell2
cell_minus = cell1 - cell2
cell_multiply = cell1 * cell2
cell_division = cell1 / cell2

print(f'Уменьшение - {cell_minus}')
print(f'Умножение - {cell_multiply}')
print(f'Увеличение - {cell_plus}')
print(f'Деление - {cell_division}')
print(cell_minus.make_order(5))
