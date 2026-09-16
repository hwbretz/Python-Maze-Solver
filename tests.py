import unittest

from Maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._Maze__cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._Maze__cells[0]),
            num_rows,
        )
    
    def test_visited_reset(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        for i in range (len(m1._Maze__cells)):
            for j in range (len(m1._Maze__cells[0])):
                self.assertEqual(m1._Maze__cells[i][j].visited,False)

if __name__ == "__main__":
    unittest.main()
