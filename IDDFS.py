IDDFS(start, goal, max_depth):
    for depth in range(max_depth + 1):
        if DLS(start, goal, depth):
            return True
    return False
