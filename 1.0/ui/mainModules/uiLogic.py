#for the app
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import appSetup
#mainWindow
from appSetup import MainWindow, ui, app
#noAreaOrCatException
from appSetup import Dialog
#module "food" need it
import requests
from bs4 import BeautifulSoup
import openpyxl
import food

#start main window
appSetup.MainWindow.show()

#hook logic
def except1():
    if ui.comboBox.currentText() == "РАЙОН":
        appSetup.Dialog.show()
    if ui.comboBox_2.currentText() == "ВИД ЕДЫ":
        appSetup.Dialog.show()
    else:
        #if you're editing this code, you can test food functions here
        food.showFood()
#app logic
#the first "НАЙТИ" button
ui.pushButton.clicked.connect(except1)

#Run main loop 
sys.exit(app.exec_())
