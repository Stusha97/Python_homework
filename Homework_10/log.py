import datetime

def write (expression, result):
    with open ("logging.txt",'a',encoding = 'utf-8') as i:
        i.write(f'\t {expression} = {result},{datetime.datetime.now()}'"\n")
