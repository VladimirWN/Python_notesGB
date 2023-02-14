import datetime
from view import menu


class Note:
    u_id = 0

    def __init__(self, title, text):
        self.__title = title
        self.__text = text
        Note.u_id += 1
        self.__uid = Note.u_id
        self.__update_date = datetime.datetime.now()
        self.__index = 0
        self.__items_lst = [self.__uid, self.__title, self.__text, self.__update_date]

    def edit_note(self):
        point = -1
        while point != 0:
            menu.note_edit_menu()
            point = int(menu.menu_inp(2))
            if point == 1:
                self.__title = check_title("Введите новое название: ")
            elif point == 2:
                self.__text = input("Введите новый текст заметки: ")
            elif point == 0:
                print("Отмена изменений.")
        self.__update_date = datetime.datetime.now()

    def __str__(self) -> str:
        return "ID: {}\nНазвание: {}\nВремя последнего изенения: {}\nСодержание заметки: {}"\
            .format(self.__uid, self.__title, datetime.datetime.strftime(self.__update_date, "%d.%m.%y %H:%M"),
                    self.__text)

    def __iter__(self):
        return self

    def __next__(self):
        if self.__index < 4:
            i = self.__index
            self.__index += 1
            return self.__items_lst[i]
        else:
            self.__index = 0
            raise StopIteration


def check_title(msg):
    inp = str(input(msg))
    while True:
        if inp.strip():
            return inp
        else:
            print("Название не может быть пустым.")
            inp = str(input(msg))


def create_note():
    title = check_title("Введите название новой заметки: ")
    text = input("Текст заметки: ")
    print(f"Название: {title}\nТекст:\n{text}\nПодтверждаете создание новой заметки (y/n)?")
    if input() == "y":
        print("Заметка создана!")
        return Note(title, text)
    else:
        print("Отмена добавления заметки.")


def convert_data_from_file_to_objects_note(lst: list):
    notes_lst = list()
    for i in lst:
        uid, title, text = i[0], i[1], i[2]
        date = datetime.datetime.strptime(i[3], "%Y-%m-%d %H:%M:%S.%f")
        note = Note(title, text)
        note.__uid = uid
        note.__update_date = date
        Note.u_id = int(uid)
        notes_lst.append(note)
    return notes_lst
