
import PyQt5.QtCore
import PyQt5.uic
import PyQt5.QtGui
from PyQt5.QtWidgets import *
import sys
import sqlite3

from src.AddEmployee import AddEmployee
from src.AllEmployee import AllEmployee

from src.AddBrand import AddBrand
from src.AllBrand import AllBrand

class Main(QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        self.ui=PyQt5.uic.loadUi('ui/Welcome.ui', self)
        #self.setWindowFlags(PyQt5.QtCore.Qt.FramelessWindowHint) 
        self.setWindowIcon(PyQt5.QtGui.QIcon('balloon.svg')) 
        
        self.addEmployee =None
        self.allEmployee =None

        self.addBrand = None
        self.allBrand = None

        self.ui.actionAdd_New_Employee.triggered.connect(self.action_Add_New_Employee)    
        self.ui.actionAll_Employee.triggered.connect(self.action_All_Employee)    

        self.ui.actionAdd_New_Brand.triggered.connect(self.action_Add_New_Brand)    
        self.ui.actionAll_Brand.triggered.connect(self.action_All_Brand)    

        #print(dir(self.ui.actionAdd_New_Employee.triggered))
        #'actionAdd_New_Brand', 'actionAdd_New_Device', 'actionAdd_New_Employee', 'actionAll_Brand', 'actionAll_Devices', 'actionAll_Employee', 'actionAssign_Device', 'actionBrand', 'actionDevices_History'

        self.connDB = sqlite3.connect('DeviceDatabase.db')


        self.developedBy()
        

        self.show()

    def action_Add_New_Employee(self, action):
        if not isinstance(self.addEmployee,  AddEmployee):
            self.addEmployee= AddEmployee(self) 
        else:
            self.addEmployee.activateWindow()   


    def action_All_Employee(self, action):
        if not isinstance(self.allEmployee,  AllEmployee):
            self.allEmployee= AllEmployee(self) 
        else:
            self.allEmployee.activateWindow()   

    #action_Add_New_Brand
    def action_Add_New_Brand(self, action):
        if not isinstance(self.addBrand,  AddBrand):
            self.addBrand= AddBrand(self) 
        else:
            self.addBrand.activateWindow()   

    def action_All_Brand(self, action):
        if not isinstance(self.allBrand,  AllBrand):
            self.allBrand= AllBrand(self) 
        else:
            self.allBrand.activateWindow()   


    def developedBy(self):
        #pass
        developedby = self.ui.developedby # Find the button
        developedby.setText("<a href='https://github.com/eashvinee'>github:eashvinee</a>")
        developedby.setOpenExternalLinks(True)


  

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Main()
    app.exec_()
