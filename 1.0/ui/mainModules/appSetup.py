from PyQt5 import QtCore, QtGui, QtWidgets
from appUi import appUi
from appUi import noAreaOrCatExceptionUi
import sys 

#MAIN WINDOW
#create app
app = QtWidgets.QApplication(sys.argv)
#create form and init ui
MainWindow = QtWidgets.QMainWindow()
application = appUi.Ui_MainWindow
ui = application()
ui.setupUi(MainWindow)
#set the size of the main window
MainWindow.setFixedSize(1025, 620) 
#main windo title
MainWindow.setWindowTitle("SamAfisha")

#noAreaOrCatException
Dialog = QtWidgets.QDialog()
except1 = noAreaOrCatExceptionUi.Ui_Dialog
uiExcept1 = except1()
uiExcept1.setupUi(Dialog)    