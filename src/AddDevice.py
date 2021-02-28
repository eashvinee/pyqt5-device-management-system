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

        cbAddDeviceBrand=self.ui.cbAddDeviceBrand
        #print(dir(self.ui.cbAddDeviceBrand))
        rows =  self.pself.connDB.execute("SELECT ID, title FROM tbl_brand WHERE parent=0").fetchall()
        for row in rows:
            self.ui.cbAddDeviceBrand.addItem(row[1], row[0]);


        cbAddDeviceBrand.currentTextChanged.connect(self.cb_device_brand_changed)

        self.ui.btnAddDeviceSave.clicked.connect(self.btn_AddDeviceSave)

        self.show()

    def cb_device_brand_changed(self):
        cbdata=self.ui.cbAddDeviceBrand.currentData()
        self.ui.cbAddDeviceModal.clear()
        self.ui.cbAddDeviceModal.addItem('Select', None);
        rows =  self.pself.connDB.execute("SELECT ID, title FROM tbl_brand WHERE parent=:parent", (cbdata, )).fetchall()
        for row in rows:
            self.ui.cbAddDeviceModal.addItem(row[1], row[0]);


    def btn_AddDeviceSave(self):
        device={}
        device['brand_id']=self.ui.cbAddDeviceBrand.currentData()
        device['model_id']=self.ui.cbAddDeviceModal.currentData()
        device['serial_number']=self.ui.leAddDeviceNumber.text()
        device['manufature_year']=self.ui.deAddDeviceManufatureYear.text()
        device['buying_date']=self.ui.deAddDeviceBuyingDate.text()
        self.insert_device(device)


    def insert_device(self, device):
        self.pself.connDB.execute("INSERT INTO tbl_device (brand_id, model_id, serial_number, manufature_year, buying_date) VALUES (:brand_id, :model_id, :serial_number, :manufature_year, :buying_date)",(device['brand_id'], device['model_id'], device['serial_number'], device['manufature_year'], device['buying_date']));        
        self.pself.connDB.commit()

        self.close()
        if not isinstance(self.pself.allDevice,  AllDevice):
            self.pself.allDevice= AllDevice(self.pself) 
        else:
            self.pself.allDevice.activateWindow()   


    def closeEvent(self, event):
        self.pself.addDevice=None
        self.pself.activateWindow() 


"""
CREATE TABLE tbl_device(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    brand_id INTEGER,
    model_id INTEGER,
    serial_number text,
    manufature_year text,
    buying_date INTEGER,
    images txt,
)

"""