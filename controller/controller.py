from view import menu
from data.note import Note


def button_click():
    point = -1
    while point != 0:
        menu.menu()
        point = int(menu.menu_inp(5))
        if point == 1:
            pass  # all list
        elif point == 2:
            pass  # search
        elif point == 3:
            pass  # add
        elif point == 4:
            pass  # edit
        elif point == 5:
            pass  # delete
        if point != 0:
            input('Для возврата в главное меню введите любой символ.\n')
    else:
        print('Завершение работы программы.')

button_click()