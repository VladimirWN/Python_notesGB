import datetime


def check_digit(msg):
    while True:
        num = input(msg)

        try:
            num = int(num)
        except ValueError:
            print('Значение должно содержать только цифры, повторите ввод. ')
        else:
            break
    return num


def choice_current_id(lst: list, current_id=-1):
    id_lst = [j.get_id() for j in lst]
    while True:
        if current_id in id_lst:
            return current_id
        elif current_id != -1:
            print("Данного ID нет.")
        print("id: ", id_lst)
        current_id = check_digit("ID искомой заметки: ")


def edit_note(lst: list):
    current_id = choice_current_id(lst)
    result_lst = list()
    for i in range(len(lst)):
        if current_id == lst[i].get_id():
            temp = lst[i]
            temp.edit_note()
            result_lst.append(temp)
        else:
            result_lst.append(lst[i])
    return result_lst


def delete_note(lst: list):
    current_id = choice_current_id(lst)
    for i in lst:
        if current_id == i.get_id():
            print(f"Заметка ID: {i.get_id()}, \"{i.get_title()}\" удалена!")
            lst.remove(i)
            return lst


def search_by_date(lst):
    while True:
        inp_date = input("Введите дату в формате: \"ГГГГ-ММ-ДД\": ")
        try:
            search_date = datetime.datetime.strptime(inp_date, "%Y-%m-%d")
        except ValueError:
            print("Неверный формат даты")
        else:
            break
    for i in lst:
        if search_date.date() == i.get_date().date():
            print(i)
