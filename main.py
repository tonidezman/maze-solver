from graphics import Window, Line, Point


def main():
    win = Window(800, 600)

    p1 = Point(100, 100)
    p2 = Point(200, 200)
    line = Line(p1, p2)
    win.draw_line(line, fillcolor="red", width=2)

    win.wait_for_close()


main()