from Window import Window
from Line import Line
from Point import Point

class Cell:
    def __init__(self,win=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        
        self.__x1 = -1.0
        self.__x2 = -1.0
        self.__y1 = -1.0
        self.__y2 = -1.0
        
        self.visited = False
        
        if win is not None:
            self.win = win
        else:
            self.win = None
        
    def draw(self,x1,y1,x2,y2):
        self.__x1 = x1
        self.__x2 = x2
        self.__y1 = y1
        self.__y2 = y2
        
        point_one = Point(x1,y1)
        point_two = Point(x1,y2)
        line_one = Line(point_one,point_two)
        color = ""
        color = "black" if self.has_left_wall == True else "white"
        if self.win is not None:
            self.win.draw_line(line_one,color)
        
        point_one = Point(x2,y1)
        point_two = Point(x2,y2)
        line_one = Line(point_one,point_two)
        color = "black" if self.has_right_wall == True else "white"
        if self.win is not None:
            self.win.draw_line(line_one,color)
    
        point_one = Point(x1,y1)
        point_two = Point(x2,y1)
        line_one = Line(point_one,point_two)
        color = "black" if self.has_top_wall == True else "white"
        if self.win is not None:
            self.win.draw_line(line_one,color)
        
        point_one = Point(x1,y2)
        point_two = Point(x2,y2)
        line_one = Line(point_one,point_two)
        color = "black" if self.has_bottom_wall == True else "white"
        if self.win is not None:
            self.win.draw_line(line_one,color)
    
    def draw_move(self, to_cell: "Cell",undo: bool = False) -> None:
        color = "gray"
        if not undo:
            color = "red"
            
        x1 = (self.__x1 + self.__x2) / 2
        y1 = (self.__y1 + self.__y2) / 2
        point_one = Point(x1,y1)
        
        x2 = (to_cell.__x1 + to_cell.__x2) / 2
        y2 = (to_cell.__y1 + to_cell.__y2) / 2
        point_two = Point(x2,y2)
        
        line = Line(point_one,point_two)
        if self.win is not None:
            self.win.draw_line(line,color)
    
