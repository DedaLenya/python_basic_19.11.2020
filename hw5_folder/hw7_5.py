"""7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста."""

import json


with open('firm_json.json', 'w', encoding='UTF-8') as file_json:
    with open('example7.txt', 'r', encoding='UTF-8') as file:
        some_dict = {}
        aver_dict = {}
        count_profit_comp, total_profit = 0, 0
        for line in file:

            line = list(line.split())
            some_dict[line[0]] = int(line[2]) - int(line[3])
            profit = int(line[2]) - int(line[3])
            if profit >= 0:
                total_profit += profit
                count_profit_comp += 1
        try:
            aver_dict['average_profit'] = total_profit / count_profit_comp
        except ZeroDivisionError:
            aver_dict['average_profit'] = 0

        profits = some_dict.values()
        data_result = [some_dict, aver_dict]

    json.dump(data_result, file_json)
