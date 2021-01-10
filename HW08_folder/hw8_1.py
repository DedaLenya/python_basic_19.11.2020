"""1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата
«день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число,
месяц, год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить
валидацию числа, месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на
реальных данных."""


class Data:
    def __init__(self, date):
        self.date = date

    @classmethod
    def number_metod(cls, date):
        number = int(''.join(map(str, date.split('-'))))
        print(number)
        return cls(date=date)

    @staticmethod
    def valid_date_metod():
        valid_date = str(a.date).split('-')
        for i in valid_date:
            if i.isdigit():
                pass
            else:
                raise ValueError('В дату передаются не допустимые символы')
        print(valid_date)
        return a.date


a = Data('28-12-2021')
b = Data.number_metod('28-10-2020')
Data.valid_date_metod()
