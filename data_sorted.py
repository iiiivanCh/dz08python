import print_user as pu


def get_option_sorted(data):
    print('---------------------------------\n'
          '     ВЫБЕРАЕМ ПОЛЯ СОРТИРОВКИ\n'
          '---------------------------------\n'
          '      нет - Enter, да - д\n')
    box = data[0]
    for key in box:
        option = input(f'Выбераем {key}? ')
        if option == '':
            continue
        else:
            return key
    option = input('Вы ничего не выбрали. Повторить? нет - Enter, да - д \n')
    if option == '':
        return False
    else:
        return get_option_sorted(data)


def get_data_sorted(data):
    option = get_option_sorted(data)
    if option:
        result = sorted(data, key=lambda x: x[option])
        pu.get_print_user_all(result)
