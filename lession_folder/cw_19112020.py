# less6 ООП

############################## 1й вариант.

class TrafficLight: # Класс
    __color = "" # Атрибут

    def running(self): # Метод

        self.color = "Красный"
        print("RED")

        self.color = "Желтый"
        print("YELL")

        self.color = "Зеленый"
        print("GREEN")#

a = TrafficLight()
a.running()

################################ 2й вариант

class TrafficLight: # Класс
    __color = "" # Атрибут


    def running(self, color): # Метод
        self.color = color
        print(color)

        return color

a = TrafficLight()
a.running('RED')
a.running('YELL')
a.running('GREEN')

############################### 3й вариант

class TrafficLight: # Класс
    __color = "" # Атрибут


    def __init__(self, color): # Метод
        self.color = color

red_light = TrafficLight("Зеленый")
print(red_light.color)

yell_light = TrafficLight("Желтый")
print(yell_light.color)

green_light = TrafficLight("Красный")
print(green_light.color)

