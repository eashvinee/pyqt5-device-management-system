#import PyQt5.QtCore
from PyQt5.QtCore import *
import PyQt5.uic
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import threading
import time
import sys

class AllDevice(QWidget):
    def __init__(self, pself):
        self.pself=pself
        super(AllDevice, self).__init__()
        self.ui=PyQt5.uic.loadUi('ui/AllDevices.ui', self)
        self.setWindowIcon(PyQt5.QtGui.QIcon('balloon.svg')) 
        self.setWindowFlags(PyQt5.QtCore.Qt.WindowCloseButtonHint)

        self.view=self.ui.tblAllDevices
        rows =  self.pself.connDB.execute("SELECT ID, brand_id, model_id, serial_number, manufature_year, buying_date FROM tbl_device").fetchall()

        for row in rows:
            r = self.view.rowCount()
            self.view.setRowCount(r + 1)
            self.view.setItem(r, 0,  QTableWidgetItem(str(row[0])))
            self.view.setItem(r, 1,  QTableWidgetItem(str(row[1])))
            self.view.setItem(r, 2,  QTableWidgetItem(str(row[2])))
            self.view.setItem(r, 3,  QTableWidgetItem(row[3]))
            self.view.setItem(r, 4,  QTableWidgetItem(row[4]))
            self.view.setItem(r, 5,  QTableWidgetItem(row[5]))
    
        self.view.resizeColumnsToContents()
        self.show()

    def closeEvent(self, event):
        self.pself.allDevice=None
        self.pself.activateWindow() 


