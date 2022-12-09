from easygui import *
from model import *
import view

msg = 'Добро пожаловать в информационную систему "Закупки импортных комплектующих"'
title = "Информационная система"
button = "Начать работу"
msgbox (msg,title,button)

commands = ["Показать все данные", "Добавить данные","Выбрать данные по параметру"]

commands_start =[show_all,add_data,parameter]

parameter_buttons= ["контракты на сумму > 5000", "комплектующие из страны"]

def buttons():
    while True:
        res = buttonbox("Выберите одну из команд, нажав на соответствующую кнопку", choices=commands)
        if res is None:
            break
        elif res == "Выбрать данные по параметру":
            buttonbox("Выберите одну из команд, нажав на соответствующую кнопку", choices=parameter_buttons)
            result = parameter ()
            return result   
        else:
            commands_start[commands.index(res)]()
buttons() 