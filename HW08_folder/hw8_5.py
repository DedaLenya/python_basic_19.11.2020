"""5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и
передачу в определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники,
а также других данных, можно использовать любую подходящую структуру, например словарь."""


class Data:
    def __init__(self, date):
        self.date = date

    @staticmethod
    def valid_date_metod():
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

eprinter = Enter_warehouse('printer', 2, 'pcs')
ecopier = Enter_warehouse('xerox', 1, 'pcs')
print(Enter_warehouse.some_dict)

sale = Out_warehouse(2)
print(f'\nОстаток на складе {Enter_warehouse.some_dict}')
