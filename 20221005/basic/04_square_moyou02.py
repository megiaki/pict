import turtle

# ポインターの形設定
turtle.shape('classic')

#色の設定
turtle.color('green')

# 四角をずらして複数書く　繰り返し

for i in range(4*8):
   
    if i%4 == 0:
        turtle.left(45)

    turtle.forward(150)
    turtle.left(90)

# 描画後turtle非表示
turtle.hideturtle()
turtle.done()



