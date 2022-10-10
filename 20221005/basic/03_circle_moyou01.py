import turtle

# ポインターの形設定
turtle.shape('classic')

#色の設定
turtle.color('green')


# 円をずらして複数書く　ベタ書き
# turtle.right(135)
# turtle.circle(100)

# turtle.right(135)
# turtle.circle(100)

# turtle.right(135)
# turtle.circle(100)

# turtle.right(135)
# turtle.circle(100)

# turtle.right(135)
# turtle.circle(100)

# turtle.right(135)
# turtle.circle(100)


# 円をずらして複数書く　繰り返し
for i in range(8):
    turtle.right(135)
    turtle.circle(100)

turtle.done()
