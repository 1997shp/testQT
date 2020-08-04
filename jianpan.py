import sys
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


list = []

class picture(QWidget):
   def __init__(self):
      super(picture, self).__init__()
      self.initUI()

      self.i = 0
      self.j = 0


      self.k = 0
      self.l = 0
      #   self.label = QLabel(self)
      #   self.label.setText("   显示图片")
      #   self.label.setFixedSize(300, 200)
      #   self.label.move(160, 160)

      #   self.label.setStyleSheet("QLabel{background:white;}"
      #                            "QLabel{color:rgb(300,300,300,120);font-size:10px;font-weight:bold;font-family:宋体;}"
      #                            )

        

        


   def initUI(self):

      self.grid = QGridLayout()
      self.setLayout(self.grid) 

      btn = QPushButton(self)
      btn.setText("GCD")
      btn.clicked.connect(self.openimage)

      btn1 = QPushButton(self)
      btn1.setText("能力技")
      btn1.clicked.connect(self.openimage1)

      btn2 = QPushButton(self)
      btn2.setText("保存")
      btn2.clicked.connect(self.saveList)

      self.grid.addWidget(btn,3,9)
      self.grid.addWidget(btn1,4,9)
      self.grid.addWidget(btn2,5,9)

      self.move(500, 500)
      self.setWindowTitle('Red Rock')
      # self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        
      self.show()







   def openimage(self):
      imgName, imgType = QFileDialog.getOpenFileName(self, "打开图片", "", "*.png;;*.png;;All Files(*)")

      name = str(imgName)
      global list

      list.append(name)
      a = str(self.i)

      a = QLabel(self)
      a.setPixmap(QPixmap(imgName))
      self.grid.addWidget(a,1,self.j)
      self.i += 1
      self.j += 1

      
      # jpg = QtGui.QPixmap(imgName)
      # self.label.setPixmap(jpga)


   def openimage1(self):
      imgName, imgType = QFileDialog.getOpenFileName(self, "打开图片", "", "*.png;;*.png;;All Files(*)")
      a = str(self.k)
      a = QLabel(self)

      name = str(imgName)
      global list
      list.append(name)

      a.setPixmap(QPixmap(imgName))
      # pickle.dump(imgName,open(filePath.txt,'wb'))
      # print(pickle.load(filePath))
      self.grid.addWidget(a,2,self.l)
      self.k += 1
      self.l += 1


   def saveList(self):

      global list

      for i in list:


         print (i) 

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    my = picture()
    my.show()
    sys.exit(app.exec_())
