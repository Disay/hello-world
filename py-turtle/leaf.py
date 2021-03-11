# -*- coding: utf-8 -*-

import turtle as t
#准备设置
t.screensize(400, 300) #设置画布大小
t.setup(840, 500) #设置主窗口的大小为840*500
t.pensize(5) #设置外花边的大小
t.color('mediumseagreen', 'forestgreen') #设置画笔颜色和填充颜色
t.speed(10) #设置画笔速度为10

def draw_clover(radius, rotate): #参数radius控制叶子的大小，rotate控制叶子的旋转
    t.begin_fill() #外形填充开始标志
    for i in range(4): #从0到3开始的for循环，共四片花瓣
        direction = i * 90
        t.seth(60 + direction + rotate)   #控制叶子根部的角度为60度
        t.fd(4 * radius)
        for j in range(2):
            t.seth(90 + direction + rotate)
            t.circle(radius, 180)
        t.seth(-60 + direction + rotate)
        t.fd(4 * radius)
        t.seth(60 + direction+rotate)   #控制叶子根部的角度为60度
        t.fd(2 * radius)

        for j in range(2): #从0到1开始的for循环，画内花边
            t.pencolor("whitesmoke") #设置内花边颜色
            t.pensize(8) #设置内花边的大小
            t.seth(90 + direction + rotate)
            t.circle(radius/2, 180)
            t.color('mediumseagreen', 'forestgreen')
            t.pensize(5)
        t.seth(-60 + direction + rotate)
        t.fd(2 * radius)
    t.end_fill() #依据轮廓填充颜色
    t.seth(-110)
    t.fd(6 * radius)

draw_clover(40, 25)
t.done() #保持窗口停留