"""2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными.
Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом,
толщиной в 1 см * чи сло см толщины полотна. Проверить работу метода.
Например: 20м * 5000м * 25кг * 5см = 12500 т"""


# 1е решение
class Road:  # Объявляем класс
    _length = None  # Атрибут
    _width = None  # Атрибут

    def result(self):
        print(f'Масса {self.length * self.width * 25 * 5 / 1000} т.')


road_1 = Road()  # Экземпляр класса
road_1.length = 5000
road_1.width = 20
road_1.result()

# 2 решение
# class Road:
#     def __init__(self, length, width):
#         self._length = length
#         self._wigth = width
#
#     def result(self, mass_1cm, layer_cm):
#         return self._length * self._wigth * mass_1cm * layer_cm
# road = Road(5000,20)
# print(road.result(10,20))
