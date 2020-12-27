"""1. Создать программно файл в текстовом формате, записать в него построчно данные,
вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка. """


def new_data_string(my_file):
    """
    Файл создасться програмно, в него будут записаны строки через энтер, окончанием будет пустой энтер.
    :param my_file: Передаем в функцию называние создаваемого файла
    :return:
    """
    f = open(f"{my_file}.txt", "w")
    while True:
        some_text = str(input("Введите текст>>"))
        if some_text == "":
            break
        f.writelines([some_text, "\n"])
    f.close()

    f = open(f"{my_file}.txt", "r")

    print(f.read())
    f.close()


new_data_string("remove_me_after")
