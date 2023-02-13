from view import menu
from data.note import Note
from data import note
from util import csv_writer_reader


def button_click():
    point = -1
    actual_notes = note.convert_data_from_file_to_objects_note(csv_writer_reader.read_from_file())
    while point != 0:
        menu.menu()
        point = int(menu.menu_inp(5))
        if point == 1:
            print("Текущие заметки:")
            for i in actual_notes:
                print(i, "\n")
        elif point == 2:
            pass  # search
        elif point == 3:
            new_note = note.create_note()
            if new_note:
                actual_notes.append(new_note)
                csv_writer_reader.write_to_file(actual_notes)
        elif point == 4:
            pass  # edit
        elif point == 5:
            pass  # delete
        if point != 0:
            input('Для возврата в главное меню введите любой символ.\n')
    else:
        print('Завершение работы программы.')
