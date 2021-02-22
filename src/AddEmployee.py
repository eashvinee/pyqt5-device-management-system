#import PyQt5.QtCore
from PyQt5.QtCore import *
import PyQt5.uic
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import threading
import time
import sys

class AddEmployee(QWidget):
    def __init__(self, pself):
        self.pself=pself
        super(AddEmployee, self).__init__()
        self.ui=PyQt5.uic.loadUi('ui/AddEmployee.ui', self)
        self.setWindowIcon(PyQt5.QtGui.QIcon('balloon.svg')) 
        self.setWindowFlags(PyQt5.QtCore.Qt.WindowCloseButtonHint)

        print(dir(self.ui))
        #'lblAddEmpAddress', 'lblAddEmpEmail', 'lblAddEmpFather', 'lblAddEmpHeading', 'lblAddEmpID', 'lblAddEmpImage', 'lblAddEmpImgContainer', 'lblAddEmpMobile', 'lblAddEmpName', 'leAddEmpEmail', 'leAddEmpFather', 'leAddEmpID', 'leAddEmpMobile', 'leAddEmpName','teAddEmpAddress'
        #btnAddEmpBrowseImage', 'btnAddEmpImageRemove', 'btnAddEmpSave'
        self.ui.btnAddEmpSave.clicked.connect(self.btn_addEmpSave)

        self.show()

    def btn_addEmpSave(self):
        #pass
        emp={}
        emp['emp_name']=self.ui.leAddEmpName.text()
        emp['father_name']=self.ui.leAddEmpFather.text()
        emp['emp_id']=self.ui.leAddEmpID.text()
        emp['mobile']=self.ui.leAddEmpMobile.text()
        emp['email']=self.ui.leAddEmpEmail.text()
        emp['address']=self.ui.teAddEmpAddress.toPlainText()
        emp['img']=''
        self.insert_emplyoee(emp)
        #print(emp)

    def insert_emplyoee(self, emp):
        #pass
        #print(self.pself.connDB)
        self.pself.connDB.execute("INSERT INTO tbl_employee (emp_name, father_name, emp_id, mobile, email, address, img) VALUES (:emp_name, :father_name, :emp_id, :mobile, :email, :address, :img )",(emp['emp_name'], emp['father_name'], emp['emp_id'], emp['mobile'], emp['email'],  emp['address'], emp['img']));        
        self.pself.connDB.commit()
        print("insert into database successfully")


"""
CREATE TABLE tbl_employee(
    ID NTEGER PRIMARY KEY AUTOINCREMENT,
    emp_name text,
    father_name text,
    emp_id text,
    mobile text,
    email text,
    address text,
    img text
)

"""