# coding: utf-8
import turtle as t
t.screensize(500,300)
t.setup(840,500)
t.speed(10)

def hair():
    #开始作画，提笔
    t.penup()
    t.goto(-70,125 )
    t.pendown()
    t.fillcolor("saddlebrown")
    t.begin_fill()
    for j in range(12):
        t.seth(60 - (j * 30))  #每次调整画笔角度
        t.circle(-50, 90)   #画120度的弧度
    t.end_fill()

def ears(dir):
    t.penup()
    t.goto((0 - dir) * 25, 75)
    t.seth(90)
    t.pendown()
    t.fillcolor('peru')
    t.begin_fill()
    t.circle(dir * 28)
    t.end_fill()
    t.penup()
    t.goto((0 - dir) * 30, 68)
    t.seth(90)
    t.pendown()
    t.fillcolor('white')
    t.begin_fill()
    t.circle(dir * 18)
    t.end_fill()

def face():
    t.penup()
    t.goto(0, 80)
    t.pendown()
    t.fillcolor('peru')
    t.begin_fill()
    t.setheading(180)
    t.circle(80)
    t.end_fill()
    # 下巴
    t.circle(80, 125)
    t.fillcolor('white')
    t.begin_fill()
    t.circle(80, 110)
    t.setheading(145)
    t.circle(110, 72)
    t.end_fill()

# 画眼睛，dir用来设置方向，左右眼对称
def eye(dir):
    t.penup()
    t.goto((0 - dir) * 30, 20)
    t.setheading(0)
    t.pendown()
    t.fillcolor('black')
    t.begin_fill()
    t.circle(10)
    t.end_fill()

# 画嘴巴
def mouth():
    t.penup()
    t.goto(0, 0)
    t.setheading(-90)
    t.pendown()
    t.forward(50)
    t.setheading(0)
    t.circle(80, 25)
    t.penup()
    t.goto(0, -50)
    t.setheading(180)
    t.pendown()
    t.circle(-80, 25)

# 画鼻子
def nose():
    t.penup()
    t.goto(15, 0)
    t.setheading(90)
    t.pendown()
    t.fillcolor('saddlebrown')
    t.begin_fill()
    t.circle(15)
    t.end_fill()


hair()
ears(1)
ears(-1)
face()
eye(1)
eye(-1)
mouth()
nose()

t.done()  # 保持窗口停留
