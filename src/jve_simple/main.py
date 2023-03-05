from collections import defaultdict, deque


class Graph:
    def __init__(self, adjacency_list: dict[list[str]]) -> None:
        self.adjacency_list = adjacency_list
        self.predecessors = self._make_predecessors()

    def _make_predecessors(self):
        # Flip adjacency list (successors) to create predecessors
        predecessors = {node: [] for node in self.adjacency_list.keys()}
        for node, successors in self.adjacency_list.items():
            for successor in successors:
                predecessors[successor].append(node)
        return dict(predecessors)

    def topological_sort(self):
        def dfs(node: str):
            nonlocal queue, visited

            # Mark node as visited
            visited.add(node)

            # Ensure all parents are processed before processing node
            for prev_node in self.predecessors[node]:
                if prev_node not in visited:
                    dfs(prev_node)

            # Must appear
            queue.append(node)

        queue = deque()
        visited = set()
        # Use each unvisited node as source if they have no already been visited
        for source_node in self.predecessors.keys():
            if source_node not in visited:
                dfs(source_node)
        return list(queue)


def run():
    alist = {
        "1": ["2", "3", "4"],
        "2": ["3"],
        "4": [],
        "3": ["4"],
    }
    g = Graph(alist)
    print(g.adjacency_list)
    print(g.predecessors)
    print(g.topological_sort())
