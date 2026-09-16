from tkinter import Tk, BOTH, Canvas
from Line import Line
from Point import Point

class Window:
    def __init__(self,width,height):
        self.width = width
        self.height = height
        
        self.root = Tk()
        self.root.title("Maze Solver")
        self.canvas = Canvas(self.root, bg="white", width = self.width, height = self.height)
        self.canvas.pack(fill=BOTH, expand=1)
        self.win_open = False
        self.root.protocol("WM_DELETE_WINDOW", self.close)
        
    def redraw(self) -> None:
        self.root.update_idletasks()
        self.root.update()
    
    def wait_for_close(self):
        self.win_open = True
        while self.win_open:
            self.redraw()
    
    def close(self):
        self.win_open = False
        
    def draw_line(self,line,fill_color):
        line.draw(self.canvas,fill_color)

