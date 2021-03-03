#import PyQt5.QtCore
from PyQt5.QtCore import *
import PyQt5.uic
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import threading
import time
import sys

#from src.AllBrand import AllBrand


class AssignDevice(QWidget):
    def __init__(self, pself):
        self.pself=pself
        super(AssignDevice, self).__init__()
        self.ui=PyQt5.uic.loadUi('ui/AssignDevice.ui', self)
        self.setWindowIcon(PyQt5.QtGui.QIcon('balloon.svg')) 
        self.setWindowFlags(PyQt5.QtCore.Qt.WindowCloseButtonHint)
        #self.introspect(self.ui.leAssignDeviceEmpName)
        #textChanged
        #leAssignDeviceEmpName, leAssignDeviceEmpMobile, leAssignDeviceName, btnAssignDeviceSave
        self.ui.leAssignDeviceEmpName.keyPressEvent=self.assign_emp_name()
        #self.ui.leAssignDeviceEmpName.textChanged.connect(self.assign_emp_name)
        #print(dir(self.ui.cbAddBrandParent))
        #rows =  self.pself.connDB.execute("SELECT ID, title FROM tbl_brand WHERE parent=0").fetchall()
        #self.assign_emp_name()
        #for row in rows:
            #self.ui.cbAddBrandParent.addItem(row[1], row[0]);
        #print("aaaa")
        #self.ui.btnAddBrandSave.clicked.connect(self.btn_AddBrandSave)
        #print(dir(self.ui.leAssignDeviceEmpName))

        self.show()


    def assign_emp_name(self):
        emp_name=self.ui.leAssignDeviceEmpName.text()
        # WHERE emp_name LIKE :emp_name", ('%'+emp_name+'%', )
        rows =  self.pself.connDB.execute("SELECT ID, emp_name FROM tbl_employee WHERE emp_name LIKE :emp_name", ('%'+emp_name+'%', )).fetchall()    
        #rows =  self.pself.connDB.execute("SELECT ID, emp_name FROM tbl_employee").fetchall()    

        names =list() 

        for row in rows:
            if row[1]:
                names.append(row[1]+'-'+str(row[0]))

        #print(names)
        completer = QCompleter(names)
        completer.setCaseSensitivity(PyQt5.QtCore.Qt.CaseInsensitive)
        self.ui.leAssignDeviceEmpName.setCompleter(completer) 
        #self.ui.leAssignDeviceEmpName.textChanged.connect(self.select_emp_name)

        ###print(completer.completionPrefix())

        return True

    def select_emp_name(self):
        emp_name=self.ui.leAssignDeviceEmpName.text()
        print(emp_name)

    def btn_AddBrandSave(self):
        #pass
        brand={}
        brand['title']=self.ui.leAddBrandTitle.text()
        cbdata=self.ui.cbAddBrandParent.currentData()

        if cbdata:        
            brand['parent']=cbdata
        else:
            brand['parent']=0

        #print(brand)
        self.insert_brand(brand)
        #print(emp)

    def insert_brand(self, brand):
        #pass
        #print(self.pself.connDB)
        self.pself.connDB.execute("INSERT INTO tbl_brand (title, parent) VALUES (:title, :parent)",(brand['title'], brand['parent']));        
        self.pself.connDB.commit()
        print("insert brand into database successfully")
        self.close()
        if not isinstance(self.pself.allBrand,  AllBrand):
            self.pself.allBrand= AllBrand(self.pself) 
        else:
            self.pself.allBrand.activateWindow()   



    def closeEvent(self, event):
        #pass
        self.pself.assignDevice=None
        self.pself.activateWindow() 

    def introspect(self, obj):
      for func in [type, id, dir, vars, callable]:
        print("%s(%s):\t\t%s" % (func.__name__, self.introspect.__code__.co_varnames[0], func(obj)))
        


"""
CREATE TABLE tbl_brand(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    title text,
    parent INTEGER
)

"""