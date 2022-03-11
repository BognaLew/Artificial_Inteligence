from search_algorithms import a, dijkstra, gbfs
from variables import maze

maze.draw()
maze.path = a(maze)   #change to dijkstra or gbfs to see how they work
print()
maze.draw()
print('path length: ', len(maze.path))
for node in maze.path:
    print(f'({node.x}, {node.y})', end=' ')
print()

