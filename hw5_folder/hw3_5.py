"""3  Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников."""

d = {}
count = 0
with open("example3.txt", "r", encoding="utf-8") as file:
    for line in file:
        count += 1
        key, value = line.split()
        d[key] = int(value)


with open("example3.txt", "r", encoding="utf-8") as file:
    print(f"Общий список сотрудников и окладов из файла:\n{file.read()}")
midl_prof = (sum(d.values())) / count
print(f"Средний доход на {count} сотрудников {midl_prof}\n")
for key, value in d.items():
    if value < 20000:
        print(f"Оклады менее 20 т.р. : {key}, {value}")
