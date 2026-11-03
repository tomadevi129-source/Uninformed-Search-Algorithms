
# Breadth First Search (BFS)

from collections import deque

# Define the graph
graph = {
    'A': ['B', 'C', 'D'],
    'B': ['E', 'F'],
    'C': ['G'],
    'D': ['H', 'I'],
    'E': [],
    'F': [],
    'G': [],
    'H': [],
    'I': []
}

# Function to get children
def children(node):
    return graph.get(node, [])

# Function to display the tree
def show_tree(node, prefix="", is_last=True):
    print(prefix + ("└── " if is_last else "├── ") + node)

    child_nodes = children(node)

    for i, child in enumerate(child_nodes):
        show_tree(
            child,
            prefix + ("    " if is_last else "│   "),
            i == len(child_nodes) - 1
        )

# BFS Algorithm
def BFS(start, goal):
    queue = deque([start])
    visited = []

    print("\nBFS Traversal:")

    while queue:
        node = queue.popleft()

        if node not in visited:
            visited.append(node)
            print("Visiting:", node)

            if node == goal:
                print("\nGoal Found:", goal)
                print("Traversal Order:", " -> ".join(visited))
                return True

            queue.extend(children(node))

    print("\nGoal Not Found!")
    print("Traversal Order:", " -> ".join(visited))
    return False


# Main Program
start = 'A'
goal = 'G'

print("========== BFS SEARCH TREE ==========")
show_tree(start)

print("\n========== BFS SEARCH RESULT ==========")
BFS(start, goal)
