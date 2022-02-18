import turtle
def koch(size,n):       #size是长度，n是阶数
    if n== 0:
        turtle.fd(size)
    else:
        for angle in [0,60,-120,60]:
            turtle.left(angle)
            koch(size/3,n-1)
def main():     #主的控制过程
    turtle.setup(800,400)
    turtle.penup()
    turtle.goto(-300,-50)
    turtle.pendown()
    turtle.pensize(2)
    
    # koch(600,3)     #3阶科赫曲线，
    # turtle.hideturtle()       #以上是绘制曲线
# 以下是绘制雪花
    level =3
    koch(400,level)
    turtle.right(120)
    koch(400,level)
    turtle.right(120)
    koch(400,level)
    turtle.hideturtle()
main()
