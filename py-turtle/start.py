# coding: utf-8
import turtle #引用绘图库 turtle

turtle.screensize(500, 300)#设置画布大小
#turtle.setup(width=0.5, height=0.75, startx=None, starty=None)
# width，height：输入宽和高为整数时, 表示像素; 为小数时, 表示占据电脑屏幕的比例、(startx，starty)：这一坐标表示矩形窗口左上角顶点的位置。如果为空，则窗口位于屏幕中心
turtle.setup(800, 400, 300, 300) # 设置主窗口的大小和位置,后两个参数可选
turtle.speed(2) #设置画笔速度为2

turtle.penup() #提起笔移动，不绘制图形
turtle.fd(-330)# 画笔向绘制方向的当前方向移动distance(integer or float)的pixels距离
turtle.pendown()#落下画笔
turtle.pensize(20) #设置画笔的宽度；
turtle.pencolor("green") #画笔颜色设成绿色
#更改笔的角度为angle
turtle.seth(-45) # 只改变行进方向（角度按逆时针），但不行进
for i in range(5):
    turtle.circle(40, 90) #画圆，半径为正(负)，表示圆心在画笔的左边(右边)画圆
    turtle.circle(-40, 90)
turtle.circle(40, 80/2)
turtle.fd(40)
turtle.circle(16, 180)
turtle.fd(40 * 2/3)
turtle.end_fill() #完成填充图片的绘制
turtle.done() #保持窗口停留