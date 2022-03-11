from variables import end_node


def returnKey(node):
    return node.cost


def returnP(node):
    return node.priority


def lenghtM(start):
    return abs(start.x - end_node.x) + abs(start.y - end_node.y)
