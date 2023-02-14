from view import menu
from data import note
from util import csv_writer_reader
import service.service as sv


def button_click():
    point = -1
    actual_notes = note.convert_data_from_file_to_objects_note(csv_writer_reader.read_from_file())
    while point != 0:
        menu.menu()
        point = int(menu.menu_inp(5))
        if point == 1:
            print_actual_notes(actual_notes)  # print all notes
            select_note(actual_notes)  # select one note
        elif point == 2:
            sv.search_by_date(actual_notes)  # search by date
        elif point == 3:
            new_note = note.create_note()  # add note
            if new_note:
                actual_notes.append(new_note)
                csv_writer_reader.write_to_file(actual_notes)
        elif point == 4:
            print_actual_notes(actual_notes)  # edit note
            actual_notes = sv.edit_note(actual_notes)
            csv_writer_reader.write_to_file(actual_notes)
        elif point == 5:
            print_actual_notes(actual_notes)  # delete note
            actual_notes = sv.delete_note(actual_notes)
            csv_writer_reader.write_to_file(actual_notes)
        if point != 0:
            input('Для возврата в главное меню введите любой символ.\n')
    else:
        print('Завершение работы программы.')


def print_actual_notes(lst):
    print("Текущие заметки:")
    for i in lst:
        print(f"ID: {i.get_id()}, Название: \"{i.get_title()}\", дата изменения: {i.get_simple_date()}")


def select_note(lst):
    current_id = sv.check_digit("Развернуть заметку? (введите ID заметки / для отмены - \"-1\": ")
    if current_id != -1:
        current_id = sv.choice_current_id(lst, current_id)
        for i in lst:
            if current_id == i.get_id():
                print(i)
                return
