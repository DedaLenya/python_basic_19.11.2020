"""6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь по возможности реализовать
в проекте «Склад оргтехники» максимум возможностей, изученных на уроках по ООП."""


class Data:
    def __init__(self, date):
        self.date = date

    @staticmethod
    def valid_date_metod() -> int:
        valid_date = str(a.date).split('-')
        for i in valid_date:
            if i.isdigit():
                pass
            else:
                raise ValueError('В дату передаются не допустимые символы')
        print(f'На склад {valid_date} поступило:')
        return a.date


class Enter_warehouse:
    some_dict = {}
    count = 0

    def __init__(self, name_type, quanty, units):
        self.name_type = name_type
        self.quanty = quanty
        self.units = units
        Enter_warehouse.count += 1
        Enter_warehouse.some_dict[Enter_warehouse.count] = [self.name_type, self.quanty, self.units]


class Out_warehouse:
    def __init__(self, key):
        self.key = key
        Enter_warehouse.some_dict.pop(key, 1)


a = Data('28-12-2021')
Data.valid_date_metod()

eprinter = Enter_warehouse('printer', 1, 'pcs')
ecopier = Enter_warehouse('xerox', 1, 'pcs')
escanner = Enter_warehouse('HP', 1, 'compl')
print(Enter_warehouse.some_dict)


class Zerrocheck(Exception):
    def __init__(self, text):
        self.txt = text


article = input("\nВведите ячейку что хотите взять со склада>>")
try:
    if not article.isdigit():
        raise Zerrocheck("Ячейка может быть только числом, перемещение не состоялось")
    else:
        sale = Out_warehouse(int(article))
except Zerrocheck as mr:
    print(mr)

print(f'\nОстаток на складе {Enter_warehouse.some_dict}')
