"""4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction),
которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод
show_speed, который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar
переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно
выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам,
выведите результат. Выполните вызов методов и также покажите результат."""


class Car:
    def __init__(self, speed: int, color: str, name: str, is_police: bool):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return 'start, move'

    def stop(self):
        return 'stop'

    def turn_left(self):
        return 'turn left'

    def turn_right(self):
        return 'turn right'

    def show_speed(self):
        return {'speed': self.speed, '': []}


class TownCar(Car):
    speed_limit = 60

    def show_speed(self):
        speed_info = super().show_speed()
        if speed_info['speed'] > TownCar.speed_limit:
            speed_info[''].append('over speed')
        return speed_info


class SportCar(Car):
    pass


class WorkCar(Car):
    speed_limit = 40

    def show_speed(self):
        speed_info = super().show_speed()
        if speed_info['speed'] > TownCar.speed_limit:
            speed_info[''].append('over speed')
        return speed_info


class PoliceCar(Car):
    pass


chevrolet = TownCar(0, 'red', 'Chevrolet', True)
print(f'Params {chevrolet.color}, {chevrolet.name}, Cops - {chevrolet.is_police}')
print(chevrolet.go())
chevrolet.speed = 50
print(chevrolet.show_speed())
print(chevrolet.turn_right())
chevrolet.speed = 110
print(chevrolet.show_speed())
print(chevrolet.turn_left())
print(chevrolet.stop())

print(50 * "#")

gas = WorkCar(0, 'black', 'Gazel', False)
print(f'Params {gas.color}, {gas.name}, Cops - {gas.is_police}')
print(gas.go())
gas.speed = 30
print(gas.show_speed())
gas.speed = 70
print(gas.show_speed())
print(gas.stop())
