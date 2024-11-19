from collections import defaultdict, deque

class Graph:
    def __init__(self, directed=False):
        """
        Initialize the graph.
        :param directed: True if the graph is directed, False otherwise.
        """
        self.graph = defaultdict(list)  # Adjacency list representation
        self.directed = directed

    def add_vertex(self, vertex):
        """
        Add a vertex to the graph.
        """
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, u, v):
        """
        Add an edge between vertex u and vertex v.
        :param u: Start vertex.
        :param v: End vertex.
        """
        self.graph[u].append(v)
        if not self.directed:
            self.graph[v].append(u)

    def bfs(self, start):
        """
        Perform Breadth-First Search (BFS) starting from the given vertex.
        :param start: The starting vertex.
        :return: List of vertices in BFS order.
        """
        visited = set()
        queue = deque([start])
        bfs_order = []

        while queue:
            vertex = queue.popleft()
            if vertex not in visited:
                visited.add(vertex)
                bfs_order.append(vertex)
                for neighbor in self.graph[vertex]:
                    if neighbor not in visited:
                        queue.append(neighbor)

        return bfs_order

    def dfs(self, start):
        """
        Perform Depth-First Search (DFS) starting from the given vertex.
        :param start: The starting vertex.
        :return: List of vertices in DFS order.
        """
        visited = set()
        dfs_order = []

        def dfs_recursive(vertex):
            if vertex not in visited:
                visited.add(vertex)
                dfs_order.append(vertex)
                for neighbor in self.graph[vertex]:
                    dfs_recursive(neighbor)

        dfs_recursive(start)
        return dfs_order

    def display(self):
        """
        Display the graph as an adjacency list.
        """
        for vertex, neighbors in self.graph.items():
            print(f"{vertex}: {neighbors}")

# Create an undirected graph
g = Graph()

# Add edges
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(2, 4)
g.add_edge(3, 4)
g.add_edge(4, 5)

# Display the graph
print("Graph:")
g.display()

# Perform BFS
print("\nBFS starting from vertex 1:")
print(g.bfs(1))  # Output: [1, 2, 3, 4, 5]

# Perform DFS
print("\nDFS starting from vertex 1:")
print(g.dfs(1))  # Output: [1, 2, 4, 5, 3]