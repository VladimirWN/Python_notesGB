import datetime
from view import menu


class Note:
    u_id = 0

    def __init__(self, title, text):
        self.__title = title
        self.__text = text
        Note.u_id += 1
        self.__id = Note.u_id
        self.__update_date = datetime.datetime.now()

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
            .format(self.__id, self.__title, datetime.datetime.strftime(self.__update_date, "%d.%m.%y %H:%M"),
                    self.__text)


def check_title(msg):
    inp = str(input(msg))
    while True:
        if inp or inp.isspace():
            return inp
        else:
            print("Название не может быть пустым.")
            inp = str(input(msg))


def create_note():
    title = check_title("Введите название заметки: ")
    text = input("Текст заметки: ")
    print(f"Название: {title}\nТекст:\n{text}\nПодтверждаете создание новой заметки (y/n)?")
    if input() == "y":
        print("Заметка создана!")
        return Note(title, text)
    else:
        print("Отмена добавления заметки.")
