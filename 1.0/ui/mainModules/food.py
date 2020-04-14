#to work with exel
import openpyxl
#to parse
import requests
from bs4 import BeautifulSoup
#connetc to the app
from appSetup import ui

#set User's price
def price():
    lowPrice = ui.lineEdit_5.text()
    highPrice = ui.lineEdit_4.text()
    try:
        int(lowPrice)
        int(highPrice)
        linkPart = "&price_min=" + str(lowPrice) + "&price_max=" + str(highPrice) #this the part of a link witch will be send to the web-site
    except:
        linkPart = ""
    return linkPart

def cat():
    #cat is an identifier of food (422 is coffe, 424 is confect etc.)
    if ui.comboBox_2.currentText() == "СУШИ":
        catInd = "288"
    if ui.comboBox_2.currentText() == "ПИЦЦА":
        catInd = "425"
    if ui.comboBox_2.currentText() == "БУРГЕРЫ":
        catInd = "418"
    if ui.comboBox_2.currentText() == "КОФЕЙНЯ":
        catInd = "422"
    if ui.comboBox_2.currentText() == "КОНДИТЕРСКАЯ":
        catInd = "424"
    if ui.comboBox_2.currentText() == "ВЕГЕТАРИАНСКОЕ ПИТАНИЕ":
        catInd = "303"
    return catInd

def area():
    #areas
    if ui.comboBox.currentText() == "ЦЕНТРАЛЬНЫЙ":
        area = "tsentralnyiy"
    if ui.comboBox.currentText() == "КУРЧАТОВСКИЙ":
        area = "kurchatovskiy"
    if ui.comboBox.currentText() == "ЛЕНИНСКИЙ":
        area = "leninskiy"
    if ui.comboBox.currentText() == "ТРАКТОРОЗАВОДСКИЙ":
        area = "traktorozavodskiy"
    if ui.comboBox.currentText() == "СОВЕТСКИЙ":
        area = "sovetskiy"
    if ui.comboBox.currentText() == "МЕТАЛЛУРГИЧЕСКИЙ":
        area = "metallurgicheskiy"
    if ui.comboBox.currentText() == "КАЛИНИНСКИЙ":
        area = "kalininskiy"
    return area

#check if institution is open
def findOpen():
    #collecting amount os instituitions to know how many pages of web-site should be parsed
    filePath = "G:\\Pytonchik\\In progress\\samAfisha\\Code\\dataBase\\areas\\" + area() + "\\" + cat() + ".xlsx"
    dataBase = openpyxl.load_workbook(filename = filePath)
    sheet = dataBase["dataBase"]
    #cycle to know amount of institutions in .xlsx file
    amount = 0
    for instit in range(1, 200):
        if sheet["A" + str(instit)].value != None:
                amount = amount + 1
        if sheet["A" + str(instit)].value == None:
                break
    #amount of Institutions in every area is different, so it needed various identidier to be devided at
    if area() == "tsentralniy" or "kurchatovskiy" or "leninskiy" or "kalininskiy" or "traktorozavodskiy":
        areaIdent = 11
    if area() == "metallurgicheskiy" or "sovetskiy":
        areaIdent = 10    
    if cat() == 422: #coffe is the most whidespreaded institution
        areaIdent = 18
    amountPage = amount // areaIdent 
    #detect if open 
    openInstList = [] #all opened Institutions
    #css classes to check is institution opened or closed
    opened = ['companies__item-working-status', 'is-color-green'] 
    closed = ['companies__item-working-status', 'is-color-red']
    b = 1
    for page in range(1, amountPage):
        mainLink = "https://www.yell.ru/cheliabinsk/top/restorany/" + area() + "/" + "?cat=" + str(cat)+ price() + "&page=" + str(page)
        print("page: " + str(page))
        link = requests.get(mainLink)
        parseObj = BeautifulSoup(link.text, "html.parser")
        #find OPENED institutions
        allInst = parseObj.find_all('span', class_= 'companies__item-working-status')
        #exel row counter
        for inst in allInst:
            if sheet["A" + str(b)].value == None:
                break
            if inst.attrs["class"] == opened:
                print()
                openInstList.append(sheet["A" + str(b)].value)
                b += 1
            if inst.attrs["class"] == closed:
                b += 1
    return openInstList    

#if user didn't choose opened institutions
def showFood():
    filePath = "G:\\Pytonchik\\In progress\\samAfisha\\1.0\\dataBase\\areas\\" + area() + "\\" + str(cat()) + ".xlsx"
    dataBase = openpyxl.load_workbook(filename = filePath)
    sheet = dataBase["dataBase"]
    instList = []
    for institution in range(1, 200):
        if sheet["A" + str(institution)].value != None:
            instList.append(sheet["A" + str(institution)].value)
        if sheet["A" + str(institution)].value == None:
            break
    return instList