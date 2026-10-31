BFS(start, goal):
    queue = [start]
    visited = []

    while queue:
        node = queue.pop(0)

        if node == goal:
            return True

        if node not in visited:
            visited.append(node)
            queue.extend(children(node))

    return False
