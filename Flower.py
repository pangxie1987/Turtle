# -*- coding:utf-8 -*-
# https://blog.csdn.net/zengxiantao1994/article/details/76588580

'''
太阳花
'''
import turtle as t
import time

# t.color('red','yellow')
# t.begin_fill()

# for i in range(50):
#     t.fd(200)
#     t.left(170)
# t.end_fill()
# t.done()


'''
五角星
'''
# t.pensize(5)
# t.color('yellow','red')
# t.hideturtle()  #隐藏画笔箭头

# t.begin_fill()
# for i in range(5):
#     t.fd(200)
#     t.right(144)
# t.end_fill()
# time.sleep(2)

# t.penup()
# t.goto(-150,-120)
# t.color('violet')
# t.write('Done',font=('Arial',40,'normal'))
# t.done()


'''
时钟程序
'''
# from datetime import *

# def Skip(step):
#     '''
#     抬起画笔，向前运动一段距离放下
#     '''
#     t.penup()
#     t.fd(step)
#     t.pd()

# def mkHand(name,length):
#     '''
#     注册Turtle形状，建立表针Turtle
#     '''
#     t.reset()
#     Skip(-length*0.1)
#     t.begin_poly()
#     t.fd(length*1.1)
#     t.end_poly()
#     handForm=t.get_poly()
#     t.register_shape(name,handForm)

# def Init():
#     global secHand,minHand,hurHand,printer
#     # 重置Turtle指向北
#     t.mode('logo')
#     # 建立三个表针Turtle并初始化
#     mkHand('secHand',135)
#     mkHand('minHand',125)
#     mkHand('hurHand',90)
#     secHand=t.Turtle()
#     secHand.shape('secHand')
#     minHand=t.Turtle()
#     minHand.shape('minHand')
#     hurHand=t.Turtle()
#     hurHand.shape('hurHand')

#     for hand in secHand,minHand,hurHand:
#         hand.shapesize(1,1,3)
#         hand.speed(0)

#     # 建立输出文字Turtle
#     printer = t.Turtle()
#     # 隐藏画笔的turtle形状
#     printer.hideturtle()
#     printer.pu()

# def SetupClock(radius):
#     '''
#     建立表的外框
#     '''
#     t.reset()
#     t.pensize(7)
#     for i in range(60):
#         Skip(radius)

#         if i % 5 == 0:
#             t.fd(20)
#             Skip(-radius - 20)
#             Skip(radius + 20)

#             if i ==0:
#                 t.write(int(12),align='center',font=('Courier',14,'bold'))
#             elif i == 30:
#                 Skip(25)
#                 t.write(int(i/5),align='center',font=('Courier',14,'bold'))
#                 Skip(-25)
#             elif(i ==25 or i==35):
#                 Skip(20)
#                 t.write(int(i/5),align='center',font=('Courier',14,'bold'))
#                 Skip(-20)
#             else:
#                 t.write(int(i/5),align='center',font=('Courier',14,'bold'))
#             Skip(-radius - 20)

#         else:
#             t.dot(5)
#             Skip(-radius)
#         t.right(6)

# def Week(t):
#     week=['星期一','星期二','星期三',
#     '星期四','星期五','星期六','星期日']
#     return week[t.weekday()]

# def Date(t):
#     y = t.year
#     m = t.month
#     d = t.day
#     return '%s %d%d'%(y,m,d)

# def Tick():
#     '''
#     绘制表针的动态显示
#     '''
#     tt = datetime.today()
#     second = tt.second+tt.microsecond*0.000001
#     minute = tt.minute+second / 60.0
#     hour = tt.hour + minute /60.0
#     secHand.setheading(6*second)
#     minHand.setheading(6*minute)
#     hurHand.setheading(30*hour)

#     t.tracer(False)
#     printer.fd(65)
#     printer.write(Week(tt),align='center',font=('Courier',14,'bold'))

#     printer.back(130)
#     printer.write(Date(tt),align='center',font=('Courier',14,'bold'))
#     printer.home()
#     t.tracer(True)

#     # 100s后继续调用tick
#     t.ontimer(Tick,100)

# def main():
#     t.tracer(False)
#     Init()
#     SetupClock(160)
#     t.tracer(True)
#     Tick()
#     t.mainloop()

# if __name__=='__main__':
#     main()

'''
心形图案
'''
# def curvemove():
#     for i in range(200):
#         t.right(1)
#         t.fd(1)
# t.speed(30)
# t.hideturtle()
# t.pensize(5)
# t.color('red','pink')
# t.begin_fill()
# t.left(140)
# t.fd(111.65)
# curvemove()
# t.left(120)
# curvemove()
# t.fd(111.65)
# t.end_fill()
# t.done()


# http://baijiahao.baidu.com/s?id=1577063675516282624&wfr=spider&for=pc
'''
鱼
'''
# t.color('black','yellow')
# t.ht()
# t.pensize(5)
# # 身体
# t.begin_fill()
# t.goto(200,200)
# t.goto(200,-200)
# # 鱼尾
# t.home()
# t.pu()
# t.goto(200,0)
# t.pd()
# t.goto(250,50)
# t.goto(250,-50)
# t.goto(200,0)
# # 眼睛
# t.pu()
# t.goto(50,-10)
# t.pd()
# t.circle(10)
# t.end_fill()
# t.done()

'''
机器猫
'''
t.setup(600,700)
t.pensize(5)
t.speed(10)
# blue&white face
t.color('black','blue')
t.begin_fill()
t.circle(200)
t.end_fill()
t.begin_fill()
t.color('black','white')
t.circle(160)
t.end_fill()
# nose
t.color('black','red')
t.pu()
t.begin_fill()
t.goto(0,200)
t.pd()
t.circle(20)
t.end_fill()
# eye1
t.color('black','white')
t.pu()
t.goto(-45,250)
t.pd()
t.begin_fill()
t.circle(45)
t.end_fill()
t.pu()
t.goto(-20,250)
t.pd()
t.begin_fill()
t.color('black')
t.circle(15)
t.goto(45,250)
t.pu()
t.goto(20,250)
t.pd()
t.end_fill()
# eye2
t.color('black','white')
t.pu()
t.goto(45,250)
t.pd()
t.begin_fill()
t.circle(45)
t.end_fill()
t.pu()
t.goto(20,250)
t.pd()
t.begin_fill()
t.color('black')
t.circle(15)
t.goto(-45,250)
t.goto(-20,250)
t.end_fill()

# smile
t.goto(0,50)
t.circle(150,-75)
print(t.pos())
t.circle(150,75)
t.left(15)
t.fd(150)
t.done()

