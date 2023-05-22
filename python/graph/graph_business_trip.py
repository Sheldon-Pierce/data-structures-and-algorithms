def direct_flights(graph, names):
    current_node = None
    total_distance = 0

    for name in names:
        node = None
        for graph_node in graph.get_nodes():
            if graph_node.value == name:
                node = graph_node
                break

        if not node:
            return False, 0

        if current_node:
            edge = None
            for neighbor in graph.get_neighbors(current_node):
                if neighbor.vertex == node:
                    edge = neighbor
                    break

            if not edge:
                return False, 0

            total_distance += edge.weight

        current_node = node

    return True, total_distance
