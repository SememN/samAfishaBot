from PyQt5 import QtCore, QtGui, QtWidgets
from appUi import appUi
from appUi import noAreaOrCatExceptionUi
from appUi import foodFind
import sys 

#MAIN WINDOW
#create app
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
mainWin = appUi.Ui_MainWindow
mainUi = mainWin()
mainUi.setupUi(MainWindow)

MainWindow.setFixedSize(1025, 620) 

MainWindow.setWindowTitle("SamAfisha")

#noAreaOrCatException
Dialog = QtWidgets.QDialog()
except1 = noAreaOrCatExceptionUi.Ui_Dialog
uiExcept1 = except1()
uiExcept1.setupUi(Dialog)    

#FOODFIND WINDOW
foodFindWin = QtWidgets.QApplication(sys.argv)
foodWin = QtWidgets.QWidget()
foodWindow = foodFind.Ui_FoodWin
foodWindowUi = foodWindow()
foodWindowUi.setupUi(foodWin)
