from Cell import Cell
from time import sleep
import random

class Maze:
    def __init__(
      self,
      x1: int,
      y1: int,
      num_rows: int,
      num_cols: int,
      cell_size_x: float,
      cell_size_y: float,
      win=None,
      seed=None
   ) -> None:
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        if win is not None:
            self.win = win
        else:
            self.win = None
        self.__cells = []
        self.__create_cells()
        self.__break_entrance_and_exit()
        self.__break_walls_r(0,0)
        self.__reset_cells_visited()
        
        if seed is not None:
            random.seed(seed)
        
    def __create_cells(self):
        for i in range (self.num_cols):
            columns:list[Cell] = []
            for j in range (self.num_rows):
                columns.append(Cell(self.win))
            self.__cells.append(columns)
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self.__draw_cell(i,j)
    
    def __draw_cell(self,i,j):
        x1 = i * self.cell_size_x + self.x1
        y1 = j * self.cell_size_y + self.y1
        x2 = x1 + self.cell_size_x
        y2 = y1 + self.cell_size_y
        self.__cells[i][j].draw(x1,y1,x2,y2)
        self.__animate()
    
    def __animate(self):
        if self.win is not None:
            self.win.redraw()
            sleep(.05)

    def __break_entrance_and_exit(self):
        self.__cells[0][0].has_top_wall = False
        self.__draw_cell(0,0)
        self.__cells[self.num_cols - 1][self.num_rows - 1].has_bottom_wall = False
        self.__draw_cell(self.num_cols - 1,self.num_rows - 1)
        
    def __break_walls_r(self, i, j):
        
        self.__cells[i][j].visited = True
        while True:
            indices = []
            # up, right, down, left
            if j > 0 and self.__cells[i][j-1].visited == False:
                indices.append((i,j-1))
            if i < self.num_cols - 1 and self.__cells[i+1][j].visited == False:
                indices.append((i+1,j))
            if j < self.num_rows - 1 and self.__cells[i][j+1].visited == False:
                indices.append((i,j+1))
            if i > 0 and self.__cells[i-1][j].visited == False:
                indices.append((i-1,j))
            
            if len(indices) == 0:
                self.__draw_cell(i,j)
                return
            
            dir = random.choice(indices)
        
            if dir[1] == j - 1:
                self.__cells[i][j].has_top_wall = False
                self.__cells[i][j-1].has_bottom_wall = False
            
            if dir[0] == i + 1:
                self.__cells[i][j].has_right_wall = False
                self.__cells[i+1][j].has_left_wall = False
                
            if dir[1] == j + 1:
                self.__cells[i][j].has_bottom_wall = False
                self.__cells[i][j+1].has_top_wall = False
            
            if dir[0] == i - 1:
                self.__cells[i][j].has_left_wall = False
                self.__cells[i-1][j].has_right_wall = False
            
            self.__break_walls_r(dir[0],dir[1])
        
    def __reset_cells_visited(self):
        for i in range (self.num_cols):
            for j in range (self.num_rows):
                self.__cells[i][j].visited = False
                
    def solve(self):
        solved = self._solve_r(0,0)
    
    def _solve_r(self,i,j):
        
        self.__animate()
        self.__cells[i][j].visited = True
        if i == self.num_cols - 1 and j == self.num_rows - 1:
            return True
        dirs = []
        #1=up, 2=right, 3=down, 4=left
        if j > 0 and self.__cells[i][j-1].visited == False and self.__cells[i][j].has_top_wall == False and self.__cells[i][j-1].has_bottom_wall == False:
            dirs.append((i,j-1))
        if i < self.num_cols - 1 and self.__cells[i+1][j].visited == False and self.__cells[i][j].has_right_wall == False and self.__cells[i+1][j].has_left_wall == False:
            dirs.append((i+1,j))
        if j < self.num_rows - 1 and self.__cells[i][j+1].visited == False and self.__cells[i][j].has_bottom_wall == False and self.__cells[i][j+1].has_top_wall == False:
            dirs.append((i,j+1))
        if i > 0 and self.__cells[i-1][j].visited == False and self.__cells[i][j].has_left_wall == False and self.__cells[i-1][j].has_right_wall == False:
            dirs.append((i-1,j))

        for dir in dirs:
            if dir[1] == j - 1:
                self.__cells[i][j].draw_move(self.__cells[i][j-1])
                solved = self._solve_r(i,j-1)
                if solved:
                    return True
                self.__cells[i][j].draw_move(self.__cells[i][j-1],True)
                
            if dir[0] == i + 1:
                self.__cells[i][j].draw_move(self.__cells[i+1][j])
                solved = self._solve_r(i+1,j)
                if solved:
                    return True
                self.__cells[i][j].draw_move(self.__cells[i+1][j],True)
                
            if dir[1] == j + 1:
                self.__cells[i][j].draw_move(self.__cells[i][j+1])
                solved = self._solve_r(i,j+1)
                if solved:
                    return True
                self.__cells[i][j].draw_move(self.__cells[i][j+1],True)
            
            if dir[0] == i - 1:
                self.__cells[i][j].draw_move(self.__cells[i-1][j])
                solved = self._solve_r(i-1,j)
                if solved:
                    return True
                self.__cells[i][j].draw_move(self.__cells[i-1][j],True)
        return False

