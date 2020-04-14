# parse data base
import requests
from bs4 import BeautifulSoup
import openpyxl
def parser():
    print('Введите путь до файлов')
    fileList = [input(''),input(''),input(''),input(''),input(''),input('')]
    print('Введите ссылки')
    links = [input(''),input(''),input(''),input(''),input(''),input('')]
    institutionsNamesList = []
    institutionsAdressesList = []    
    linkCount = 0
    for j in fileList:      
        print("начинаю заполнение файла " + j)       
        #open xlsx file
        dataBase = openpyxl.load_workbook(filename = j)
        sheet = dataBase['dataBase']
        link = links[linkCount]
        print("link: " + link)
        print("linkCount: " + str(linkCount))
        pageNumber = 1
        for i in range(20):       
            getList = requests.get(link + str(pageNumber))
            gotList = BeautifulSoup(getList.text, 'html.parser')
            institutionNames = gotList.find_all('h2') #finding all names of institutions
            #find names
            for name in institutionNames: #appending all names into list
                name = name.a
                tag = name.string
                institutionsNamesList.append(str(tag))
            #find adresses
            adresses = gotList.find_all('div', class_= 'companies__item-address') #finding all adresses of institutions
            for adress in adresses: #appending all adresses into list
                adr = adress.string
                institutionsAdressesList.append(str(adr))
            pageNumber += 1
            print("pageNumber: " + str(pageNumber))
        #adding names and adresses into xlsx file    
        for c in range(len(institutionsNamesList)):
                sheet['A' + str((c+1))] = institutionsNamesList[c]
                dataBase.save(j)
        for f in range(len(institutionsAdressesList)):
                sheet['H' + str((f+1))] = institutionsAdressesList[f]
                dataBase.save(j)
        linkCount += 1
        print("файл заполнен")
        print("обнуляю переменные из цикла")
        pageNumber = 1
        institutionsNamesList = []
        institutionsAdressesList = []
        getList = None
        gotList = None
        institutionNames = None
        name = None
        tag = None
        adr = None
        adress = None
        adresses = None
        print("переменные обнулены")

#delete extra data
def delete():
    area = input('Введите район: ')
    paths = [
        'G:\Pytonchik\In progress\samAfisha\Code\dataBase\\areas\\' + area + '\coffe.xlsx',
        'G:\Pytonchik\In progress\samAfisha\Code\dataBase\\areas\\' + area + '\confect.xlsx',
        'G:\Pytonchik\In progress\samAfisha\Code\dataBase\\areas\\' + area + '\\fastFood.xlsx',
        'G:\Pytonchik\In progress\samAfisha\Code\dataBase\\areas\\' + area + '\pizza.xlsx',
        'G:\Pytonchik\In progress\samAfisha\Code\dataBase\\areas\\' + area + '\sushi.xlsx',
        'G:\Pytonchik\In progress\samAfisha\Code\dataBase\\areas\\' + area + '\\vegan.xlsx'
    ]
    for i in range(6):
        dataBase = openpyxl.load_workbook(filename = paths[i])
        sheet = dataBase['dataBase']
        for s in range (11, 200):
            print('deleting..')
            sheet['A' + str(s)] = None
            dataBase.save(paths[i])
            sheet['H' + str(s)] = None

parser()