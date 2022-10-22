import json
import os


def read_file(filename):
    if os.path.exists(filename):
        with open(filename, "r", encoding='utf8') as read_file:
            data = json.load(read_file)
    else:
        data = []
        print('------------------------------\n'
              '  БАЗА ФИРМЫ "РОГА И КОПЫТА"\n'
              '------------------------------\n'
              ' ПРИВЕТ! НАЧИНАЕМ НОВУЮ БАЗУ!\n'
              '------------------------------\n'
              'введите данные первого сотрудника\n')
    return data


def write_file(data, file_reserve="data_file.json"):
    with open(file_reserve, "w", encoding='utf8') as write_file:
        json.dump(data, write_file, ensure_ascii=False, indent=4)
