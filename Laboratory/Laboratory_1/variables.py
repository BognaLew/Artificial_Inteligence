import sys
from maze import Maze


maze = Maze.from_file(sys.argv[1])
end_node = maze.find_node('E')
