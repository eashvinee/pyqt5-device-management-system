
import PyQt5.QtCore
import PyQt5.uic
import PyQt5.QtGui
from PyQt5.QtWidgets import *
import sys
import sqlite3

from src.AddEmployee import AddEmployee


class Main(QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        self.ui=PyQt5.uic.loadUi('ui/Welcome.ui', self)
        #self.setWindowFlags(PyQt5.QtCore.Qt.FramelessWindowHint) 
        self.setWindowIcon(PyQt5.QtGui.QIcon('balloon.svg')) 

        self.ui.actionAdd_New_Employee.triggered.connect(self.action_Add_New_Employee)    
        #print(dir(self.ui.actionAdd_New_Employee.triggered))
        #'actionAdd_New_Brand', 'actionAdd_New_Device', 'actionAdd_New_Employee', 'actionAll_Brand', 'actionAll_Devices', 'actionAll_Employee', 'actionAssign_Device', 'actionBrand', 'actionDevices_History'

        self.connDB = sqlite3.connect('DeviceDatabase.db')


        self.developedBy()
        

        self.show()

    def action_Add_New_Employee(self, action):
        self.addEmployee= AddEmployee(self)    

    def developedBy(self):
        #pass
        developedby = self.ui.developedby # Find the button
        developedby.setText("<a href='https://github.com/eashvinee'>github:eashvinee</a>")
        developedby.setOpenExternalLinks(True)


  

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Main()
    app.exec_()
