#import PyQt5.QtCore
from PyQt5.QtCore import *
import PyQt5.uic
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import threading
import time
import sys

class AllEmployee(QWidget):
    def __init__(self, pself):
        self.pself=pself
        super(AllEmployee, self).__init__()
        self.ui=PyQt5.uic.loadUi('ui/AllEmployee.ui', self)
        self.setWindowIcon(PyQt5.QtGui.QIcon('balloon.svg')) 
        self.setWindowFlags(PyQt5.QtCore.Qt.WindowCloseButtonHint)

        self.view=self.ui.tableWidget
        #father_name, emp_id,, address, img
        rows =  self.pself.connDB.execute("SELECT ID, emp_name,  mobile, email FROM tbl_employee").fetchall()

        for row in rows:
            r = self.view.rowCount()
            self.view.setRowCount(r + 1)
            self.view.setItem(r, 0,  QTableWidgetItem(str(row[0])))
            self.view.setItem(r, 1,  QTableWidgetItem(row[1]))
            self.view.setItem(r, 2,  QTableWidgetItem(row[2]))
            self.view.setItem(r, 3,  QTableWidgetItem(row[3]))
    
        self.view.resizeColumnsToContents()
        self.show()

    def closeEvent(self, event):
        self.pself.allEmployee=None
        self.pself.activateWindow() 


