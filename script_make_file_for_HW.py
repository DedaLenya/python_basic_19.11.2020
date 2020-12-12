def make_file_for_HW(qty_task, num_less):
    """Создает в каталоге скрипта структурированые файлы для ДЗ
    :param qty_task: Количество заданий в текущем уроке
    :param num_less: Номер урока или ДЗ
    :return:
    """
    count = 0
    for i in range(qty_task):
        count += 1
        f = open(f"hw{count}_{num_less}.py", "x")
        f.close()
    return None


make_file_for_HW(2, 9)
