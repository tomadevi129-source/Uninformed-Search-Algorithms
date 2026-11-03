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

# Tree দেখানোর জন্য GitHub-friendly ফাংশন
def show_tree(node, prefix=""):
    print(prefix + node)
    child_nodes = children(node)
    for i, child in enumerate(child_nodes):
        connector = "+-- " if i == len(child_nodes) - 1 else "|-- "
        show_tree(child, prefix + "    " + connector)

# আপনার দেওয়া BFS লজিক
def BFS(start, goal):
    queue = [start]
    visited = []
    
    print("\nBFS Traversal:")
    while queue:  
        node = queue.pop(0)  

        if node == goal:  
            print("\nGoal Found:", goal)
            print("Traversal Order:", " -> ".join(visited + [node]))
            return True  

        if node not in visited:  
            visited.append(node)  
            print("Visiting:", node)
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

