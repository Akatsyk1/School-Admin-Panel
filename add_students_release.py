import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from addstudents import *
import sqlite3


class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(MyWin, self).__init__(parent)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.add_info)

    def add_info(self):
        db = sqlite3.connect('data_school.db')
        cursor = db.cursor()
        name = self.ui.lineEdit.text()
        surname = self.ui.lineEdit_2.text()
        age = self.ui.lineEdit_3.text()
        _class = self.ui.lineEdit_4.text()
        cursor.execute("""INSERT INTO data_students VALUES (?, ?, ?, ?)""", (name, surname, age, _class))
        print(name, surname, age, _class)
        db.commit()
        db.close()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())
