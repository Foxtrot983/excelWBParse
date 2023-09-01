import os
from openpyxl import load_workbook

from main import parse


def start():
    cwd = os.getcwd()
    book = load_workbook('Книга111.xlsx')
    sheet = book['Лист1']
    print(sheet.values)
    values = [x[0] for x in sheet.values]
    for i in values:
        #print(i)
        parse(i)
        #Тут переход дальше на парсинг
        
if __name__ == "__main__":
    start()