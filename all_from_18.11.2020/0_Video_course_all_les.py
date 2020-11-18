"""
# определяем тип переменной
person_name = 'Max'
age = 30
period = 3.2
is_good = True
person = None
print(type(person_name))
print(type(age))
print(type(period))
print(type(is_good))
print(type(person))


# str - это строка
# int - целое число
# float - число с плавающей точкой
# bool - булевые числа, ЛОГИЧЕСКИЙ тип данных, правда или ложь
# NoneType -
Конкатинация - это склеивание данных


# sep - сепаратор, фукция котора в принте разделяет фукции любым знаком. пример
print('stroka', 40, 40.5, True, None, sep='***')
# end='\n' это перенос строки или убирает её, приклеивает наверх
print('stroka', 40, 40.5, True, None, end='--------------')
print('stroka', 40, 40.5, True, None)


# что бы не спросили в инпут, это всегда будет строка, что бы сделать числом вначале вставляем ИНТ
result = int(input('>>'))
print(result)
print(type(result))


ale = 71
age = int(input('how old are U?:'))
print('Your universary yes', age % 5 == 0)

# not and or, != не равно или еще можно перед фукцией поставить not

print('У вас НЕ юбилей', age % 5 != 0)
print('У вас НЕ юбилей', not age % 5 == 0)

# and
print('У васю юбил И возраст меньше средней жизни', age %  5 == 0 and age <ale)

# or
print('У вас юбил ИЛИ возраст меньше средней жизни', age % 5 == 0 or age <ale)

# приоритет в логических выражениях
print((3>2 and (6 <5 or 3 < 2)) and 0 == 0)


age = int(input('input your age:'))
# если возраст меньше 18 лет
# Вывести на экран "доступ запрещен"
# else это условие если не выполняется if
# elif это дополнительный код (альтернативное условие) к if и элиф может быть сколько угодно много
# if может быть внутри блоков , в любой блок. вложенность
if age < 18:
    print("эдоступ запрещен")
elif age == 18:
    print("вам только 18")
    print("что с вами делать")
elif age > 18 and age <25:
    print("вы отдельная категория пользователей")
else:
    print('acsess aproved')
    # проверим на юбилей
    if age % 5 == 0:
        print('поздравляем у вас в этом году юбилей')

number = 43
value = int(input('введите число от 1 до 100>>'))
if value == number:
    print('Угадали!!')
else:
    if value > number:
        print("Не верно, введенное число слишком большое")
    else:
        print("Не верно, введенное число слишко маленькое")



# ЦИКЛЫ while *********************************************************
# это цикл с условиями, while условие выполняется тогда: действие1 дейстиве2 и т д
name = input(' кто создатель python ?>')
while name != 'Гвидо':
    print(' Не верно, пробуйте еще')
    name = input(' кто создатель python ?>')
print(' верно ')

# первый вариант, самостоятельный, как бы от обратного
i = 10
value = int(input('введите число больше 0 но меньше 10>> '))
while value > i or value <= 0:
   value = int(input('от 0 до 10, пробуй еще раз>> '))
print(value ** 2)


# второй вариант из урока, но более логичный в вечном цикле

while True:
    value = int(input('введите число от ноля до десяти'))
    if value < 10 and value >0:
        print(value**2, 'хороший вариант')
        break # брейк можно не писать, тогда снова будет ввод
    else:
        print('от 0 до 10 пробуй еще раз')



# вывод чисел от 0 до 100
# вывод числе от 0 до n , где эн вводит пользователь
# вывод четных чисел от 0 до эн

number = 0
n = int(input(' число введите>>'))
while number <= n:
    if number % 2 == 0: # делится на 2, значит четное
        print(number) # поэтому печатаем
    # number = number + 1
    number += 1 # это будет тоже самое что строка сверху



# break позволяет выйти из цикла в независимотси выполнилось условие или нет
name = None

while True:
    name = input(' кто создатель python ?>')
    if name == 'Гвидо':
        break
    print(' не верно ')
print(' верно ')

# continue переход на след. итерацию цикла (команды в цикле после continue не выплняются)


number = 0
n = int(input(' число введите>>'))

while number <= n:
    if number % 2 == 0: # делится на 2, значит четное
        number += 1 # это будет тоже самое что строка сверху
        continue
    print(number)  # поэтому печатаем
    number += 1


# while-else в блоке else (после while ) мы выполеняем действиея после того
#как вышли из цикла while когда условие цикла стало не верным (False)

number = 0

while number <=100:
    print(number)
    number += 1
    #if number == 33:
     #   break
else:
    print('else - end')
print('end')


ДОМАШНЕЕ ЗАДАНИЕ 1-3 ПУНКТЫ

while True:
    number = int(input('введите число 0-10>>'))
    if number > 0 and number < 10:
        break
    print(' НЕ верно, число должно быть от 0 до 10')
    continue
number1 = number ** 2
print('ваше число во второй степени - ', number1)




name = input(' имя -')
surname = input(' фамилия-')
age = int(input(' ваш возрас -'))
weight = int(input(' ваш вес-'))

if age <=30 and weight >= 50 and weight <=120:
    print(name, surname, 'хорошее состояние')
elif age > 30 and age <= 40 and (weight > 50 or weight > 120):
    print(name, surname, ' займись собой')
elif age >= 40 and (weight < 50 or weight > 120):
    print(name, surname, ' иди к врачу')


# СТРОКИ str
# можно вычислить символ по индексу, индекс указывается в []
# все индексы начинаются с 0. отрицательные индексы допускаются

friend = 'Максим'
n = int(input(' введите номер буквы>> '))
letter = friend[n]
print(n+1, 'я буква имени - ', letter)
print(friend[-1])


# Срезы 1 - с какого символа, 4 - по какой символ, 4: срез с начала строки

friend = 'Максим'
print(friend[1:4])



# len методы и строки, может определить длину строки
# len(friend) - длинна строки (сколько в ней символов)
# friend.find('a') - ищем символ а в строке
# friend.split() - разбиение строки через пробел
# friend.isdigit() - строка состоит из чисел

friends = 'Максим Леонид'
print(friends)

print(len(friends))
print(friends.find('нид'))
friends = 'Максим-Леонид'
print(friends.split('-')) # можно не только пробелы разделить, а любой другой знак

print(friends.isdigit()) # строка не из цифр, поэтому выдает false. работает похоже только на то что в скобках

number = '123'
print(number.isdigit())

print(friends.upper()) # все буквы делает большими заглавными
print(friends.lower()) # все буквы делает меленькими строчными

# функция len и методы списка, len(friends) - длина списка (сколько в нем элементов)

# Методы строк строчек
# help(str) или выпадающая подсказка в pycharm или сайт питонворлд

# ФОРМАТИРОВАНИЕ СТРОК
# конкантенация (не рекомендуется) - это склеиванеи строк
# %
# format (рекомендуется)

name = 'Leo'
age = 30
# конкатенация не плохо читается код и нужны пробелы
hellou_str = ' привет, ' + name + ' тебе ' + str(age) + ' лет '
print(hellou_str)
# % строка %s и число %d
hellou_str = ' Привет %s тебе %d лет' % (name, age)
print(hellou_str)

# 3 format
hellou_str = ' Привет {} тебе {} лет ' .format(name, age)
print(hellou_str)

top5 = ' Первые 5 мест на соревнованиях: 1. Иванов. 2. Петров. ' \
       '3. Сидоров. 4. Орлов. 5.Соколов.'
start = top5.find('1')
end = top5.find('4')
top3 = top5[start: end]
result = ' Поздравляем {} с успехом!'.format(top3.upper())
print(result)


#  Список и кортежи. Списки (list - списки)

# можно объявить пустой список
empty_list = []

# можнго объявит список и сразу заполнить его элементами
friends = ['Max', 'Leo', 'Kaye']

# тип списка - list
print(type(friends))

# Как и в строке для списка доступны индексы (начинаются с 0)
print('Второй друр: ', friends[1])
print('Первый друг с конца', friends[-1])
print('Первый друг', friends [0])

# Так же можно применять срезы, срезы вовзращают параметр списка
print(friends[1:2])
print(friends[:2])
print(friends[1:])

# Функция len и методы списка
# len(friends) - длинна списка (сколько в нем элементов)
# friends.append('Ron') - добавление нового элемента
# friends.pop() - удаляем последний элемент и возвращаем его
# friends.clear() - очищаем весь список
# friends.remove('Ron) - удаление объекта из списка
# del friends[0] - удаление элемента по индексу


friends = ['Max', 'Leo', 'Kate']
print(friends)
print(len(friends)) # узнаем длинну списка
friends.append('Ron') # добавляем в существующий список новый элемент
print(friends)
print(len(friends))
print(friends.pop()) # удалили последний элемент и вывели его на экран
print(friends)
friends.clear()
print(friends)

friends = ['Max', 'Leo', 'Kate']
friends.remove ('Kate')
print(friends)

del friends[0] # Так можно удалить элементсписка
print(friends)
"""

# Оператор in ВАЖНО !!!!!!!!!!!!!!!!
# позволяет проверить наличие элемента в списке. есть ли значение, найти, проверить
# 'Max' in friends, результат тру или фолс
#
"""
hero = 'Superman'



if hero.find('man') != -1:
    print('man')
if 'man' in hero:
    print('есть1')

goals = ['стать гуру языка пайтон', 'здоровье', 'накормить кота']
if 'здоровь' in goals:
    print('не забыли все ок')
else: print('нету, ошибочка вышла')

"""

# КОРТЕЖ (tuple) - список который нельзя менять. записывается в КРУГЛЫХ скобках.
# roles = ('user', 'manager', 'admin').
# Кортеж служит для защиты от изменений.

# пользователь вводит кол-во учатсников соревнований по пайтон.
# Пользователь вводит участников и их метса в зависимости от количества
# .
"""
print('соревнования по пайтон'. upper())
count = int(input('введи количество участников>>'))
i = count
members = []
while i > 0:
    name = input('Кто занял {} место>>'.format(i))
    members.append(name)
    i-=1
# кто участвовал в соревнованиях (по алфавиту)
print('В соревновании участвовали:', sorted(members))
# мы записали людей с конца ?
members.reverse()

# нам нужно взять первые три места
result = members[:3]
result = 'Победители : {} Поздравляем!'.format(result)
print(result)
"""

# встроенные типы и операции с ними
# for цикл
"""
friend_name = 'Max'
friends = ['Max', 'Leo', 'Kate']
roles = ('admin', 'guest', 'user')

if 'Max' in friends:
    print('У меня есть этот друг')

if 'M' in friend_name:
    print('Буква М есть в имени друга')

i = 0 # переменная i стандартная с нуля
while i < len(friends):
    friend = friends[i]
    print(friend)
    i+=1  # на забываем добавлять счетчик или цикл while будет бесконечным.
"""
# тоже черзе цикл for. позволяет перебирать элементы последовательности
# по порядку без указания индекса.
#  for friend in friedns:
#          print (friend)
# заканчивает выполнение кода заканчиватеся последовательность элементов.
"""
for friend in friends:
    print(friend)
print('end списка с циклами while and for--------------')
for letter in friend_name:
    print(letter)
print('end строка')

for role in roles:
    print(role)
print('конец кортежа')
"""
# for vs while
# преимущество следует отдавать циклу фор
# --------------------

# функция range, создаем последовательность

"""
numbers = range(10)
print(numbers)
print(type(numbers))
numbers = range(20) # от 0 ипоследняя цифра в последовательность не включается
print(list(numbers))
"""

# RANGE
"""
winners = ['Max', 'Leo', 'Kate' ]
# простой перебор
for winner in winners:
    print(winner)

# используем range
for i in range (len(winners)):
    print(i+1, ')', winners[i])

"""

# словарь dict . неупорядоченные коллекции произвольных объектов с доступом по ключу.[]
"""
friends = ['Max', 'Leo', 'Kate' ]
print (friends)
print(type(friends))
friend = friends[0]
print(friend)
print(type(friend))
# как добавить возраст другу. нужно ввести ключ и значение
friend = {
    'name': 'Max',
    'age': 39
}
print(friend)
print(type(friend))
"""

#####
"""
friend = {
    'name': 'Max',
    'age': 23
}
print(friend)
print(type(friend))
print(friend['age']) # вызываем из словоря квадратными скобками
print(friend['name'])
# добавляем в словарь квадратными скобками.
friend['has_car'] = True
print(friend)
friend['has_car'] = False
print(friend)
del friend['age']
print(friend)

if 'age' in friend:
    print('есть возраст')
if 'has_car' in friend:
    print('есть тачка')
######




friend = {
    'name': 'Max',
    'age': 23,
    'has_car': True
}
# по ключам
for key in friend.keys():
    print(key)
    print(friend[key])

# тоже самое по ключам вариант 2
for key in friend:
    print(key)
    print(friend[key])

# по значениям
for val in friend.values():
    print(val)

    print('-----------')

# самый широкий подход это Пары ключ значение
for item in friend.items(): # items возвращает нам список из кортежей
    print(type(item))
    print(item)

for key, val in friend.items():
    print(key)
    print(val)
######
"""

# Множества SET . Методы и применения. Не может быть 2 одинаковых элемента.
# объявляется фигурной скобкой и пишутся значения через запятую
"""
######
cites = ['Las Vegas', 'Paris', 'Moscow', 'Paris', 'Moscow']

print(type(cites))
print(cites)

cites = set(cites)
print(cites) # видим что задублированные города исчезли
#####

#####
cites = {'Las Vegas', 'Paris', 'Moscow'}
print(cites)
cites.add('Burma')
print(cites)

cites.remove('Moscow')
print(cites)

print(len(cites))
print('Paris' in cites)

for city in cites:
    print(city)
#####


# множества поддерживают операции, объеденение &, пересечение |, разность -
#####
# семейная пара собирается в отпуск, каждый из супругов собирает в поездку вещи
# , макс взял эти вещи
max_things = {'Телефон', 'Бритва', 'Рубашка', 'Шорты'}
# Кейт взяла эти вещи
kate_things = {'Телефон', 'Шорты', 'Зонтик', 'Помада'}

# какие вещи взяли супруги?
print(max_things | kate_things)
# какие вещи повторяются
print(max_things & kate_things)
# какие не взял макс, но взяла кейт
print(max_things - kate_things)
# какие не взяла кейт но взял макс
print(kate_things - max_things)

#####

# 1: Даны два произвольные списка. Удалите из первого списка элементы присутствующие во втором списке.
a = [1, 1, 1, 2, 2, 2, 3, 4]
b = [2, 4, 5]
for number in a[:]: # что бы не пропускать цифры делаем срез от начала до конца
     if number in b: # это означает что если намбер есть в списке то
         a.remove(number) # срез , т.к. делаем удаление из списка
print(a)




#2 Дана дата в формате dd.mm.yyyy, например: 02.11.2013.
# Ваша задача — вывести дату в текстовом виде, например:
# второе ноября 2013 года. Склонением пренебречь (2000 года, 2010 года)

date = '02.11.2013'
d, m, y = date.split('.') # берем команду сплит, что бы разделить список на 3 части

print(d, m, y)
month = {
    '01': 'января',
    '11': 'ноября',
    '12': 'декабря',

}

days = {
    '02': 'Второе',
    '11': 'одиннадцатое'
}
result = f'{days[d]} {month[m]} {y} года'
print(result)


# 3: Дан список заполненный произвольными целыми числами.
# Получите новый список, элементами которого будут только уникальные элементы исходного.
#     Примечание. Списки создайте вручную, например так:
# my_list_1 = [2, 2, 5, 12, 8, 2, 12]
#
# В этом случае ответ будет:
# [5, 8]

# my_list_1 = [2, 2,2,25, 5, 12, 8, 2, 12]
# print([i for i in my_list_1 if my_list_1.count(i) == 1])

numbers = [2, 2, 5, 12, 8, 2, 12]
result = []
for data in numbers:
    if numbers.count(data) == 1:
        result.append(data)

print(result)

####################################### Программа угадай число.
import random
number = random.randint(1, 100)
print(number)
user_number = int(input('Угадай число любое>> '))
print(user_number)
if number == user_number:
    print('Вы угадали')
elif number < user_number:
    print('Ваше число БОЛЬШЕ загаданного')
else:
    print('Ваше число МЕНЬШЕ загаданного')
"""
# Эта модель (сверху) разовая, поэтому нужно добавить цикл, что бы игра повторялась, пока пользователь не угадает
"""
import random
number = random.randint(1, 100)
#print(number)
while True:
    user_number = int(input('Угадай число любое>> '))
    print(user_number)
    if number == user_number:
        print('Вы угадали')
        break
    elif number < user_number:
        print('Ваше число БОЛЬШЕ загаданного')
    else:
        print('Ваше число МЕНЬШЕ загаданного')
"""

# еще один вариант улучшенного кода  программы
"""
import random
user_number = None # Здесь мы для открытия цикла присваиваем переменной никакое значение
number = random.randint(1,100)
print(number)
while number != user_number: # т.е. когда наше число не равно загаданному, то
    # возвращается в цикл, а цикл условие НЕ РАВНО, поэтом когда угадывается число, то идет прерывание цикла и оно же ВЕРНО.
    user_number = int(input('Введите число >> '))
    if user_number > number:
        print('чсило БОЛЬШЕ загаданного')
    elif user_number < number:
        print('Ваше число меньше загаданного')
print('победа')
"""

# усложним. добавим количество попыток
"""
import random
user_number = None
count = 0
max_count = 3

number = random.randint(1,100)
print(number)
while number != user_number:
    count +=1
    if count > max_count:
        print('Все наигрался, хватит!')
        break
    print(f'Попытка №{count}')
    user_number = int(input('Введите число >> '))
    if user_number > number:
        print('чсило БОЛЬШЕ загаданного')
    elif user_number < number:
        print('Ваше число меньше загаданного')
else: # добавили else, что бы исправить ситуацию с тем что при превышении попыток , вываливается цикл и соотв. победа
 print('WINN !!!')
"""

# усложним. добавим уровни сложности

"""
import random
user_number = None
count = 0
levels = {1: 10, 2: 5, 3: 3} # вписываем ключи
level = int(input('выбери уровень сложности от 1 до 3: '))
max_count = levels[level] # выставляем по ключу уровень сложности

number = random.randint(1,100)
print(number)
while number != user_number:
    count +=1
    if count > max_count:
        print('Все наигрался, хватит!')
        break
    print(f'Попытка №{count}')
    user_number = int(input('Введите число >> '))
    if user_number > number:
        print('чсило БОЛЬШЕ загаданного')
    elif user_number < number:
        print('Ваше число меньше загаданного')
else: # добавили else, что бы исправить ситуацию с тем что при превышении попыток , вываливается цикл и соотв. победа
 print('YOU WINN !!!')
 """

# Добавим пользователей
"""
import random
user_number = None
count = 0
levels = {1: 10, 2: 5, 3: 3} # вписываем ключи
level = int(input('выбери уровень сложности от 1 до 3: '))
max_count = levels[level] # выставляем по ключу уровень сложности
user_count = int(input('введи количество игроков: '))
users = [] # объявляем пустой список. пользователей будем записывать в список.
for i in range(user_count):
    user_name = input(f'Введите имя пользователя {i}: ')
    users.append(user_name)
# нужно организовать логику очередности хода по очереди

number = random.randint(1,100)
print(number)
while number != user_number:
    count +=1
    if count > max_count:
        print('Все пользователи проиграли!!')
        break
    print(f'Попытка №{count}')
    for user ............
    user_number = int(input('Введите число >> '))
    if user_number > number:
        print('чсило БОЛЬШЕ загаданного')
    elif user_number < number:
        print('Ваше число меньше загаданного')
else: # добавили else, что бы исправить ситуацию с тем что при превышении попыток , вываливается цикл и соотв. победа
 print('YOU WINN !!!')
 """

# ЗАДАНИЕ
"""
1. В этой игре человек загадывает число, а компьютер пытается его угадать.
В начале игры человек загадывает число от 1 до 100 в уме или записывает его на листок бумаги. 

Компьютер начинает его отгадывать предлагая игроку варианты чисел. Если компьютер угадал число, 
игрок выбирает “победа”. Если компьютер назвал число меньше загаданного, игрок должен выбрать 
“загаданное число больше”. Если компьютер назвал число больше, игрок должен выбрать “загаданное 
число меньше”. Игра продолжается до тех пор пока компьютер не отгадает число.
Пример игры:
Допустим, пользователь загадал число 42
`15
35
96
<
37
74
<
52
<
42
=`
    Примечание: Знаки “=”, “>” и “<” пользователь вводит с клавиатуры для общения с компьютером. 
    Вы можете использовать этот способ или придумать свой
"""

#################################
"""
import random

min_number = 1
max_number = 100
result = None
while result != '=':
    number = random.randint(min_number, max_number)
    print(number)
    result = input('><=Х ? >>')
    if result == '<':
        min_number = number + 1
    elif result == '>':
        max_number_number = number - 1
print('win')
"""

######### Урок 8 . ФУНКЦИИ ########### с 26,10,20
"""
numbers = [] # сделаем пустой контейнер
for i in range(3):
    number = int(input('введите число >> '))
    numbers.append(number)
print(max(numbers))
print(min(numbers))
print(sum(numbers))
"""

################ def СОЗДАНИЕ СОБСТВЕННЫХ ФУНКЦИЙ №№№№№№№№№№№№№№
"""
def print_sep(sep, sep_len):
    print(sep * sep_len) # Название, параметры, результат. Так пишутся свои функции

print_sep('*', 70)
print_sep('-', 70)
"""

"""
def get_sep(sep, sep_len):
    return sep * sep_len

print(get_sep('*', 70))
print(get_sep('-', 70))

# меняем знак и длинну разделителя
get_sep('=', 50)

# используем разделитель в тексте
sep = get_sep('-', 50)
text = 'Hello {} Func {}'.format(sep, sep)

print(text)

"""
############# Передача параметров по имени
"""
def hello_max():
    print('Hellow', 'Max')
hello_max()

def hello(who):
    print('Hellow', who)
hello('Leo')
hello('Max')

def greeting(who, say): # Передача параметров по имени
    print(say, who)

greeting('Leo', 'Hi')
greeting('Max','Hiiiiii')
greeting(say='hi', who='leo')

def greeting(who, say='Defold параметр'): # Параметр по умолчанию можно сделать
    print(say, who)

greeting('Leo')
greeting('Max','Hiiiiii')
greeting(say='hi', who='leo')
"""

##################### args , kwargs
# args - передача любого количества по порядку - *
# kwargs - передача любого количества по ИМЕНИ - **kwargs

"""
def greeting(say, *who): # (* звездочка перед параметром - любое количество по порядку, видим что есть кортеж)
    print(say, who)

greeting('Hello', 'Leo')
greeting('Hello', 'Leo', 'Max')
greeting('Hello', 'Leo', 'Max',' Kate')

def get_person(**kwargs): # (**kwargs - приходит словарь, т.е. любое количстество имен)
    for k, v in kwargs.items():
        print(k, v)

get_person(name='Leo', age=20, has_car=True)

"""

######## sorted, filter, map функции #########

"""
numbers = [1,5,3,5,9,11]
print(sorted(numbers)) # сортировка по возрастанию
print(sorted(numbers, reverse=True)) # по убыванию

cites = [('Москва', 1000), ("Лас-Вегас", 500), ("Антверпен", 2000)]
print(sorted(cites)) # сработает численность по алфавиту

def by_count(city):
    return city[1]
print(sorted(cites, key=by_count)) # сработает численность по количеству населения

print(sorted(cites, key=lambda city: city[1])) # тоже самое но через лямбду

"""
"""
def person_info(name, age, city):
    result = f'{name}, {age} лет(год(а)) , проживает в городе {city}'
    return result
name = input('введите имя')
age = int(input('Введите возраст'))
city = input('Введите город')
print(person_info(name, age, city))
"""

# 2: Создайте функцию, принимающую на вход 3 числа и возвращающую наибольшее из них

"""
def get_max(a,b,c):
    result = max([a,b,c])
    return result

result = get_max(1,5,3)
print(result)
print(get_max(7,1,3))
"""

"""
3: Давайте опишем пару сущностей player и enemy через словарь, который будет 
иметь ключи и значения:
name - строка полученная от пользователя,
health = 100,
damage = 50. ### Поэкспериментируйте с значениями урона и жизней по желанию. 
### Теперь надо создать функцию attack(person1, person2). 
Примечание: имена аргументов можете указать свои. ### Функция в качестве аргумента 
будет принимать атакующего и атакуемого. ### В теле функция должна получить параметр 
damage атакующего и отнять это количество от health атакуемого. Функция должна сама 
работать со словарями и изменять их значения.
"""
"""
player_name = input('Имя игрока - ')

player = { # Словарь . Данные через библиотеку заносим
    'name': player_name,
    'health': 100,
    'damage': 50
}

enemy_name = input('Имя врага - ')
enemy = { # Словарь . Данные через библиотеку заносим
    'name': enemy_name,
    'health': 50,
    'damage': 30

}
def attack(unit, target):
    target['health'] -= unit['damage']

attack(player, enemy)
print(enemy)

attack(enemy, player)
print(player)

"""

"""
4: Давайте усложним предыдущее задание. Измените сущности, 
добавив новый параметр - armor = 1.2 (величина брони персонажа)
Теперь надо добавить новую функцию, которая будет вычислять 
и возвращать полученный урон по формуле damage / armor
Следовательно, у вас должно быть 2 функции:
Наносит урон. Это улучшенная версия функции из задачи 3.
Вычисляет урон по отношению к броне.

Примечание. Функция номер 2 используется внутри функции номер 1 
для вычисления урона и вычитания его из здоровья персонажа.
"""

"""
player_name = input('Имя игрока - ')

player = { # Словарь . Данные через библиотеку заносим
    'name': player_name,
    'health': 100,
    'damage': 50,
    'armor': 1.2
}

enemy_name = input('Имя врага - ')
enemy = { # Словарь . Данные через библиотеку заносим
    'name': enemy_name,
    'health': 50,
    'damage': 30,
    'armor': 1
}

def get_damage(damage, armor ):
    return damage / armor

def attack(unit, target):
    damage = get_damage(unit['damage'], target['armor'])
    target['health'] -= damage

attack(player, enemy)
print(enemy)

attack(enemy, player)
print(player)
"""

"""
name_for_userid = {
    382: "Alice",
    590: "Bob",
    951: "Dilbert",
}
def greeting(userid):
    return "Hi %s!" % name_for_userid.get(userid, "there")
print(greeting(382))
print(greeting(111111))
"""

########################################################################################
#################################  МОДУЛИ ##############################################
# 29.10.2020

##### тимпорт обычный ################
"""
import math
import random as rd
print(math.pi) # получаем сразу число пи из модуля
print(math.sin(38)) # синус угла в радианах

print(rd.randint(1,55))
"""

##### тимпорт всего  содержимого модуля(не рекоменд.) ################
"""
from math import *
print(pi) # в данном случае можно писать сразу пи,
# без указания библиотеки, т.к. имортировано все целиком
print(sin(30))
"""
"""
from random import randint, randrange # импорт конкретных фукций
print(randint(1,99))
"""

####### Библиотека math ################

"""

import math
r = 100
# определяем длинну окружности C = 2πR = π D, где R – радиус круга, D – диаметр круга
print(2*r*math.pi)

# определяем площадь окружности S=πr**2
print(math.pi*(r**2))
print(math.pow(r, 2)*math.pi)

# по координатам 2-х точек опр. расстояние между ними
x1 = 10
y1 = 10
x2 = 50
y2 = 100
l = math.sqrt((x1-x2)**2+(y1-y2)**2) # вычисляем квадратный корень по теореме пифагора
print('расстояние между двумя точками', l)

# найти факториал числа 9
print(math.factorial(9))
"""

###################   random модуль ####################

"""
# случайное число от 0 до 100
from random import randint
print(randint(0,100))

# выбрать победителя лотереи из списка players
from random import randint, choice # Дополнительно импортируем choice
players = ['max', 'leo', 'kate', 'ron', 'bill']
print(choice(players))

# выбрать трех победетелей из списка
from random import randint, choice, sample # Доплнительно испортиуем сэмпл
players = ['max', 'leo', 'kate', 'ron', 'bill']
print(sample(players, 3)) # итак, формируются три победителя

# перемешать карты в стопке (списке) cards
cards = ['6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
from random import randint, choice, sample, shuffle # добавляем ипорт шафл
print(cards)
shuffle(cards)
print(cards)
"""

###################### Модули os и sys ###########################
"""
time = int(input('Введите количество секунд>>'))
hour = time // 3600
minute = time // 60
second = time % 60
print(f"чч:мм:сс >>> {hour:02}:{minute:02}:{second:02}")
"""

"""
import os
def create_folders():
    for i in range(1, 3):
        folder_name = f'dir_{i}'
        os.mkdir(folder_name)

def delete_folders():
    for i in range(1, 10):
        folder_name = f'dir_{i}'
        os.rmdir(folder_name)
if __name__ == "__main__":

    create_folders()
    delete_folders()

"""

##################### ФАЙЛЫ И КОДИРОВКИ ########################


###########Режимы открытия mode
"""
Функция open
f = open(‘my.txt’, ‘w’)
file — имя файла
mode — режим
открывает файл в указанном режиме
encoding — кодировка
r — чтение
w — запись, если файла нет, создается новый
x — запись, если файла нет, ошибка
a — дозапись
b — двоичный режим
+ — открытие на чтение и запись

открываем на запись, файла не существует.
f = open("first.txt", "w")

открываем на чтение - файла не существует, ошибка
f = open("second.txt", "r")

открываем на чтение - файл существует
f = open("first.txt", "r")

Запись текста в файл
writelines — записать список строк в файл
\n — символ конца строки
write — записать строку в файл

"""
# f = open("first.txt", "w")
# f.write("Hello\n")
# f.write("World")
#
# f.writelines(["Hello\n", "Python, \"i kavichki vnutry postavim\""])

"""
Чтение из файла
for line in f: — чтение файла построчно
readlines — чтение файла в список строк
read — чтение всего файла
"""

# f = open("first.txt", "r")
# print(f.read())
# for line in f:
#     print(line.replace('\n', ""))
# print(f.readlines())

"""
Закрытие файла
Открытые файлы тратят ресурсы системы.
f.close().
Если до close произойдет исключительная ситуация, файл не будет закрыт.
После работы с файлом его необходимо закрывать.
Удобным вместо close() является использование with.
"""
# f = open("first.txt", "r")
# for line in f:
#     print(line.replace('\n', ""))
# f.close()

# with open("first.txt", "r") as f:
#     for line in f:
#         print(line.replace('\n', ""))
# print("end")


###########Режимы открытия mode
"""
Функция open
f = open(‘my.txt’, ‘w’)
file — имя файла
mode — режим
открывает файл в указанном режиме
encoding — кодировка
r — чтение
w — запись, если файла нет, создается новый
x — запись, если файла нет, ошибка
a — дозапись
b — двоичный режим
+ — открытие на чтение и запись

открываем на запись, файла не существует.
f = open("first.txt", "w")

открываем на чтение - файла не существует, ошибка
f = open("second.txt", "r")

открываем на чтение - файл существует
f = open("first.txt", "r")

Запись текста в файл
writelines — записать список строк в файл
\n — символ конца строки
write — записать строку в файл

"""
# f = open("first.txt", "w")
# f.write("Hello\n")
# f.write("World")
#
# f.writelines(["Hello\n", "Python, \"i kavichki vnutry postavim\""])

"""
Чтение из файла
for line in f: — чтение файла построчно
readlines — чтение файла в список строк
read — чтение всего файла
"""

# f = open("first.txt", "r")
# print(f.read())
# for line in f:
#     print(line.replace('\n', ""))
# print(f.readlines())

"""
Закрытие файла
Открытые файлы тратят ресурсы системы.
f.close().
Если до close произойдет исключительная ситуация, файл не будет закрыт.
После работы с файлом его необходимо закрывать.
Удобным вместо close() является использование with.
"""
# f = open("first.txt", "r")
# for line in f:
#     print(line.replace('\n', ""))
# f.close()

# with open("first.txt", "r") as f:
#     for line in f:
#         print(line.replace('\n', ""))
# print("end")

############## СТРОКИ И БАЙТЫ
"""
Типы строк в Python
bytes — строки байт
bytearray — изменяемая строка байт
str — обычные строки

Действия со строками байт
срез sb[1:3]
...
индекс sb[0]

"""

"""
Работа с файлом в режиме байтов
open(‘filename’, ‘rb’) — режим чтения байтов
параметр encoding определяет кодировку
open(‘filename’, ‘wb’) — режим записи байтов
open(‘filename’, ‘w’, encoding=’utf-8’)

Запись байтов в файл
f.write(‘some str’) — файл открыт в режиме w
в любом случае информация хранится в виде нулей и единиц
f.write(b’some bytes’) — файл открыт в режиме wb

Чтение байтов из файла
f.read() - файл открыт в режиме r — читаем строки
f.read() - файл открыт в режиме rb — читаем байты

Python
pickle

Модуль pickle
Преобразует сложные объекты в байты.
Встроен в Python.
Сохраняет сложные объекты в файл. 

pickle. Основные функции
dumps — преобразование объекта в байты
load — загрузка объекта из файла
dump — сохранение объекта в файл 
loads — загрузка объекта из набора байт

Python
json

План
Модуль json в Python. Применение.
Основные функции.
Примеры.
Формат json. Применение.

Формат json
Текстовый формат обмена данными, основанный на JavaScript.
JavaScript Object Notation.
Аналогичен набору словарей, списков, простых типов данных в Python.
Является просто текстом (строкой).

Применение
передача данных
чаще всего используется в web-разработке для передачи данных по протоколу http
хранение данных

json в Python
Требуется только преобразование в строку и обратно.
Этим занимается модуль json.
Основные структуры Python схожи с форматом.
import json.

json. Основные функции
dumps — преобразование объекта в json (в текст)
load — загрузка объекта из файла
dump — сохранение объекта в формате json в файл 
loads — загрузка объекта из формата json (строки)

Задача
Передать список любимых песен и их исполнителей своему другу, разработчику C#.

import json

friends = [
    {"name": "Max", "age": 23, "Phones": [123,234]},
    {"name": "Leo", "age": 33}
] # список в который входят словари

# посмотрим тип объекта
print(type(friends))


# Преобразуем список друзей в json
json_friends = json.dumps(friends)

# печатаем что поулчилось
print(json_friends)

# проверим тип
print(type(json_friends))

# обратно из json в объект
friends = json.loads(json_friends)

print(friends) 
print(type(friends))

########## отправка файла соседу для открытия на С# ######

import json

favourite_tracks = [
    {"name": "Вечная любовь", "artists": "Агата Кристи"},
    {"name": "Angel", "artists": "Massive Attack"},
    {"name": "Jamming", "artists": "Bob Marley"}
]

with open("tracks.json", "w", encoding="utf-8") as f: # открываем на запись и добавляем кодировку, тк есть русские буквы
    json.dump(favourite_tracks, f)

print("выполнено")


"""
################### Тернарный оператор #########################
"""тернарный (ternarius — «тройной») оператор — операция, возвращающая свой первый или третий операнд в зависимости от значения логического выражения, заданного вторым операндом
результат 1 если выражение_истинно, иначе результат 2

Применение
позволяет писать компактный и читаемый код
вместо конструкции if … else, в которой нет elif

Синтаксис
number = 1 if is_one else 2
print(‘Привет’ if is_russian else ‘Hello’)
name = ‘Max’ if is_has_name else ‘Empty’
в общем виде: результат1 если условие иначе результат2


is_has_name = True
name = "Max" if is_has_name else "Empty"
print(name)
is_has_name = False
name = "Max" if is_has_name else "Empty"
print(name)

is_one = True
number = 1 if is_one else 2
print(number)
is_one = False
number = 1 if is_one else 2
print(number)

is_russian = True
print("Привет" if is_russian else "Hello")
is_russian = False
print("Привет" if is_russian else "Hello")



word = "слово"
print(type(word))
result = []
for i in range(len(word)):
  if i % 2 != True:
    letter = word[i].lower()
  else:
    letter = word[i].upper()
  result.append(letter)

result = "".join(result)
print(result)

word = "Тернарный"
print(type(word))
result = []
for i in range(len(word)):
  letter = word[i]
  letter = letter.upper() if i % 2 == 0 else letter.lower()
  result.append(letter)

result = "".join(result)
print(result)

password = input("Введите пароль j>>")

print("Входите" if password == "j" else "не верный пароль")
"""

######################## Генератор списка и словарей ##############

"""Определение
В Python существует специальная синтаксическая конструкция, которая позволяет по определенным правилам создавать заполненные списки. Такие конструкции называются генераторами списков.
Генераторы словарей можно определить по аналогии.

Применение
позволяет писать компактный и читаемый код
вместо цикла for
работают быстрее

Синтаксис
[ number for number in numbers if number > 0 ]

# Записать в список только положительные числа
numbers = [1,2,3,4,5,-1,-2,-3]

# по классике сначала через тернарный оператор
result = []
for n in numbers:
  result.append(n) if n > 0 else None
print(result)

# черзе функцию filter
result = filter(lambda number: number > 0, numbers)
print(list(result))

# Через генератор списка
result = [number for number in numbers if number > 0 ]
print(result)


# Создать список из случайных чисел от 1 до 100.
import random
numbers = [random.randint(1, 100) for i in range(5)]
print(numbers)

# Создать список квадратов чисел.
numbers = [number**2 for number in numbers]
print(numbers)

# Создать список имен на букву А.
names = ["Руслан", "Андрей", "Алексей"]
names = [name for name in names if name.startswith("А")]
print(names)

Решить с помощью генераторов списка.

1: Даны два списка фруктов. Получить список фруктов,
присутствующих в обоих исходных списках.
    Примечание: Списки фруктов создайте вручную в начале файла.


# Записать в список только положительные числа
fruit1 = [
    "apple",
    "pear",
    "chery",
    "melon"
]

fruit2 = [
    "apple",
    "orange",
    "chery"
]

f = []
f = [f for f in fruit1 if f in fruit2]
print(f)



2: Дан список, заполненный произвольными числами.
Получить список из элементов исходного, удовлетворяющих следующим условиям:
Элемент кратен 3,
Элемент положительный,
Элемент не кратен 4.

Примечание: Список с целыми числами создайте вручную в начале файла.
Не забудьте включить туда отрицательные числа. 10-20 чисел в списке вполне достаточно.


from random import randint
numbers = [randint(-100, 100) for i in range(20)]
# numbers = [1,2,3,4,5,6,7,8,9,10,-5,-16,-9]
print(numbers)


print ([n for n in numbers if n % 3 == 0 and n > 0 and n % 4 != 0])



3. Напишите функцию которая принимает на вход список.
Функция создает из этого списка новый список из квадратных
корней чисел (если число положительное) и самих чисел
(если число отрицательное) и возвращает результат (желательно применить
генератор и тернарный оператор при необходимости).
В результате работы функции исходный список не должен измениться.
Например:
old_list = [1, -3, 4]
result = [1, -3, 2]

Примечание: Список с целыми числами создайте вручную в начале файла.
Не забудьте включить туда отрицательные числа. 10-20 чисел
в списке вполне достаточно.

import math
old_list = [9, -72, -54, 66, 54, 85, 45, -78, 10, 75, -39, 66, 40, 70, 6, 39, 51, -67, -99, -52]

def new_sqrt_list(input_list):
    result = [math.sqrt(number) if number > 0 else number for number in input_list]
    return result

result = new_sqrt_list(old_list)
print(result)
print(old_list)







----------------------------------


Приведение типов к bool в Python
Истина: ‘abc’, [1], (1,), {1:’a’}, 10, 1.1, ...
Ложь: ‘’, [], (), {}, 0, None, ...
Все встроенные типы данных в Python 
приводятся к логическому типу bool по определенным правилам:


# добавление элемента в список
# классический способ
def add_to_list (input_list = None):
  if input_list is None:
    input_list = []
  input_list.append(2)
  return input_list
result = add_to_list([0, 1])
print(result)
result = add_to_list()
print(result)

# через or
def add_to_list (input_list = None):
  # используем свойство or вместо условия
  input_list = input_list or []
  input_list.append(2)
  return input_list
result = add_to_list([0, 1])
print(result)
result = add_to_list()
print(result)
"""
################ Модуль copy

"""Хранение списков в памяти
При работе со списками стоит помнить, что если мы переприсваиваем 
список в другую переменную a = b и меняем значения внутри нового списка b[1], 
значения изменятся и внутри старого списка a[1], т.к. ссылки на элементы 
списка остаются на своих местах в памяти и каждый список использует одни и те же элементы.


Изменение элементов списка в функции
При передаче списка параметром в функцию нужно быть особенно внимательными: 
функция может изменить элемент списка внутри основной программы.


Методы копирования списка
Метод copy у самого списка.
Создание среза от начала и до конца списка my_list[:]. 

Модуль copy
Используется функция deepcopy.
b = copy.deepcopy(a).
Применяется для полного (глубокого) копирования списка.


# пример
numbers = [1,2,3]

def change_number_in_list(input_list):
  input_list[1] = 200

# после вызова функции
change_number_in_list(numbers)
# список в основной программе тоже изменится
print(numbers)

# пример
numbers = [1,2,3]

def change_number_in_list(input_list):
  input_list[1] = 200

# после вызова функции
change_number_in_list(numbers)
# список в основной программе тоже изменится
print(numbers)

#### пример как сделать копию

a = [1,2,3]
# копия с помощью срезу
b = a[:]
b[1] = 200
# список а не изменится
print(a)

# копия с помощью метода copy
b = a.copy()
b[1] = 200
# ничего не изменилось
print(a)

# эти фукциии не будут работать если есть вложенные списки
a = [1,2,[1,2]]
b = a[:]
print(a)


# b = copy.deepcopy(a).
# Применяется для полного (глубокого) копирования списка.

import copy

a = [1,2, [1,2]]
b = copy.deepcopy(a)
b[2][1] = 200

# список а не изменился
print(a)
print(b)
"""

############# обработка исключений

"""Исключительная ситуация
Во время выполнения программы могут возникать ситуации, 
когда состояние внешних данных, устройств ввода-вывода 
или компьютерной системы в целом делает дальнейшие вычисления 
в соответствии с базовым алгоритмом невозможными или бессмысленными.

Классические примеры
Ошибка чтения данных при отсутствии доступа к ресурсу
...
Деление на 0

try:
    Код, который выполняется при возникновении исключительной      ситуации.

Перехват конкретных исключений
TypeError, ValueError, ...
Самое общее исключение имеет тип Exception.
В Python каждая исключительная ситуация имеет свой тип.
Рекомендуется обрабатывать конкретные исключительные ситуации и реагировать на разные исключения по-разному.

Информация об ошибке
Тогда в переменную e будет сохранен объект исключения.
Можно получить дополнительную информацию об исключении,Если использовать конструкцию except Исключение as e:

try - except - else - finally
Блок except — что делать при возникновении исключения.
Блок else — что делать, если исключения не произошло.
Блок try — код, который может вызвать исключение.
Блок finally — выполняется всегда.

Генерация исключений
Это можно сделать с помощью команды raise: raise Exception(‘Что то пошло не так’).
Иногда требуется не обработать а, наоборот, создать исключительную ситуацию.

"""
# пример ситуации
"""
number = int(input("Введите число>>"))
try:
    result = 100 /number
except ZeroDivisionError as e:
    print("деление на ноль")
    print("Информация о исключении", e)
except Exception as e:
    print("Не известная ошибка")
    print("Информация о исключении", e)

# try - except - else - finally
# Блок except — что делать при возникновении исключения.
# Блок else — что делать, если исключения не произошло.
# Блок try — код, который может вызвать исключение.
# Блок finally — выполняется всегда.


number = int(input("Введите число>>"))
try:
    result = 100 /number
except:
    print("деление на ноль")
else:
    print("Всё ОК ошибок не было")
finally:
    print("этот блок будет всегда при ошибке и нет")
raise Exception("Что то пошло не так") # создание исключительной ситуации


-----------
4. Написать функцию которая принимает на вход число от 1 до 100.
Если число равно 13, функция поднимает исключительную ситуации
ValueError иначе возвращает введенное число, возведенное в квадрат.
Далее написать основной код программы. Пользователь вводит число.
Введенное число передаем параметром в написанную функцию и печатаем
результат, который вернула функция. Обработать возможность возникновения
исключительной ситуации, которая поднимается внутри функции.

def unlucky_number(number):
    if number == 13:
        raise ValueError ("Несчастливое число")
    else:
        return number ** 2
number = int(input("Введите число>>"))

try:
    result = unlucky_number(number)
except ValueError:
    print("У нас обработка исключения которое создали сами")
else:
    print(result)



------------
"""

################### практикум консольный файловый менеджер ##########################

"""
Задача
Создание, удаление, копирование файлов и папок.
Сохранение информации о своей работе в файл.
Текущее видео: создание и проверка основных функций.
Консольный файловый менеджер.
Шаг 1
Создание файла.
Создание папки.
Шаг 2
Функция создания папки.
Шаг 3
Расширение функционала.
Просмотр списка файлов и папок.
Шаг 4
Цикл.
Пользователь играет, пока не угадает число.
Python
Практикум. File Manager.
Основные функции
(продолжение)
Задача
Удаление, копирование.
Запись информации о работе менеджера в файл.
Новые функции:
Шаг 1
Удаление файла.
Шаг 2
Копирование.
Шаг 3
Запись информации о работе менеджера в файл.
Шаг 4
Цикл.
Пользователь играет, пока не угадает число.
Python
Практикум. File Manager.
Создание скрипта
Задача
Написать логику работы скрипта.
Обработать возможные ошибки.
Объединить функции в одну программу.
Шаг 1
Импорт функций.
Шаг 2
Логика работы скрипта.
Шаг 3
Параметры для каждой функции.
Шаг 4
Проверка функционала.
Шаг 5
Вызов функции информации о менеджере.
Обработка возможных ошибок ввода пользователя.



# функция для создания файла

# Шаг 1 Создание файла.
def create_file(name, text=None):
    with open(name, "w", encoding="utf-8") as f:
        if text:
            f.write(text)


if __name__ == "__main__":  # для того чтобы при импорте фукции , другой скрип не выполнялся
    create_file("text.dat")  # файл создался
    create_file("text.dat", "some text")  # теперь проверим добавился ли в него текст
# Шаг 2 Создание папки.
import os  # воспользуемся модулем ос для создания папки


def create_folder(name):
    try:
        os.mkdir(name)
    except FileExistsError:
        print("Такая папка уже есть")


if __name__ == "__main__":
    create_folder("new_f1")


# Шаг 3 Расширение функционала. Просмотр списка файлов и папок.

def get_list(folders_omly=False):
    result = os.listdir()
    if folders_omly:
        result = [f for f in result if os.path.isdir(f)]
    print(result)
    print(os.listdir())

get_list(True)

# шаг 4 Удаление файла

def delete_file(name): # нейм будет путь до файла или папки
    if os.path.isdir(name):
        os.rmdir(name) # данная фукция удаляет по нейму только папку
    else:
        os.remove(name)
# delete_file("new2") # Удалит папку
# delete_file("text.dat") # Удалит файл

# шаг 5 Копирование файла или папки

import shutil # Импортируем модуль специальный
def copy_file(name, new_name):
    if os.path.isdir(name): # копирование дял папки
        try:
            shutil.copytree(name, new_name)
        except FileExistsError:
            print("Такая папка же уже есть")
    else:
        shutil.copy(name,new_name ) # теперь  копирование для файла
copy_file("new_f", "new_f2")
copy_file("text.dat", "text1.dat")

# шаг 6. Запись информации о работе менеджера в файл.
import datetime

def save_info(message):
    current_time = datetime.datetime.now()
    result = f"{current_time} - {message}"
    with open("log.txt", "a", encoding="utf-8") as f:
        f.write(result + "\n")

save_info("abc")

"""
# -----------------------------
# Написанный файловый менеджер

# main.py (файл создать)

import sys
from core import create_file, create_folder, get_list, delete_file, copy_file, save_info, change_dir
save_info("start")

try:
    command = sys.argv[1]
except IndexError:
    print("Необходимо выбрать команду. help")
else:
    if command == "list":
        get_list()

    elif command == "create_file":
        try:
            name = sys.argv[2]
        except IndexError:
            print("отсутствует название файла")
        else:
            create_file(name)

    elif command == "create_folder":
        try:
            name = sys.argv[2]
        except IndexError:
            print("отсутствует название папки")
        else:
            create_folder(name)

    elif command == "delete":
        try:
            name = sys.argv[2]
        except IndexError:
            print("отсутствует название файла")
        else:
            delete_file(name)

    elif command == "ch":
        try:
            name = sys.argv[2]
        except IndexError:
            print("отсутствует название директории")
        else:
            change_dir(name)


    elif command == "copy":
        try:
            name = sys.argv[2]
            new_name = sys.argv[3]
        except IndexError:
            print("введите название файла и нового файла")
        else:
            copy_file(name, new_name)
    elif command == "help":
        print("list - список файлов и папок")
        print("create_file - создать файл")
        print("create_folder - создать папку")
        print("delete - удалить файл или папку")
        print("copy - копировать файл или папку")

    save_info("finish")

# core.py файл создать

def create_file(name, text=None):
    with open(name, "w", encoding="utf-8") as f:
        if text:
            f.write(text)

import os  # воспользуемся модулем ос для создания папки


def create_folder(name):
    try:
        os.mkdir(name)
    except FileExistsError:
        print("Такая папка уже есть")

# Шаг 3 Расширение функционала. Просмотр списка файлов и папок.

def get_list(folders_omly=False):
    result = os.listdir()
    if folders_omly:
        result = [f for f in result if os.path.isdir(f)]
    print(result)
    print(os.listdir())


# шаг 4 Удаление файла

def delete_file(name): # нейм будет путь до файла или папки
    if os.path.isdir(name):
        os.rmdir(name) # данная фукция удаляет по нейму только папку
    else:
        os.remove(name)


# шаг 5 Копирование файла или папки

import shutil # Импортируем модуль специальный
def copy_file(name, new_name):
    if os.path.isdir(name): # копирование дял папки
        try:
            shutil.copytree(name, new_name)
        except FileExistsError:
            print("Такая папка же уже есть")
    else:
        shutil.copy(name,new_name ) # теперь  копирование для файла


# шаг 6. Запись информации о работе менеджера в файл.
import datetime

def save_info(message):
    current_time = datetime.datetime.now()
    result = f"{current_time} - {message}"
    with open("log.txt", "a", encoding="utf-8") as f:
        f.write(result + "\n")


def change_dir(name):
    os.chdir(name)
    print(os.getcwd())


if __name__ == "__main__":  # для того чтобы при импорте фукции , другой скрип не выполнялся
    create_file("text.dat")  # файл создался
    create_file("text.dat", "some text")  # теперь проверим добавился ли в него текст
    create_folder("new_f1")
    get_list(True)
    delete_file("new2") # Удалит папку
    delete_file("text.dat") # Удалит файл
    copy_file("new_f", "new_f2")
    copy_file("text.dat", "text1.dat")
    save_info("abc")
