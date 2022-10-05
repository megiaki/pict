import turtle

# ポインターの形設定
turtle.shape('classic')

#色の設定
turtle.color('green')

# 左
turtle.backward(100)

#角度設定
turtle.left(90)
turtle.backward(100)

turtle.right(90)
turtle.backward(100)

# ホームに戻る
turtle.home()

# 円を描く
turtle.circle(150)

#　右へ
turtle.forward(200)

turtle.done()