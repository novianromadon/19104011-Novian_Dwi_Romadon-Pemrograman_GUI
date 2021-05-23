import sys 
from PyQt5.QtGui import * 
from PyQt5.QtCore import * 
from PyQt5.QtWidgets import *

class MainForm(QWidget): 
   def __init__(self): 
      super().__init__() 
      self.setupUi()

   def setupUi(self): 
      self.resize(400, 200) 
      self.move(300, 300) 
      self.setWindowTitle('Demo QTextEdit')

      # Membuat label No. HP dan LineEditnya
      self.label1 = QLabel() 
      self.label1.setText('No. HP')
      self.phoneEdit = QLineEdit()
      # Label No. HP dan LineEdit digabung menggunakan Layout Vertikal
      vbox1 = QVBoxLayout()
      vbox1.addWidget(self.label1) 
      vbox1.addWidget(self.phoneEdit)

      # Membuat label Pesan dan TextEditnya
      self.label2 = QLabel() 
      self.label2.setText('Pesan') 
      self.messageEdit = QTextEdit()
      # Label Pesan dan TexEdit digabung menggunakan Layout Vertikal
      vbox2 = QVBoxLayout() 
      vbox2.addWidget(self.label2) 
      vbox2.addWidget(self.messageEdit)

      # Layout No. HP dan Pesan digabung menggunakan Layout Vertikal
      vbox3 = QVBoxLayout() 
      vbox3.addLayout(vbox1) 
      vbox3.addLayout(vbox2)

      # Membuat Push Button Kirim SMS dan Batal
      self.sendButton = QPushButton('&Kirim SMS') 
      self.cancelButton = QPushButton('&Batal') 
      # Digabung menggunakan Layout Horizontal
      hbox = QHBoxLayout()
      hbox.addStretch() 
      hbox.addWidget(self.sendButton) 
      hbox.addWidget(self.cancelButton)
      layout = QVBoxLayout() 
      layout.addLayout(vbox3)

      # Membuat garis horizontal
      horizontalLine = QFrame(); 
      horizontalLine.setFrameShape(QFrame.HLine) 
      horizontalLine.setFrameShadow(QFrame.Sunken) 
      layout.addWidget(horizontalLine) 
      layout.addLayout(hbox) 
      self.setLayout(layout)

# Run Program
if __name__ == '__main__': 
   a = QApplication(sys.argv) 
   form = MainForm()
   form.show()
   a.exec_()