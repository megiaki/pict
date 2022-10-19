import turtle

# ポインターの形設定
turtle.shape('classic')

#色の設定
turtle.color('green')

# 四角をずらして複数書く　繰り返し
for i in range(70):
    
    turtle.forward(150)
    turtle.left(90)

    if i%4 == 1:
        turtle.left(90 + (i/4 * 90))




# turtle.setheading(275)
# turtle.circle(100)

# turtle.penup()
# turtle.setheading(0)
# turtle.forward(-5)

# turtle.setheading(275)
# turtle.pendown()
# turtle.circle(105)

# turtle.penup()
# turtle.setheading(0)
# turtle.forward(-15)

# turtle.setheading(275)
# turtle.pendown()
# turtle.circle(120)


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