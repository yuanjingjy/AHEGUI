#!/usr/bin/env python
# encoding: utf-8
'''
@Author: yuanjing
@file: test.py
@time: 2020/12/11 10:54
'''
import matplotlib
matplotlib.use("Qt5Agg")  # 声明使用QT5
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import numpy as np
from ahegui import Ui_Form
from PyQt5.QtWidgets import *
import sys


class MyFigure(FigureCanvas):
    def __init__(self,width =50,height=40,dpi=100):
        #第一步，创建一个Figure
        self.fig = Figure(figsize=(width,height),dpi=dpi)
        #第二步：在父类中激活Figure窗口
        super(MyFigure,self).__init__(self.fig)



class MainDialogImgBW(QDialog,Ui_Form):
    def __init__(self):
        super(MainDialogImgBW,self).__init__()
        self.setupUi(self)

        #第五步：定义MyFigure类的一个实例
        self.F = MyFigure(width=50, height=40, dpi=100)
        self.gridlayout = QGridLayout(self.graphicsView_2)
        # self.gridlayout.addWidget(self.graphicsView_2,1,0)
        # self.scene = QGraphicsScene() #创建一个场景
        # self.scene.addWidget(self.F)#将图形元素添加到场景中
        # self.graphicsView_2.setScene(self.scene)#将创建添加到图形视图显示窗口
        # self.graphicsView_2.show()

        self.plotother()


    def plotother(self):
        F1 = MyFigure(width=50, height=40, dpi=100)
        # F1.fig.suptitle("Figuer_4")
        F1.axes1 = F1.fig.add_subplot(111)
        x = np.arange(0, 50)
        y = np.random.rand(50)
        F1.axes1.hist(y, bins=50)
        F1.axes1.plot(x, y)
        F1.axes1.bar(x, y)
        self.gridlayout.addWidget(F1, 0, 2)

    def plotcos(self):
        F1 = MyFigure(width=50, height=40, dpi=100)
        F1.fig.suptitle("Figuer_4")
        F1.axes1 = F1.fig.add_subplot(111)
        x = np.arange(0, 50)
        y = np.random.rand(50)
        F1.axes1.hist(y, bins=50)
        F1.axes1.plot(x, y)
        F1.axes1.bar(x, y)
        self.gridlayout.addWidget(F1, 0, 2)


    def plotscat(self):
        F1 = MyFigure(width=50, height=40, dpi=100)
        F1.axes1= F1.fig.add_subplot(111)

        x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        y = [23, 21, 32, 13, 3, 132, 13, 3, 1]
        F1.axes1.plot(x, y)
        F1.axes1.set_title("line")
        # # 散点图
        # F1.axes3 = F1.fig.add_subplot(223)
        # F1.axes3.scatter(np.random.rand(20), np.random.rand(20))
        # F1.axes3.set_title("scatter")
        # # 折线图
        # F1.axes4 = F1.fig.add_subplot(224)
        # x = np.arange(0, 5, 0.1)
        # F1.axes4.plot(x, np.sin(x), x, np.cos(x))
        # F1.axes4.set_title("sincos")
        self.gridlayout2.addWidget(F1, 0, 2)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = MainDialogImgBW()
    main.show()
    #app.installEventFilter(main)
    sys.exit(app.exec_())
