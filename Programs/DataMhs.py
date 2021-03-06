# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frm_DataMhs.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from Edit import *

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(491, 647)
        self.formLayoutWidget = QtWidgets.QWidget(Form)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 430, 471, 143))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.lbl_nimMhs = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Iosevka Custom")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_nimMhs.setFont(font)
        self.lbl_nimMhs.setObjectName("lbl_nimMhs")
        self.verticalLayout_3.addWidget(self.lbl_nimMhs)
        self.lbl_namaMhs = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Iosevka Custom")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_namaMhs.setFont(font)
        self.lbl_namaMhs.setObjectName("lbl_namaMhs")
        self.verticalLayout_3.addWidget(self.lbl_namaMhs)
        self.lbl_jurusanMhs = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Iosevka Custom")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_jurusanMhs.setFont(font)
        self.lbl_jurusanMhs.setObjectName("lbl_jurusanMhs")
        self.verticalLayout_3.addWidget(self.lbl_jurusanMhs)
        self.lbl_noTelpMhs = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Iosevka Custom")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_noTelpMhs.setFont(font)
        self.lbl_noTelpMhs.setObjectName("lbl_noTelpMhs")
        self.verticalLayout_3.addWidget(self.lbl_noTelpMhs)
        self.formLayout.setLayout(0, QtWidgets.QFormLayout.LabelRole, self.verticalLayout_3)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.ledit_nimMhs = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.ledit_nimMhs.setObjectName("ledit_nimMhs")
        self.verticalLayout_2.addWidget(self.ledit_nimMhs)
        self.ledit_namaMhs = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.ledit_namaMhs.setObjectName("ledit_namaMhs")
        self.verticalLayout_2.addWidget(self.ledit_namaMhs)
        self.ledit_jurusanMhs = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.ledit_jurusanMhs.setObjectName("ledit_jurusanMhs")
        self.verticalLayout_2.addWidget(self.ledit_jurusanMhs)
        self.ledit_noTelpMhs = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.ledit_noTelpMhs.setObjectName("ledit_noTelpMhs")
        self.verticalLayout_2.addWidget(self.ledit_noTelpMhs)
        self.formLayout.setLayout(0, QtWidgets.QFormLayout.FieldRole, self.verticalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        
        self.btn_tambah = QtWidgets.QPushButton(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Iosevka")
        font.setBold(True)
        font.setWeight(75)
        self.btn_tambah.setFont(font)
        self.btn_tambah.setObjectName("btn_tambah")
        self.horizontalLayout.addWidget(self.btn_tambah)
        self.btn_tambah.clicked.connect(self.clickButtonTambah)
        
        self.btn_edit = QtWidgets.QPushButton(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Iosevka")
        font.setBold(True)
        font.setWeight(75)
        self.btn_edit.setFont(font)
        self.btn_edit.setObjectName("btn_edit")
        self.horizontalLayout.addWidget(self.btn_edit)
        self.btn_edit.clicked.connect(self.clickButtonEdit)
        
        self.btn_clear = QtWidgets.QPushButton(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Iosevka")
        font.setBold(True)
        font.setWeight(75)
        self.btn_clear.setFont(font)
        self.btn_clear.setObjectName("btn_clear")
        self.horizontalLayout.addWidget(self.btn_clear)
        self.btn_clear.clicked.connect(self.clickButtonClear)
        
        self.btn_clear_2 = QtWidgets.QPushButton(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Iosevka")
        font.setBold(True)
        font.setWeight(75)
        self.btn_clear_2.setFont(font)
        self.btn_clear_2.setObjectName("btn_clear_2")
        self.horizontalLayout.addWidget(self.btn_clear_2)
        self.btn_clear_2.clicked.connect(self.clickButtonHapus)
        
        self.formLayout.setLayout(1, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(10, 20, 471, 401))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.lbl_dataMhs = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Iosevka Custom")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_dataMhs.setFont(font)
        self.lbl_dataMhs.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_dataMhs.setObjectName("lbl_dataMhs")
        self.verticalLayout_4.addWidget(self.lbl_dataMhs)
        
        self.listWidget = QtWidgets.QListWidget(self.verticalLayoutWidget_3)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout_4.addWidget(self.listWidget)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(-10, 580, 501, 71))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/newPrefix/Design/waves.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label.raise_()
        self.formLayoutWidget.raise_()
        self.verticalLayoutWidget_3.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def clickButtonTambah(self):
        self.listWidget.addItem(
           'NIM\t: ' + self.ledit_nimMhs.text()  + '\n' + 
           'Nama\t: ' + self.ledit_namaMhs.text() + '\n' +
           'Jurusan\t: ' + self.ledit_jurusanMhs.text()  + '\n' +
           'No.Telp\t: ' + self.ledit_noTelpMhs.text() + '\n')

    def clickButtonEdit(self):
    	if self.listWidget.currentRow() < 0: return
    	self.entryForm = EntryForm()
    	s = str(self.listWidget.currentItem().text())
    	idxNim = s.index('NIM\t:')
    	idxNama = s.index('Nama\t:')
    	idxJurusan = s.index('Jurusan\t:')
    	idxNoTelp = s.index('No.Telp\t:')
    	self.entryForm.ledit_nimMhs.setText(s[(idxNim):6])
    	self.entryForm.ledit_namaMhs.setText(s[(idxNama):22])
    	self.entryForm.ledit_jurusanMhs.setText(s[(idxJurusan):38])
    	self.entryForm.ledit_TelpMhs.setText(s[(idxNoTelp):52])
    	
    	if self.entryForm.exec_() == QDialog.Accepted:
    	   self.listWidget.currentItem().setText(
    	   self.entryForm.ledit_nimMhs.text() + '\n' +
    	   self.entryForm.ledit_namaMhs.text() + '\n' +
    	   self.entryForm.ledit_jurusanMhs.text() + '\n' +
    	   self.entryForm.ledit_TelpMhs.text() + '\n')
    	   
    def clickButtonClear(self):
    	self.listWidget.clear()
    	
    def clickButtonHapus(self):
    	row = self.listWidget.currentRow()
    	if row >= 0:
    		self.listWidget.takeItem(row)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.lbl_nimMhs.setText(_translate("Form", "NIM"))
        self.lbl_namaMhs.setText(_translate("Form", "Nama"))
        self.lbl_jurusanMhs.setText(_translate("Form", "Jurusan"))
        self.lbl_noTelpMhs.setText(_translate("Form", "No. Telp"))
        self.btn_tambah.setText(_translate("Form", "TAMBAH"))
        self.btn_edit.setText(_translate("Form", "EDIT"))
        self.btn_clear.setText(_translate("Form", "CLEAR"))
        self.btn_clear_2.setText(_translate("Form", "HAPUS"))
        self.lbl_dataMhs.setText(_translate("Form", "DATA MAHASISWA"))
import test_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
