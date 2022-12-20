input_text = input('Введите символы для сжатия: ')
with open ('rle.txt', 'w') as data:
    data.write(input_text)

path = 'rle.txt'
data = open (path, 'r')
for line in data: 
    def rle (line):
        output_text = ' '
        i = 0
        while i < len(line):
            count = 1
            while i+1 < len(line) and line[i] == line [i+1]:
                count = count+1
                i = i+1
            output_text= output_text + str(count)+ line[i]
            i = i+1
        return output_text

with open ('rle1.txt', 'w') as data:
    data.write(rle(line))