import csv

def dictionary_create():
    with open("phonebook.csv", mode="w", encoding='utf-8') as file:
        file_writer = csv.writer(file, delimiter = ",", lineterminator="\r")
        file_writer.writerow(["Фамилия", "Имя",   "Телефон",      "Описание"])
        file_writer.writerow(["Иванов", "Иван", "375-17-398-88-75", "Рабочий телефон"])
        file_writer.writerow(["Сидоров", "Петр", "375-17-246-55-17", "Домашний телефон"])
        file_writer.writerow(["Петров", "Анатолий", "375-17-748-55-78", "Рабочий телефон"])
        file_writer.writerow(["Александров", "Иван", "375-17-555-32-21", "Домашний телефон"])
        file_writer.writerow(["Леонова", "Инна", "375-17-174-12-00", "Рабочий телефон"])
