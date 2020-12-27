"""2. Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс)
этого проекта — одежда, которая может иметь определенное название. К типам одежды в этом проекте
относятся пальто и костюм. У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property."""

from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def clothes_brand(self, brand):
        pass


class Suit(Clothes):  # пример с @property
    def __init__(self, hight):
        self.hight = hight

    def clothes_brand(self, brand):
        if brand:
            print(f'Одежда бренда {brand}')

    @property
    def H_size(self):
        return f'{2 * self.hight + 0.3} Метра ткани нужно для костюма\n'


class Coat(Clothes):  # пример без @property, все расчеты и результаты в самом конструкторе
    def __init__(self, veight):
        self.veight = (veight / 6.5 + 0.5).__round__(2)
        print(f'{self.veight} Метров ткани нужно для для пальто')

    def clothes_brand(self, brand):
        if brand:  # будет ли присваиваться название(бренд) одежды.
            print(f'Одежда бренда {brand}')


markandspanser = Suit(52)
markandspanser.clothes_brand('M&S')
print(markandspanser.H_size)

baon = Coat(44)
baon.clothes_brand('Baon')
