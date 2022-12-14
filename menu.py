import user_number as un


def menu() -> int:
    print('------------------------------\n'
          '  БАЗА ФИРМЫ "РОГА И КОПЫТА"\n'
          '------------------------------\n'
          '1 - вывод базы по одному сотруднику для ознакомления или корректировки\n'
          '2 - вывод всей базы для ознакомления\n'
          '3 - ввод нового сотрудника\n'
          '4 - ввод нового поля\n'
          '5 - сортировка\n'
          '6 - поиск по ФИО и корректировка данных сотрудника\n'
          '0 - выход\n'
          '-------------------------\n')
    num_user = un.get_user_number(
        'Какую операцию выполняем? - ', [1, 2, 3, 4, 5, 6, 0])
    return num_user
