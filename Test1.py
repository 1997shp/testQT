from PyQt5.QtWidgets import (QWidget, QHBoxLayout, 
    QLabel, QApplication)
from PyQt5.QtGui import QPixmap
import sys
import sys
from PyQt5.QtWidgets import (QWidget, QGridLayout, 
    QPushButton, QApplication)
import time
from PyQt5.QtCore import QTimer, QThread
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication
import threading
from threading import Timer
import sched,time
from PyQt5 import QtCore, QtGui, QtWidgets
from pynput.keyboard import Key,Listener


t = 0

class timeout(QThread):
    def __init__(self):
        super().__init__()


    def run(self):
        self.sleep(2)

             
            



class Example(QWidget):

    def __init__(self):
        super().__init__()


        
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



        

        

        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        # QApplication.processEvents()
        self.move(500, 500)
        self.setWindowTitle('Red Rock')
        self.show()



        # time.sleep(3)
        # grid.itemAt().widget().deleteLater()


    def keyPressEvent(self, e):


        if e.key() ==  Qt.Key_0:
            # self.tH = threading.Thread(target=self.startWhile)
            print("0")
            # QApplication.processEvents()
            self.a = jianting()
            self.a.run()
            # self.tH = threading.Thread(target=self.a.run)
            # self.tH.start
            # self.tH.setDaemon(True)

            # self.tH.start()

            i = 0
            j = 0
            b = False
            b = self.startWhile()

            while (b):

                print((1 , i))
                print((2 , j))
                time.sleep(2)
                # self.changePng(i,j)
                QApplication.processEvents()
                lbl = QLabel(self)
                lbl.setPixmap(self.pixmap18)
                lb2 = QLabel(self)
                lb2.setPixmap(self.pixmap18)
                self.grid.addWidget(lbl, 1, i)
                self.grid.addWidget(lb2, 2, j)


                self.j = self.j + 1
                i = i + 1
                j = j + 1
                
                if (i == 7):

                    b = False





        # while self.i < 1:
        #     if e.key() == Qt.Key_Q:
        #         self.i = 10

        #         # t = threading.Timer(1,self.changePng())
        #         # t.start()
        #         # c = timeout()
        #         i = 0
        #         j = 0
        #         while (self.j < 6):
        #             print('1')
        #             time.sleep(2)
        #             self.changePng(i,j)
        #             QApplication.processEvents()
                    
        #             self.j = self.j + 1
        #             i = i + 1
        #             j = j + 1

                # while (self.j < 6):
                #     print("1")
                #     i = 0
                #     j = 0
                #     c.run()
                #     # s = sched.scheduler(time.time, time.sleep)
                #     # s.enter(2,0, self.changePng,(i,j))
                #     # s.run()
                    
                #     # t = threading.Timer(2, self.changePng, (i,j))
                #     # t.start()
                    
                #     self.timer = QTimer(self)  # 初始化一个定时器
                #     self.timer.timeout.connect(self.changePng ) # 计时结束调用operate()方法
                #     self.timer.start(2)  # 设置计时间隔并启动
                #     self.j = self.j + 1
                #     i = i + 1
                #     j = j + 1


    def startWhile(self):
        global t 

        if (self.i < 1) :
            print ("3")
            
            self.i = 10
            return True

        # while (t < 1):
        #     if (t == 1):
        #         return True



    def changePng(self,i,j):
        # i = 0
        # while (i < 3) :
        #     widgetToRemove = self.grid.itemAt(0).widget().deleteLater()
        #
        #
        #     i = i + 1
        # item = self.grid.takeAt(0)
        # widget = item.widget()
        # print(item)
        # # if widget has some id attributes you need to
        # # save in a list to maintain order, you can do that here
        # # i.e.:   aList.append(widget.someId)
        # widget.deleteLater()
        
        
        lbl = QLabel(self)
        lbl.setPixmap(self.pixmap18)
        lb2 = QLabel(self)
        lb2.setPixmap(self.pixmap18)
        self.grid.addWidget(lbl, 1, i)
        self.grid.addWidget(lb2, 2, j)





        
class jianting():
    def on_press(self,key):
        
        if key.char == "q":
            global t
            print('you press Enter')
            t = 1
            print(t)
            
    
        # else:
        #     return False #按键不是enter,停止监视
    def on_release(self,key):
        if key.char == "q":
            print('you release Enter')
            return False

        

    def run (self):
        #监听键盘按键
        with Listener(on_press=self.on_press,on_release=self.on_release) as listener:
            listener.join()

        #停止监视



if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())