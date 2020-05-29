#to work with exel
import openpyxl
#to parse
import requests
from bs4 import BeautifulSoup
#connetc to the app
from appSetup import mainUi
from appSetup import foodWindowUi

#set User's price
def price():
    lowPrice = mainUi.lineEdit_5.text()
    highPrice = mainUi.lineEdit_4.text()
    try:
        int(lowPrice)
        int(highPrice)
        linkPart = "&price_min=" + str(lowPrice) + "&price_max=" + str(highPrice) #this the part of a link witch will be send to the web-site
        return linkPart
    except:
        return ""
    

def cat():
    #cat is an identifier of food (422 is coffe, 424 is confect etc.)
    if mainUi.comboBox_2.currentText() == "СУШИ":
        catInd = "288"
    if mainUi.comboBox_2.currentText() == "ПИЦЦА":
        catInd = "425"
    if mainUi.comboBox_2.currentText() == "БУРГЕРЫ":
        catInd = "418"
    if mainUi.comboBox_2.currentText() == "КОФЕЙНЯ":
        catInd = "422"
    if mainUi.comboBox_2.currentText() == "КОНДИТЕРСКАЯ":
        catInd = "424"
    if mainUi.comboBox_2.currentText() == "ВЕГЕТАРИАНСКОЕ ПИТАНИЕ":
        catInd = "303"
    return catInd

def area():
    if mainUi.comboBox.currentText() == "ЦЕНТРАЛЬНЫЙ":
        area = "tsentralnyiy"
    if mainUi.comboBox.currentText() == "КУРЧАТОВСКИЙ":
        area = "kurchatovskiy"
    if mainUi.comboBox.currentText() == "ЛЕНИНСКИЙ":
        area = "leninskiy"
    if mainUi.comboBox.currentText() == "ТРАКТОРОЗАВОДСКИЙ":
        area = "traktorozavodskiy"
    if mainUi.comboBox.currentText() == "СОВЕТСКИЙ":
        area = "sovetskiy"
    if mainUi.comboBox.currentText() == "МЕТАЛЛУРГИЧЕСКИЙ":
        area = "metallurgicheskiy"
    if mainUi.comboBox.currentText() == "КАЛИНИНСКИЙ":
        area = "kalininskiy"
    return area

#this function is needed to cut Institutions's names in find_open and show_food
def string_cut(string):
    stringCopy = string[1:]
    for i in string[1:]:        
        if i == " ":
            stringCopy = "" + stringCopy[1:]
        if i != " ":
            break
    o = len(stringCopy)-1
    for i in stringCopy[::-1]:
        if i == " ":
            stringCopy =  stringCopy[:o]
            o -=1
        if i != " ":
            break
    return stringCopy

#check if institution is open
def find_open():
    opened = ['companies__item-working-status', 'is-color-green'] 
    closed = ['companies__item-working-status', 'is-color-red']
    openedInst = {}
    for page in range(20):
        parseLink = "https://www.yell.ru/cheliabinsk/top/restorany/" + area() + "/" + "?cat=" + str(cat) + price() + "&page=" + str(page)
        print("page: " + str(page))
        link = requests.get(parseLink)
        parseObj = BeautifulSoup(link.text, "html.parser")
        
        allInstStatuses = parseObj.find_all('span', class_= 'companies__item-working-status')
        allInstNames = parseObj.find_all('a', class_= 'companies__item-title-text')
        allInstAdresses = parseObj.find_all('div', class_= 'companies__item-address')

        if allInstStatuses == []:
            break
        else:
            for count in range(len(allInstStatuses)):
                if allInstStatuses[count].attrs["class"] == opened:
                    openedInst[string_cut(allInstNames[count].string)] = string_cut(allInstAdresses[count].string)
                if allInstStatuses[count].attrs["class"] == closed:
                    pass
    return openedInst

#if user didn't choose opened institutions
def show_food():
    filePath = "G:\\Pytonchik\\In progress\\samAfisha\\1.0\\dataBase\\areas\\" + area() + "\\" + str(cat()) + ".xlsx"
    dataBase = openpyxl.load_workbook(filename = filePath)
    sheet = dataBase["dataBase"]
    instList = []
    adressList = []
    for institution in range(1, 200):
        if sheet["A" + str(institution)].value != None:
            instList.append(string_cut(sheet["A" + str(institution)].value))
        if sheet["A" + str(institution)].value == None:
            break
    for adress in range(1,200):
        if sheet["H" + str(adress)].value != None:
            adressList.append(string_cut(sheet["H" + str(adress)].value))
        if sheet["H" + str(adress)].value == None:
            break
        
    foodVoc = dict(zip(instList, adressList))
    return foodVoc

def food_in_window():
    names = [foodWindowUi.Name, foodWindowUi.Name_2, foodWindowUi.Name_3, foodWindowUi.Name_4, foodWindowUi.Name_5, foodWindowUi.Name_6, foodWindowUi.Name_7, foodWindowUi.Name_8, foodWindowUi.Name_9, foodWindowUi.Name_10, foodWindowUi.Name_11, foodWindowUi.Name_12,
    foodWindowUi.Name_13,  foodWindowUi.Name_14, foodWindowUi.Name_15]

    adresses = [foodWindowUi.adress, foodWindowUi.adress_2, foodWindowUi.adress_3, foodWindowUi.adress_4, foodWindowUi.adress_5, foodWindowUi.adress_6, foodWindowUi.adress_7, foodWindowUi.adress_8, foodWindowUi.adress_9, foodWindowUi.adress_10, foodWindowUi.adress_11,
    foodWindowUi.adress_12, foodWindowUi.adress_13,  foodWindowUi.adress_14, foodWindowUi.adress_15]
    
    if mainUi.checkBox_4.isChecked():
        opened = True
    if not mainUi.checkBox_4.isChecked():
        opened = False

    if opened:
        openedLabels = find_open()
    
    if not opened:
        openedLabels = show_food()

    i = 0
    numberOfShows = 0 # this variable tells you how many inst have been showed
    for nameLabel in openedLabels:
        if i > len(names)-1:
            numberOfShows += i-1
            i = 0
            break
        names[i].setText(nameLabel)
        i+=1
    for adressLabel in openedLabels:
        if i > len(adresses)-1:
            break
        adresses[i].setText(openedLabels[adressLabel])
        i+=1
