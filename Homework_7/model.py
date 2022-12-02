import csv

def exp():
    with open("phonebook.csv", encoding='utf-8') as r_file:
        file_reader = csv.reader(r_file, delimiter = ",")
        a = input("Введите фамилию:")

        for line in file_reader:
                if a in line:
                    return line

def imp():
    with open("phonebook.csv", mode ="a",encoding='utf-8') as w_file:
        data_writer = csv.writer(w_file)
        i = input('Введите данные в формате Фамилия,Имя,Телефон, Комментарий:').split (',')
        data_writer.writerow(i)