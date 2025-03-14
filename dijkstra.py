import heapq

class Graph:
    def __init__(self):
        self.nodes = {}

    def add_node(self, node):
        if node not in self.nodes:
            self.nodes[node] = {}
        # On aura tendance à préférer la notation
        # if not node in self.nodes

    def add_edge(self, source, target, weight):
        if source not in self.nodes:
            self.add_node(source)
        if target not in self.nodes:
            self.add_node(target)
        # On vérifie déjà si c'est le noeud est dans self.nodes dans la méthode add_node
        for node in [source, target]:
            self.add_node(node)
        # Devrait suffire

        self.nodes[source][target] = weight

    def get_neighbors(self, node):
        return self.nodes[node]

class Dijkstra:
    def __init__(self, graph):
        self.graph = graph

    def find_shortest_path(self, start, end):

        distances = {node: float('inf') for node in self.graph.nodes}
        distances[start] = 0
        priority_queue = [(0, start)]
        previous_nodes = {node: None for node in self.graph.nodes}

        while priority_queue:
            current_distance, current_node = heapq.heappop(priority_queue)

            if current_node == end:
                break

            if current_distance > distances[current_node]:
                continue

            for neighbor, weight in self.graph.get_neighbors(current_node).items():
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous_nodes[neighbor] = current_node
                    heapq.heappush(priority_queue, (distance, neighbor))

        path = []
        current = end
        while current is not None:
            path.insert(0, current)
            current = previous_nodes[current]
        # https://docs.python.org/3/library/queue.html

        if distances[end] == float('inf'):
            return None, float('inf')
        return path, distances[end]

graph = Graph()
graph.add_edge("A", "B", 1)
graph.add_edge("A", "C", 4)
graph.add_edge("B", "C", 2)
graph.add_edge("B", "D", 6)
graph.add_edge("C", "D", 3)

dijkstra = Dijkstra(graph)
shortest_path, distance = dijkstra.find_shortest_path("A", "D")
print(f"Chemin le plus court : {shortest_path} avec une distance de {distance}")
# Si ce genre d'algorythmes vous interesse, je vous conseille de regarder https://cs50.harvard.edu/ai/2024/weeks/0/
# Ainsi que la librairie https://docs.scipy.org/doc/scipy/