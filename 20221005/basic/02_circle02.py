import turtle

# ポインターの形設定
turtle.shape('classic')

for i in range(20):
    i = i*10

    turtle.color('white')
    turtle.sety(-200 + i )

    # 円を描く
    turtle.color('green')
    turtle.circle(100)

# 描画後turtle非表示
turtle.hideturtle()

turtle.done()