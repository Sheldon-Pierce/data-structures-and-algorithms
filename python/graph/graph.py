from queues.queues import Queue


class Graph:
    """
    Put docstring here
    """

    def __init__(self):
        self.nodes = []
        self.adjacency_list = {}

    def add_node(self, value):
        node = Vertex(value)
        self.nodes.append(node)
        return node

    def add_edge(self, start_node, end_node, weight=1):
        if start_node not in self.nodes or end_node not in self.nodes:
            raise KeyError("Start or end node does not exist in the graph.")

        if start_node in self.adjacency_list:
            self.adjacency_list[start_node].append(Edge(end_node, weight))
        else:
            self.adjacency_list[start_node] = [Edge(end_node, weight)]

    def size(self):
        return len(self.nodes)

    def get_neighbors(self, vertex):
        if vertex in self.adjacency_list:
            return self.adjacency_list[vertex]
        else:
            return []

    def get_nodes(self):
        return self.nodes

    def breadth_first(self, root):
        nodes = []
        queue = Queue()
        visited = []

        queue.enqueue(root)
        visited.append(root)

        while not queue.is_empty():
            current = queue.dequeue()
            nodes.append(current.value)

            for neighbor in self.get_neighbors(current):
                if neighbor.vertex not in visited:
                    queue.enqueue(neighbor.vertex)
                    visited.append(neighbor.vertex)

        return nodes



class Vertex:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return self.value


class Edge:
    def __init__(self, vertex, weight):
        self.vertex = vertex
        self.weight = weight

    def __str__(self):
        return self.weight
