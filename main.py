from tkinter import *


class Robot(Frame):

    def __init__(self, current_canvas, scale=10, x=0, y=0):
        super().__init__()
        self.maxY = scale * (13 + y)
        self.y = y
        self.x = x
        self.scale = scale
        self.canvas = current_canvas
        self.draw()

    def draw(self):
        self.canvas.create_rectangle((5 + self.x) * self.scale, self.maxY - 3 * self.scale, (7 + self.x) * self.scale,
                                     self.maxY - 0 * self.scale)
        self.canvas.create_rectangle((8 + self.x) * self.scale, self.maxY - 3 * self.scale, (10 + self.x) * self.scale,
                                     self.maxY - 0 * self.scale)
        self.canvas.create_rectangle((5 + self.x) * self.scale, self.maxY - 9 * self.scale, (10 + self.x) * self.scale,
                                     self.maxY - 3 * self.scale)
        self.canvas.create_rectangle((4 + self.x) * self.scale, self.maxY - 9 * self.scale, (5 + self.x) * self.scale,
                                     self.maxY - 6 * self.scale)
        self.canvas.create_rectangle((10 + self.x) * self.scale, self.maxY - 9 * self.scale, (13 + self.x) * self.scale,
                                     self.maxY - 8 * self.scale)
        self.canvas.create_rectangle((7 + self.x) * self.scale, self.maxY - 10 * self.scale, (8 + self.x) * self.scale,
                                     self.maxY - 9 * self.scale)
        self.canvas.create_rectangle((6 + self.x) * self.scale, self.maxY - 13 * self.scale, (9 + self.x) * self.scale,
                                     self.maxY - 10 * self.scale)
        self.canvas.pack()

    def move_to(self, x, y):
        self.clear()
        self.x = x
        self.y = y
        self.maxY = self.scale * (13 + y)
        self.draw()

    def clear(self):
        self.canvas.delete("all")

    def set_scale(self, scale):
        self.clear()
        self.scale = scale
        self.maxY = self.scale * (13 + self.y)
        self.draw()

    def rotate(self, angle):
        self
        #TODO




if __name__ == '__main__':
    root = Tk()
    root.title("Robot")
    root.geometry("500x500")
    canvas = Canvas()
    canvas.pack(side="top", fill="both", expand=True)
    robot = Robot(current_canvas=canvas, x=0, y=10)
    robot.move_to(10, 20)
    robot.set_scale(5.5)
    root.mainloop()
