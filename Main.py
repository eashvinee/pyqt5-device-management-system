
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

from src.AddDevice import AddDevice
from src.AllDevice import AllDevice

from src.AssignDevice import AssignDevice


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

        self.addDevice = None
        self.allDevice = None

        self.assignDevice = None

        self.ui.actionAdd_New_Employee.triggered.connect(self.action_Add_New_Employee)    
        self.ui.actionAll_Employee.triggered.connect(self.action_All_Employee)    

        self.ui.actionAdd_New_Brand.triggered.connect(self.action_Add_New_Brand)    
        self.ui.actionAll_Brand.triggered.connect(self.action_All_Brand)    

        self.ui.actionAdd_New_Device.triggered.connect(self.action_Add_New_Device)    
        self.ui.actionAll_Devices.triggered.connect(self.action_All_Devices)    

        self.ui.actionAssign_Device.triggered.connect(self.action_assign_device)    

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


    #action_Add_New_Device
    def action_Add_New_Device(self, action):
        if not isinstance(self.addDevice,  AddDevice):
            self.addDevice= AddDevice(self) 
        else:
            self.addDevice.activateWindow()   

    #action_All_Devices
    def action_All_Devices(self, action):
        if not isinstance(self.allDevice,  AllDevice):
            self.allDevice= AllDevice(self) 
        else:
            self.allDevice.activateWindow()  
             

    #action_assign_device
    def action_assign_device(self, action):
        if not isinstance(self.assignDevice,  AssignDevice):
            self.assignDevice= AssignDevice(self) 
        else:
            self.assignDevice.activateWindow()   


    def developedBy(self):
        #pass
        developedby = self.ui.developedby # Find the button
        developedby.setText("<a href='https://github.com/eashvinee'>github:eashvinee</a>")
        developedby.setOpenExternalLinks(True)


  

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Main()
    app.exec_()
