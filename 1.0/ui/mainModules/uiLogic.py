#for the app
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import appSetup

#mainWindow
from appSetup import MainWindow, mainUi, app

#foodFind window
from appSetup import foodWin, foodWindowUi, foodFindWin

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
    food.food_in_window()
    foodWin.show()

#app logic
mainUi.pushButton.clicked.connect(except1)

#Run main loop
sys.exit(app.exec_())
