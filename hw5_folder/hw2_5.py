""" 2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строк"""


count_string = 0
with open("example.txt", "r") as f_obj:
    print(f"{f_obj.read()}\n")
with open("example.txt", "r") as f_obj:
    for i in f_obj.readlines():
        i = i.split()
        count_words = 0
        for i1 in i:
            count_words += 1
        count_string += 1
        print(f"В строке {count_string} , количество слов = {count_words}")
