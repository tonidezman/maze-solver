from tkinter import Tk, BOTH, Canvas

class Window():
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.root = Tk()
        self.title = self.root.title("Window")
        self.canvas = Canvas(self.root, width=self.width, height=self.height)
        self.pack = self.canvas.pack(fill=BOTH, expand=1)
        self.windows_is_running = False
        self.root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.root.update_idletasks()
        self.root.update()
        self.windows_is_running = True
        while self.windows_is_running:
            self.redraw()

    def wait_for_close(self):
        self.windows_is_running = True
        while self.windows_is_running:
            self.redraw()

    def close(self):
        self.windows_is_running = False

def main():
    window = Window(800, 600)
    window.wait_for_close()

main()