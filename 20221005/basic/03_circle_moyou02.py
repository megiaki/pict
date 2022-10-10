import turtle

# ポインターの形設定
turtle.shape('classic')

#色の設定
turtle.color('green')

num = 0
while True:
    turtle.forward(200)
    turtle.left(170)
    if abs(turtle.pos()) < 1:
        break

turtle.setheading(275)
turtle.circle(100)

turtle.penup()
turtle.setheading(0)
turtle.forward(-5)

turtle.setheading(275)
turtle.pendown()
turtle.circle(105)

turtle.penup()
turtle.setheading(0)
turtle.forward(-15)

turtle.setheading(275)
turtle.pendown()
turtle.circle(120)


# 描画後turtle非表示
turtle.hideturtle()

turtle.done()




#　参考
# from turtle import *
# color('red', 'yellow')
# begin_fill()
# while True:
#     forward(200)
#     left(170)
#     if abs(pos()) < 1:
#         break
# end_fill()
# done()