

def get_print_user_all(data):
    print('---------------------------------\n'
          ' ПЕРСОНАЛЬНЫЕ ДАННЫЕ СОТРУДНИКОВ\n'
          '---------------------------------\n')
    for user in data:
        for key, value in user.items():
            print(f'{key}: {value}')
        print('---------------------------------')
    input('Для выхода в меню нажмите Enter')


def get_print_user_for_one(data):
    print('---------------------------------\n'
          ' ПЕРСОНАЛЬНЫЕ ДАННЫЕ СОТРУДНИКОВ\n'
          '---------------------------------\n')
    for user in data:
        for key, value in user.items():
            print(f'{key}: {value}')
        what = input(
            '\nЖелаете внести изменения? (нет - Enter, да - д, вернуться в главное меню - ш): ')
        print()
        if what == 'д':
            for key, value in user.items():
                print(f'{key}: {value}')
                item = input(f'{key}, правим? (нет - Enter, да - д): ')
                if item == 'д':
                    user[key] = input(f'{key}: ')
                    if key == 'ФИО':
                        user[key] = user[key].title()
        elif what == 'ш':
            return data
    return data
