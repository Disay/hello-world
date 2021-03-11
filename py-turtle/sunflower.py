# coding: utf-8
# -*- coding: utf-8 -*-
import turtle as t

#准备设置
t.screensize(400, 300) #设置画布大小
t.setup(840,500) #设置主窗口的大小为840*500
t.pensize(2) #设置画笔的大小
t.color('red','yellow') #设置画笔颜色和填充颜色(pink)
t.speed(2) #设置画笔速度为10

t.penup() #提笔
t.goto(-150,0) #画笔前往坐标(-150,0)
t.pendown() #下笔

t.begin_fill() #准备绘制
while True:
    t.forward(300) #画笔前进300个像素
    t.left(170) #画笔左转170度
    if t.distance(-150, 0) < 1: #如果当前坐标点距离出发点(150,0)小于1，则跳出循环
        break
t.end_fill() #依据轮廓填充颜色

#保持窗口停留
t.done()