import charming as app


@app.setup
def setup():
    app.size(10, 10)
    # app.size(app.get_window_width() - 1, app.get_window_height() - 1)
    # app.frame_rate(1)
    app.no_cursor()


@app.draw
def draw():
    pass
    # print(app.get_frame_count(), app.get_frame_rate())


app.run()