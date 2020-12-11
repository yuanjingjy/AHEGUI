#!/usr/bin/env python
# encoding: utf-8
'''
@Author: yuanjing
@file: maingui.py
@time: 2020/12/3 8:41
'''

from PyQt5.QtCore import *
from PyQt5.QtGui import  *
from PyQt5.QtWidgets import *
import sys
import numpy as np
from ahegui import Ui_Form

import matplotlib
matplotlib.use("Qt5Agg")
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

#便于汉字显示
plt.rcParams['font.sans-serif'] = ['SimHei']#步骤一（替换sans-serif字体）
plt.rcParams['axes.unicode_minus'] = False#步骤二（解决坐标轴负数的负号显示问题）

#读取txt数据
#创建一个matplotlib图形绘制类
class MyFigure(FigureCanvas):
    def __init__(self,width =5,height=4,dpi=100):
        #第一步，创建一个Figure
        self.fig = Figure(figsizee=(width,height),dpi=dpi)
        #第二步：在父类中激活Figure窗口
        super(MyFigure,self).__init__(self.fig)
        #第三步，创建一个子图，用于绘制图形用，111表示图形编号，类似matlab中的subplot
        self.axes1 = self.fig.add_subplot(2,2,1)
        self.axes2 = self.fig.add_subplot(2,2,2)
        self.axes3 = self.fig.add_subplot(2,2,3)
        self.axes4 = self.fig.add_subplot(2,2,4)

    #第四步，画图
    def plotsin(self):
        self.axes0 = self.fig.add_subplot(111)
        t = np.arange(0.0, 3.0,0.01)
        s = np.sin(2*np.pi*t)
        self.axes0.plot(t,s)

    def plotcos(self):
        t1 = np.arange(0.0,3.0,0.01)
        s1 = np.cos(2*np.pi*t1)
        self.axes0.plot(t1,s1)

class MainDialogImgBW(QDialog,Ui_Form):
    def __init__(self):
        super(MainDialogImgBW,self).__init__()
        self.setupUi(self)
        self.setWindowTitle("显示matplotlib绘制图形")
        self.setMinimumSize(0,0)

        #第五步，定义MyFigure类的一个实例
        self.F = MyFigure(width=30,height=2,dpi=100)
        self.plotcos()
        #第六步，在GUI的groupbox中创建一个布局，用于添加MyFigure类的实例和其他部件
        self.gridlayout = QGridLayout(self.groupBox)
        self.gridlayout.addWidget(self.F,0,1)

    #补充，另创建一个实例绘图并显示

        def plotcos(self):
            s = np.loadtxt(r'D:\01袁晶\Githubcode\AHEGUI\meanbp.txt')
            self.F.axes1.plot(s)
            self.F.axes1.set_title('avr')



    if __name__ == "__main__":
        app = QApplication(sys.argv)
        main = MainDialogImgBW()
        main.show()
        sys.exit(app.exec_())