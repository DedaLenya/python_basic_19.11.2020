"""Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится месяц
(зима, весна, лето, осень). Напишите решения через list и через dict.
"""

# вариант через список
number = int(input("Введите номер месяца>>"))
month = ["Зима", "Зима", "Весна", "Весна", "Весна", "Лето", "Лето", "Лето", "Осень", "Осень", "Осень", "Зима"]
print(month[number])



# Вариант 2 через словарь
number = int(input("Введите номер месяца>>"))
d = {
    12: 'Зима',
    1: "Зима",
    2: "Зима",
    3: "Весна",
    4: "Весна",
    5: "Весна",
    6: "Лето",
    7: "Лето",
    8: "Лето",
    9: "Осень",
    10: "Осень",
    11: "Осень"
    }

print(d[number])

# Вариант 3 через строку
m1 = ("зима", "весна", "лето", "осень", "зима")
m = (int(input("Введите номер месяца>>"))) // 3
# n = m // 3
print(m1[m])
