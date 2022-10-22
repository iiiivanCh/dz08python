

def get_search_user(data):
    user_search = input('\nВведите искомое: ')
    for user in data:
        if user_search in user['ФИО']:
            for key, value in user.items():
                print(f'{key}: {value}')
            what = input(
                '\nЖелаете внести изменения? (нет - Enter, да - д): ')
            print()
            if what == 'д':
                for key, value in user.items():
                    print(f'{key}: {value}')
                    item = input(f'{key}, правим? (нет - Enter, да - д): ')
                    if item == 'д':
                        user[key] = input(f'{key}: ')
                        if key == 'ФИО':
                            user[key] = user[key].title()
            else:
                return data
    return data
