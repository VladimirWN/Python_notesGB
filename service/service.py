from data.note import Note


def check_digit(msg):
    while True:
        num = input(msg)
        if not num.isdigit():
            print('Значение должно содержать только цифры, повторите ввод. ', end='')
        else:
            break
    return int(num)


def edit_note(lst):
    id_lst = [i[0] for i in lst]
    while True:
        current_id = check_digit("ID изменяеймой заметки: ")
        if current_id in id_lst:
            break
        else:
            print("Данного ID нет.")
    for i in lst:
        if current_id == i[0]:
            i = Note.edit_note(i)
            break
    return lst
