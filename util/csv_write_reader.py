import csv


def write_to_file(lst: list):
    with open("../data.csv", 'w', encoding="UTF-8", newline='') as f:
        writer = csv.writer(f, delimiter=';')
        writer.writerows(lst)

