DLS(node, goal, limit):
    if node == goal:
        return True

    if limit == 0:
        return False

    for child in children(node):
        if DLS(child, goal, limit-1):
            return True

    return False
