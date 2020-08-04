from PyQt5.QtWidgets import (QWidget, QHBoxLayout, 
    QLabel, QApplication)
from PyQt5.QtGui import QPixmap
import sys
import sys
from PyQt5.QtWidgets import (QWidget, QGridLayout, 
    QPushButton, QApplication)
import time
from PyQt5.QtCore import *
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
import threading
from threading import Timer
import sched,time
from PyQt5 import QtCore, QtGui, QtWidgets
from pynput.keyboard import Key,Listener
from PyQt5.QtGui import QMouseEvent, QCursor

t = 0

class Example(QWidget):

    def __init__(self,parent=None):
        super(Example,self).__init__(parent)


        self.thread = WorKer()
        
        self.i = 0
        self.j = 0
        self.pixmap = QPixmap("chouka.png")
        self.pixmap1 = QPixmap("dixing.png")
        self.pixmap2 = QPixmap("faka.png")
        self.pixmap3 = QPixmap("fenzhuo.png")
        self.pixmap4 = QPixmap("guangsu.png")
        self.pixmap5 = QPixmap("zhongjian.png")
        self.pixmap6 = QPixmap("jiaocuo.png")
        self.pixmap7 = QPixmap("shaoka.png")
        self.pixmap8 = QPixmap("shaxing.png")
        self.pixmap9 = QPixmap("tiangongtu.png")
        self.pixmap10 = QPixmap("tianxingchongri.png")
        self.pixmap11 = QPixmap("xiantian.png")
        self.pixmap12 = QPixmap("xingmeng.png")
        self.pixmap13 = QPixmap("xiunei.png")
        self.pixmap14 = QPixmap("yangxing.png")
        self.pixmap15 = QPixmap("yangxingxiangwei.png")
        self.pixmap16 = QPixmap("zhanbu.png")
        self.pixmap17 = QPixmap("zhaozi.png")
        self.pixmap18 = QPixmap("kongbai.png")

        self.timer1 = QTimer()


        self.initUI()



    def initUI(self):

        self.grid = QGridLayout()
        self.setLayout(self.grid)

        self.lb = QLabel(self)
        self.lb.setPixmap(self.pixmap)

        self.lb1 = QLabel(self)
        self.lb1.setPixmap(self.pixmap1)

        self.lb2 = QLabel(self)
        self.lb2.setPixmap(self.pixmap2)

        self.lb3 = QLabel(self)
        self.lb3.setPixmap(self.pixmap3)

        self.lb4 = QLabel(self)
        self.lb4.setPixmap(self.pixmap4)

        self.lb5 = QLabel(self)
        self.lb5.setPixmap(self.pixmap5)

        self.lb6 = QLabel(self)
        self.lb6.setPixmap(self.pixmap6)

        self.lb7 = QLabel(self)
        self.lb7.setPixmap(self.pixmap7)



        self.grid.addWidget(self.lb,1,0)
        self.grid.addWidget(self.lb1, 2, 0)
        self.grid.addWidget(self.lb2, 1, 1)
        self.grid.addWidget(self.lb3, 1, 2)
        self.grid.addWidget(self.lb4, 1, 3)
        self.grid.addWidget(self.lb5, 1, 4)
        self.grid.addWidget(self.lb7, 1, 5)
        self.grid.addWidget(self.lb6, 2, 4)



        




        

        # self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.setWindowOpacity(0.5)  
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        
        self.move(500, 500)
        self.setWindowTitle('Red Rock')
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        
        self.show()


    def mousePressEvent(self, event):
        if event.button()==Qt.LeftButton:
            self.m_flag=True
            self.m_Position=event.globalPos()-self.pos() #获取鼠标相对窗口的位置
            event.accept()
            self.setCursor(QCursor(Qt.OpenHandCursor))  #更改鼠标图标
            
    def mouseMoveEvent(self, QMouseEvent):
        if Qt.LeftButton and self.m_flag:  
            self.move(QMouseEvent.globalPos()-self.m_Position)#更改窗口位置
            QMouseEvent.accept()
            
    def mouseReleaseEvent(self, QMouseEvent):
        self.m_flag=False
        self.setCursor(QCursor(Qt.ArrowCursor))
    

    def keyPressEvent(self, e):


        if e.key() ==  Qt.Key_0:
            print("触发")
            self.thread.setVal(6)
            self.timer=QTimer()
            self.timer.timeout.connect(self.setTime)
            self.timer.start(100)

            # self.threading.Thread(target=self.xunhuan)
            
            
    def setTime(self):
        global t
        print("循环接受")
        if (t == 1):
            self.timer.stop()
            self.changePng()
            # self.thread.sinOut.connect(self.slotAdd)
            # lbl = QLabel(self)
            # lbl.setPixmap(self.pixmap18)
            # self.grid.addWidget(lbl, 1, 0)
            # self.thread.setVal(6)
            

    def xunhuan(self):
        global t
        
        while True:
            if (t == 1):
                
                self.thread.sinOut.connect(self.slotAdd)
                


    def slotAdd(self,num):
        pass

        

    def timer2(self):
        print("开始删除")
        lbl = QLabel(self)
        lbl.setPixmap(self.pixmap18)
        lb2 = QLabel(self)
        lb2.setPixmap(self.pixmap18)
        self.grid.addWidget(lbl,1,self.i)
        self.grid.addWidget(lb2,2,self.j)
        self.i += 1
        self.j += 1
        if (self.i == 6):

            self.grid.addWidget(self.lb,1,0)
            self.grid.addWidget(self.lb1, 2, 0)
            self.grid.addWidget(self.lb2, 1, 1)
            self.grid.addWidget(self.lb3, 1, 2)
            self.grid.addWidget(self.lb4, 1, 3)
            self.grid.addWidget(self.lb5, 1, 4)
            self.grid.addWidget(self.lb7, 1, 5)
            self.grid.addWidget(self.lb6, 2, 4)


            
            # self.timer1.stop()
            




    def changePng(self):
        
        self.timer1.timeout.connect(self.timer2)
        self.timer1.start(2500)
        
        



class WorKer(QThread):

    sinOut = pyqtSignal(int)

    def __init__(self,parent=None):


        super(WorKer,self).__init__(parent)
 
        self.identity = None
        self.jianpan = jianting()
 
    def setIdentity(self,text):
        self.identity = text
 
    def setVal(self,val):
        self.times = int(val)
        print("0")
 
        ##执行线程的run方法
        self.start()
 
    def run(self):
        self.jianpan.run()
        global t
        while True:
            if (t == 1):
                
                self.sinOut.emit(1)
                print("已发送信号")
                t = 2



        
class jianting():
    def on_press(self,key):
        try:
            if key.char == "q":
            
                global t
                print('you press Enter')
                t = 1
                print(t)
        except:
            pass
            
    
        # else:
        #     return False #按键不是enter,停止监视
    def on_release(self,key):
        try:
            if key == "q":
            
                print('you release Enter')
                return False
            
        except:
            pass

        

    def run (self):
        #监听键盘按键
        with Listener(on_press=self.on_press,on_release=self.on_release) as listener:
            listener.join()

        #停止监视



if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())