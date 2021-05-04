# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Kisi-Kisi_UTS.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

# Import package dari PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets

# Class Ui_MainWindow
class Ui_MainWindow(object):
    # Fungsi setupUi
    def setupUi(self, MainWindow):
        
        # Deklarasi window utama
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(501, 449)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        # menempatkan widget di bagian tengah window
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(180, 40, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(40, 70, 421, 191))
        self.textEdit.setObjectName("textEdit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(42, 282, 22, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(42, 310, 32, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(42, 338, 45, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(42, 366, 44, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        # Widget LineEdit untuk NIM
        self.inputNIM = QtWidgets.QLineEdit(self.centralwidget)
        self.inputNIM.setGeometry(QtCore.QRect(120, 280, 341, 20))
        self.inputNIM.setObjectName("inputNIM")
        # Widget LineEdit untuk Nama
        self.inputNama = QtWidgets.QLineEdit(self.centralwidget)
        self.inputNama.setGeometry(QtCore.QRect(120, 310, 341, 20))
        self.inputNama.setObjectName("inputNama")
        # Widget LineEdit untuk Jurusan
        self.inputJurusan = QtWidgets.QLineEdit(self.centralwidget)
        self.inputJurusan.setGeometry(QtCore.QRect(120, 340, 341, 20))
        self.inputJurusan.setObjectName("inputJurusan")
        # Widget LineEdit untuk No. Telp
        self.inputNoTelp = QtWidgets.QLineEdit(self.centralwidget)
        self.inputNoTelp.setGeometry(QtCore.QRect(120, 370, 341, 20))
        self.inputNoTelp.setObjectName("inputNoTelp")
        self.btnTambah = QtWidgets.QPushButton(self.centralwidget)
        self.btnTambah.setGeometry(QtCore.QRect(140, 400, 75, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        # Widget PushButton untuk button Tambah
        self.btnTambah.setFont(font)
        self.btnTambah.setObjectName("btnTambah")
        self.btnEdit = QtWidgets.QPushButton(self.centralwidget)
        self.btnEdit.setGeometry(QtCore.QRect(220, 400, 75, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        # Widget PushButton untuk button Edit
        self.btnEdit.setFont(font)
        self.btnEdit.setObjectName("btnEdit")
        self.btnClear = QtWidgets.QPushButton(self.centralwidget)
        self.btnClear.setGeometry(QtCore.QRect(300, 400, 75, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        # Widget PushButton untuk button Clear
        self.btnClear.setFont(font)
        self.btnClear.setObjectName("btnClear")
        self.btnHapus = QtWidgets.QPushButton(self.centralwidget)
        self.btnHapus.setGeometry(QtCore.QRect(380, 400, 75, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        # Widget PushButton untuk button Hapus
        self.btnHapus.setFont(font)
        self.btnHapus.setObjectName("btnHapus")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    # Fungsi retranslateUi 
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        # Nama-nama title pada window utama
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Data Mahasiswa"))
        self.label_2.setText(_translate("MainWindow", "NIM"))
        self.label_3.setText(_translate("MainWindow", "Nama"))
        self.label_4.setText(_translate("MainWindow", "Jurusan"))
        self.label_5.setText(_translate("MainWindow", "No. Telp"))
        self.btnTambah.setText(_translate("MainWindow", "TAMBAH"))
        self.btnEdit.setText(_translate("MainWindow", "EDIT"))
        self.btnClear.setText(_translate("MainWindow", "CLEAR"))
        self.btnHapus.setText(_translate("MainWindow", "HAPUS"))

# Untuk menjalankan seluruh kode
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
