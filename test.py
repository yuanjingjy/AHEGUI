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