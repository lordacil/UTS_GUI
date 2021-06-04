from PyQt5.QtWidgets import *

app = QApplication([])
button = QPushButton('Click')
def on_button_click():
	alert = QMessageBox()
	alert.setText('You clicked the button!')
	alert.exec_()

button.clicked.connect(on_button_click)
button.show()
app.exec_();