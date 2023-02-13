def menu():
    print('Глевное меню.\n'
          '1 - просмотр всех заметок\n'
          '2 - выборка по дате\n'
          '3 - добавление заметки\n'
          '4 - редактирование заметки\n'
          '5 - удаление заметки\n'
          '0 - выход из программы\n')


def menu_inp(num):
    while True:
        num = check_digit('Введите пункт меню: ')
        if num not in range(0, num + 1):
            print('Такого пункта меню нет')
        else:
            return num


def note_edit_menu():
    print("1 - изменить название\n"
          "2 - изменить содержание\n"
          "0 - отмена")


def check_digit(msg):
    while True:
        num = input(msg)
        if not num.isdigit():
            print('Значение должно содержать только цифры, повторите ввод. ', end='')
        else:
            break
    return int(num)
