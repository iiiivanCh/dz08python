

def get_add_user(data: list) -> list:
    if not data:
        user: dict = {}
        user['ФИО'] = input('Введите ФИО: ')
        user['ФИО'] = user['ФИО'].title()
    else:
        sample = data[0]
        user = {}
        for i in sample:
            user[i] = input(f'Введите {i}: ')
            if i == 'ФИО':
                user[i] = user[i].title()
            else:
                user[i] = user[i].capitalize()
    data.append(user)
    return data
