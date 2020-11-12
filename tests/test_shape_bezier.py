import charming as app

app.full_screen()
app.fill('@', app.RED, app.YELLOW)
# app.no_fill()
app.stroke('e', app.BLUE, app.GREEN)
with app.open_shape():
    app.vertex(30, 10)
    app.bezier_vertex(80, 0, 80, 35, 30, 35)
    app.bezier_vertex(50, 30, 60, 25, 30, 10)
# app.bezier(40, 5, 10, 10, 50, 20, 10, 30)

# t = 0
# cnt = 4
# app.stroke('a', app.RED, app.YELLOW)
# app.stroke_weight(1)
# while t <= 1:
#     x = app.bezier_point(40, 10, 50, 10, t)
#     y = app.bezier_point(5, 10, 20, 30, t)
#     app.point(x, y)
#     t += 1 / cnt

app.run()
