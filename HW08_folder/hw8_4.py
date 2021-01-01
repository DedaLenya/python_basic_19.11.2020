'''4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники
(принтер, сканер, ксерокс). В базовом классе определить параметры, общие для приведенных типов.
В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.'''

from abc import ABC, abstractmethod

class DiscriptionWarehouse:
    def region(self, region):
        self.region = region

class Equipment(ABC):
    @abstractmethod
    def format_paper(self, paper):
        self.paper = paper
    @abstractmethod
    def brand_name(self, name):
        self.name = name


class Printer(Equipment):
    def format_paper(self, paper):
        self.paper = paper
        print('формат', paper, end=' , ')
    def brand_name(self, name):
        self.name = name
        print('бренд', name)


class Scanner(Equipment):
    def format_paper(self, paper):
        self.paper = paper
        print('формат', paper, end=' , ')

    def brand_name(self, name):
        self.name = name
        print('бренд', name)

class Copier(Equipment):
    def format_paper(self, paper):
        self.paper = paper
        print('формат', paper, end=' , ')

    def brand_name(self, name):
        self.name = name
        print('бренд', name)

a = Printer()
a.format_paper('A2')
a.brand_name('ricoh')

b = Scanner()
b.format_paper('A4')
b.brand_name('HP')

c = Copier()
c.format_paper('A3')
c.brand_name('xerox')
