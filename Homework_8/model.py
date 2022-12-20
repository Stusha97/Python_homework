import csv
import view
from dictionary_1 import *


def show_all ():
     with open("import_parts.csv", encoding='utf-8') as r_file:
        file_reader = csv.DictReader(r_file, delimiter = "|")
        for row in file_reader:
            print (row)

def add_data ():
    with open("import_parts.csv", mode="a", encoding='utf-8') as w_file:
            file_writer = csv.DictWriter(w_file, delimiter = "|", lineterminator="\r",fieldnames=names)
            i = input('Введите данные через пробел в формате: Номер изделия, Изделие, Страна,\
            Годовая потребность в шт, Номер контракта в виде списка,Сумма контракта: ').split (' ')
            a=dict(zip(names,i))
            file_writer.writerow (a)
  

def parameter ():
    choice = int(view.choice_parameter())
    with open("import_parts.csv", encoding='utf-8') as r_file:
        file_reader = csv.DictReader(r_file, delimiter = "|")
        if choice == 1:
            for row in file_reader:
                if int(row['Сумма контракта']) > 5000:
                    print(row['Сумма контракта'])
        elif choice == 2:
            country = input('Выберите страну из списка:')
            for row in file_reader:
                if row['Страна'] == country:
                    print(row)
