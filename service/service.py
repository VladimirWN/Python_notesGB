from data.note import Note


def check_digit(msg):
    while True:
        num = input(msg)
        if not num.isdigit():
            print('Значение должно содержать только цифры, повторите ввод. ', end='')
        else:
            break
    return int(num)


def choice_current_id(lst: list):
    id_lst = [j.get_id() for j in lst]
    print(id_lst)
    while True:
        current_id = check_digit("ID искомой заметки: ")
        if current_id in id_lst:
            return current_id
        else:
            print("Данного ID нет.")


def edit_note(lst: list):
    current_id = choice_current_id(lst)
    for i in lst:
        if current_id == i.get_id():
            i = Note.edit_note(i)
            return lst


def delete_note(lst: list):
    current_id = choice_current_id(lst)
    for i in lst:
        if current_id == i.get_id():
            print(f"Заметка ID: {i.get_id()}, \"{i.get_title()}\" удалена!")
            lst.remove(i)
            return lst
