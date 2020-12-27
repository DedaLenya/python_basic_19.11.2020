"""4 . Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую
построчно данные. При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""
my_dict = {
    "One": "Один",
    "Two": "Два",
    "Three": "Три",
    "Four": "Четыре"
}

with open("example4.txt", "r", encoding="utf-8") as file:
    with open("example4_1.txt", "w", encoding="utf-8") as final_file:
        lines = file.readlines()
        for line in lines:
            num_list = line.split(' — ')
            final_file.write(f'{my_dict[num_list[0]]} — {num_list[1]}')
with open("example4_1.txt", "r", encoding="utf-8") as final_file:
    print(final_file.read())
