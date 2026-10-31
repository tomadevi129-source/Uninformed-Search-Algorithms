UCS(start, goal):
    priority_queue = [(0, start)]

    while priority_queue:
        cost, node = pop_lowest(priority_queue)

        if node == goal:
            return cost

        for child, step_cost in children(node):
            new_cost = cost + step_cost
            insert(priority_queue, (new_cost, child))

    return False
