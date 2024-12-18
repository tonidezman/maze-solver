from tkinter import Canvas
from graphics import Window

class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"


class Line:
    def __init__(self, p1: Point, p2: Point):
        self.p1 = p1
        self.p2 = p2

    def draw(self, canvas: Canvas):
        canvas.create_line(self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill="black", width=2)

def main():
    win = Window(800, 600)

    p1 = Point(100, 100)
    p2 = Point(200, 200)
    line = Line(p1, p2)
    line.draw(win.get_canvas())

    win.wait_for_close()


main()