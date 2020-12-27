"""Каждый следующий элемент ряда Фибоначчи получается при сложении
двух предыдущих. Начиная с 1 и 2, первые 10 элементов будут:
1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
Найдите сумму всех четных элементов ряда Фибоначчи,
которые не превышают четыре миллиона.
"""

new_list = [1,2]
vol = []
while True:
    summ = new_list[-1] + new_list[-2]
    if summ > 4000000:
        break
    new_list.append(summ)
for ind in new_list:
    if ind % 2 == 0:
        vol.append(ind)
print(sum(vol))

print(new_list)
