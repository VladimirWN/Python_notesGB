import csv


def write_to_file(lst: list):
    with open("../data.csv", 'w', encoding="UTF-8", newline='') as f:
        writer = csv.writer(f, delimiter=';')
        writer.writerows(lst)


def read_from_file():
    lst = list()
    with open("../data.csv", 'r', encoding="UTF=8") as f:
        reader = csv.reader(f)
        for row in reader:
            lst.append(row)
    return lst