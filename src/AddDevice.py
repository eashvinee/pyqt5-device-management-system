#import PyQt5.QtCore
from PyQt5.QtCore import *
import PyQt5.uic
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import threading
import time
import sys

from src.AllDevice import AllDevice


class AddDevice(QWidget):
    def __init__(self, pself):
        self.pself=pself
        super(AddDevice, self).__init__()
        self.ui=PyQt5.uic.loadUi('ui/AddNewDevices.ui', self)
        self.setWindowIcon(PyQt5.QtGui.QIcon('balloon.svg')) 
        self.setWindowFlags(PyQt5.QtCore.Qt.WindowCloseButtonHint)

        #print(dir(self.ui))

        #cbAddDeviceBrand, cbAddDeviceModal, leAddDeviceNumber, deAddDeviceManufatureYear, deAddDeviceBuyingDate, btnAddDeviceBrowse, btnAddDeviceSave

        #print(dir(self.ui.cbAddBrandParent))
        #rows =  self.pself.connDB.execute("SELECT ID, title FROM tbl_brand WHERE parent=0").fetchall()

        #for row in rows:
            #self.ui.cbAddBrandParent.addItem(row[1], row[0]);

        #self.ui.btnAddBrandSave.clicked.connect(self.btn_AddBrandSave)

        self.show()

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
        #self.pself.connDB.execute("INSERT INTO tbl_brand (title, parent) VALUES (:title, :parent)",(brand['title'], brand['parent']));        
        #self.pself.connDB.commit()
       # print("insert brand into database successfully")
        self.close()
        if not isinstance(self.pself.allDevice,  AllDevice):
            self.pself.allDevice= AllDevice(self.pself) 
        else:
            self.pself.allDevice.activateWindow()   



    def closeEvent(self, event):
        #pass
        self.pself.addDevice=None
        #self.pself.activateWindow() 


"""
CREATE TABLE tbl_brand(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    title text,
    parent INTEGER
)

"""