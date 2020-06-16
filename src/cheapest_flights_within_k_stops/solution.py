from typing import Dict, List, Tuple

MORE_THAN_MAX_COST = 10001

class Solution:
    adjacency_lists = None

    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        self.adjacency_lists = self.buildAdjacencyLists(flights)
        shortest_paths = self.shortestPaths(self.adjacency_lists, n, src, k + 1)
        if not shortest_paths:
            return -1
        result = shortest_paths[dst].distance
        return -1 if result >= MORE_THAN_MAX_COST else result

    def buildAdjacencyLists(self, flights: List[List[int]]) -> Dict:
        adjacency_lists = {}
        for flight in flights:
            source = flight[0]
            destination = flight[1]
            cost = flight[2]
            if source not in adjacency_lists:
                adjacency_lists[source] = {}
            adjacency_lists[source][destination]  = cost
        return adjacency_lists

    def shortestPaths(self, adjacency_lists: Dict, n: int, src: int, max_depth: int) -> List:
        nodes = self.initializeNodes(n, src)
        seen = {}
        while nodes:
            current = self.extractMin(nodes)
            seen[current.value] = current
            flights = adjacency_lists.get(current.value, {})
            for flight in flights.items():
                self.relax(flight, current, nodes, max_depth)
        return seen

    def initializeNodes(self, n: int, src: int) -> Dict:
        nodes = {}
        for i in range(n):
            node = Node(i)
            if i == src:
                node.distance = 0
            nodes[i] = node
        return nodes

    def extractMin(self, nodes: Dict):
        sorted_nodes = [k for k, _ in sorted(nodes.items(), key=lambda item: item[1].distance)]
        return nodes.pop(sorted_nodes[0])

    def relax(self, flight: Tuple, current, nodes: Dict, max_depth: int):
        destination = flight[0]
        cost = flight[1]
        distance = current.distance + current.distance_offset + cost
        neighbour = nodes.get(destination)
        if neighbour and distance < neighbour.distance:
            neighbour.setParent(current, max_depth)
            neighbour.distance = distance

class Node:
    distance = MORE_THAN_MAX_COST
    distance_offset = 0
    value = -1
    parent = None
    depth = 0

    def __init__(self, value):
        self.value = value

    def setParent(self, parent, max_depth):
        self.parent = parent
        self.depth = parent.depth + 1
        if self.depth >= max_depth:
            self.distance_offset = MORE_THAN_MAX_COST

    def __eq__(self, other):
        if isinstance(other, Node):
            if self.value != other.value:
                return False
            if self.distance != other.distance:
                return False
            if self.parent != other.parent:
                return False
            if self.depth != other.depth:
                return False
            return True
        return False

    def __repr__(self):
        return "value: {}, distance: {}, depth: {}, parent: {}".format(self.value, self.distance, self.depth, self.parent)
