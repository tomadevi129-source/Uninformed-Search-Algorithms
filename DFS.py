DFS(node, goal, visited):
    if node == goal:
        return True

    visited.add(node)

    for child in children(node):
        if child not in visited:
            if DFS(child, goal, visited):
                return True

    return False
