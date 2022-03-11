from maze import path_from
from functions import lenghtM, returnP, returnKey


def a(maze):      #Algorithm A*
    start_node = maze.find_node('S')
    start_node.cost = 0
    q = [start_node]
    while len(q) > 0:
        q.sort(reverse=False, key=returnP)    
        node = q.pop(0)  # FIFO
        node.visited = True
        if node.type == 'E':
            return path_from(node)
        children = maze.get_possible_movements(node)
        for child in children:
            newCost = node.cost
            if child.type == '!':
               newCost += 5
            else:
               newCost += 1
            newP = lenghtM(child)
            if newCost < child.cost:
               child.priority = newP+newCost
               child.cost = newCost
               child.parent = node
               q.append(child)

    return None


def gbfs(maze):   #Algorithm Greedy Best-first search
    start_node = maze.find_node('S')
    q = [start_node]
    while len(q) > 0:
        q.sort(reverse = False, key=lenghtM)
        current_node = q.pop(0)
        current_node.visited = True
        if current_node.type == 'E':
            return path_from(current_node)
        children = maze.get_possible_movements(current_node)
        for child in children:
            if not child.visited:
                child.parent = current_node
                q.append(child)

    return None
    

def dijkstra(maze):     #Dijkstra's algorithm
    start_node = maze.find_node('S')
    start_node.cost = 0
    q = [start_node]
    while len(q) > 0:
        q.sort(reverse=False, key=returnKey)    
        node = q.pop(0)  # FIFO
        node.visited = True
        if node.type == 'E':
            return path_from(node)
        children = maze.get_possible_movements(node)
        for child in children:
            newCost = node.cost
            if child.type == '!':
               newCost += 5
            else:
               newCost += 1
            
            if newCost < child.cost:
               child.cost = newCost
               child.parent = node
               q.append(child)

    return None
