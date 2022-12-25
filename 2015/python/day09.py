import sys

class Vertex:
    def __init__(self, node) -> None:
        self.id = node
        self.adjacent = {}
        self.distance = sys.maxsize
        self.visited = False
        self.previous = None

    def add_neighbor(self, neighbor, weight=0):
        self.adjacent[neighbor] = weight

    def get_connections(self):
        return self.adjacent.keys()

    def get_id(self):
        return self.id

    def get_weight(self, neighbor):
        return self.adjacent[neighbor]

    def set_distance(self, dist):
        self.distance = dist

    def get_distance(self):
        return self.distance

    def set_previous(self, prev):
        self.previous = prev

    def set_visited(self):
        self.visited = True

    def __str__(self):
        return str(self.id) + ' adjacent: ' + str([x.id for x in self.adjacent])

    def __repr__(self) -> str:
        return f"{self.id}"

class Graph:
    def __init__(self):
        self.vert_dict = {}
        self.num_vertices = 0

    def __iter__(self):
        return iter(self.vert_dict.values())

    def add_vertex(self, node):
        self.num_vertices = self.num_vertices + 1
        new_vertex = Vertex(node)
        self.vert_dict[node] = new_vertex
        return new_vertex

    def get_vertex(self, n):
        if n in self.vert_dict:
            return self.vert_dict[n]
        else:
            return None

    def add_edge(self, frm, to, cost = 0):
        if frm not in self.vert_dict:
            self.add_vertex(frm)
        if to not in self.vert_dict:
            self.add_vertex(to)

        self.vert_dict[frm].add_neighbor(self.vert_dict[to], cost)
        self.vert_dict[to].add_neighbor(self.vert_dict[frm], cost)

    def get_vertices(self):
        return self.vert_dict.keys()

    def set_previous(self, current):
        self.previous = current

    def get_previous(self, current):
        return self.previous

def path_complete(graph, path):
    last_vert = path[-1]

    for neightbor in last_vert.get_connections():
        if not graph.get_vertex(neightbor.id).visited:
            return False
    return True

def path_len(path):
    len = 0
    for vert in path:
        len += vert.get_distance()
    return len


def get_paths(graph, path, all_paths, min_len):
    if path_complete(graph, path) and path_len(path) > min_len:
        all_paths.append(path.copy())
        return path_len(path)

    for neightbor in path[-1].get_connections():
        if not graph.get_vertex(neightbor.id).visited:
            neightbor.distance = neightbor.get_weight(graph.get_vertex(path[-1].id))
            path.append(neightbor)
            neightbor.visited = True
            min_len = get_paths(graph, path, all_paths, min_len)
            neightbor.distance = sys.maxsize
            neightbor.visited = False
            path.pop()
    return min_len

def get_all_paths(graph, vert, min_len):
    all_paths = []
    path = [vert]
    vert.visited = True
    vert.distance = 0

    min_len = get_paths(graph, path, all_paths, min_len)
    vert.visited = False
    vert.distance = sys.maxsize
    return all_paths, min_len

if __name__ == '__main__':
    graph = Graph()
    min_len = -1
    all_paths = []
    with open('./resources/day09', 'r') as f:
        for line in f.readlines():
            connection = line.replace('\n', '').replace('=', '').replace('to', '').split()
            graph.add_edge(connection[0], connection[1], int(connection[2]))
    for vert in graph:
        paths, min_len = get_all_paths(graph, vert, min_len)
        all_paths += paths
    for path in all_paths:
        for vert in path:
            print(vert.id, end=' ')
        print()
    print(min_len)