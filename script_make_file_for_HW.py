def make_file_for_HW(num_less, qty_task):
    """Создает в каталоге скрипта структурированые файлы для ДЗ
    :param qty_task: Количество заданий в текущем уроке
    :param num_less: Номер урока или ДЗ
    :return:
    """
    count = 0
    for i in range(qty_task):
        count += 1
        f = open(f"hw{num_less}_{count}.py", "x")
        f.close()
    return None


make_file_for_HW(6, 5)
