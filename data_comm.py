import os
import menu
import jf
import add_key as ak
import add_user as us
import print_user as pu
import data_sorted as ds
import search_user as su


def clear(): return os.system('cls')


def data_comm():
    exit_ = True
    data_flag = False
    data = jf.read_file("data_file.json")
    if data == []:
        data_flag = True
    while exit_:
        if data_flag:
            what = 3
            data_flag = False
        else:
            what = menu.menu()
        if what == 1:
            clear()
            pu.get_print_user_for_one(data)
            jf.write_file(data)
            clear()
        elif what == 2:
            clear()
            pu.get_print_user_all(data)
            clear()
        elif what == 3:
            if not data == []:
                clear()
            us.get_add_user(data)
            jf.write_file(data)
            clear()
        elif what == 4:
            clear()
            ak.get_add_key(data)
            jf.write_file(data)
            clear()
        elif what == 5:
            clear()
            ds.get_data_sorted(data)
            clear()
        elif what == 6:
            clear()
            su.get_search_user(data)
            jf.write_file(data)
            clear()
        else:
            jf.write_file(data, "data_file_reserve.json")
            exit_ = False


data_comm()
