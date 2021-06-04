from PyQt5.QtWidgets import (QDialog, QGridLayout, 
     QHBoxLayout, QLabel, QLineEdit, QPushButton)
     
class EntryForm(QDialog):
   def __init__(self):
      super().__init__()
      self.setupUi()
      
   def setupUi(self):
      self.resize(300, 100)
      self.move(320, 280)
      self.setWindowTitle('Tambah/Ubah Kontak')
        
      self.okButton = QPushButton('OK')
      self.cancelButton = QPushButton('Batal')
      
      hbox = QHBoxLayout()
      hbox.addWidget(self.okButton)
      hbox.addWidget(self.cancelButton)
      
      self.label1 = QLabel("Nim :")
      self.ledit_nimMhs = QLineEdit()
      self.label2 = QLabel("Nama :")
      self.ledit_namaMhs = QLineEdit()
      self.label3 = QLabel("Jurusan :")
      self.ledit_jurusanMhs = QLineEdit()
      self.label4 = QLabel("No.Telp :")
      self.ledit_TelpMhs = QLineEdit()
      
      layout = QGridLayout()
      layout.addWidget(self.label1, 0, 0)
      layout.addWidget(self.ledit_nimMhs, 0, 1)
      layout.addWidget(self.label2, 1, 0)
      layout.addWidget(self.ledit_namaMhs, 1, 1)
      layout.addWidget(self.label3, 2, 0)
      layout.addWidget(self.ledit_jurusanMhs, 2, 1)
      layout.addWidget(self.label4, 4, 0)
      layout.addWidget(self.ledit_TelpMhs, 4, 1)
      layout.addLayout(hbox, 5, 1)      
      self.setLayout(layout)
        
      self.okButton.clicked.connect(self.accept)
      self.cancelButton.clicked.connect(self.reject)
