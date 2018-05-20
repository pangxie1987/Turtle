https://blog.csdn.net/zengxiantao1994/article/details/76588580
https://www.cnblogs.com/bravestarrhu/p/8287261.html

小猪佩奇
https://github.com/Monster12138/-/blob/master/%E5%B0%8F%E7%8C%AA%E4%BD%A9%E5%A5%87.py

turtple库命令解释
import turtle as t

t.circle()  #画圆，半径为正(负)，表示圆心在画笔的左边(右边)画圆
t.begin_fill()  #装备开始填充图形
t.end_fill()    #填充完成
t.color(color1,color2)  #同时设置color1和color2
t.goto(x,y) #将画笔移动到坐标为x,y的位置
t.pu()=t.up()=t.penup() #将画笔提起，此时移动不会进行绘制
t.pd()=t.pendown()=t.down() #画笔按下，此时移动进行绘制
t.pensize() #设置线条粗细
t.seth()=t.setheading() #设置画笔方向
t.hideturtle()=t.ht()   #隐藏画笔（箭头），画笔按下仍可汇出图形
t.showturtle()=t.st()   #显示画笔（箭头）
t.setup()   #设置窗口的大小和位置
t.dot() #按指定直径size画圆圈
t.ontimer(fun,t=0)  #fun 一个无参的函数 t 时间，开启一个计时器，t秒后调用fun函数
t.tracer()  #打开或者关闭动画，并设置绘制延迟
t.reset()   #重置画笔状态
printer=t.Turtle()  #创建和返回具有相同位置、方向和箭头的克隆
t.begin_poly()  #表示开始记录多边形第一个顶点
t.end_poly()    #表示结束记录多边形顶点
t.get_poly()    #表示获取最后记录的多边形
t.register_shape()  #内存中添加注册图形
t.home()    #将位置和方向恢复到初始位置


screen.mainloop() | screen.done() | t.mainloop() | t.done()
# 运行后屏幕自动消失,调用这句后屏幕会保持,直到主动关闭当前窗口,想使用的话必须作为图形绘制程序的最后一条语句