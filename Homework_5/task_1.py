# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
input_text = input('Введите через пробел текст со словами, содержащими "абв":')
print (input_text)
output_text = [x for x in input_text.split() if 'абв' not in x ]
print (' '.join(output_text))