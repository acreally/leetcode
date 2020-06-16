import unittest

from src.cheapest_flights_within_k_stops.solution import Node, Solution


MORE_THAN_MAX_COST = 10001


class TestCheapestFlightsWithinKStops(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def testBuildAdjacencyLists(self):
        expected = {0: {1: 100, 2: 500}, 1: {2: 100}}
        flights = [[0,1,100],[1,2,100],[0,2,500]]

        result = self.solution.buildAdjacencyLists(flights)

        self.assertEqual(expected, result)

    def testInitializeNodesFirstNodeIsSource(self):
        number_of_nodes = 3
        source = 0
        source_node = Node(source)
        source_node.distance = 0
        expected = {0: source_node, 1: Node(1), 2: Node(2)}

        self._assertInitializeNodes(expected, number_of_nodes, source)

    def testInitializeNodesMiddleNodeIsSource(self):
        number_of_nodes = 3
        source = 1
        source_node = Node(source)
        source_node.distance = 0
        expected = {0: Node(0), 1: source_node, 2: Node(2)}

        self._assertInitializeNodes(expected, number_of_nodes, source)

    def testInitializeNodesLastNodeIsSource(self):
        number_of_nodes = 3
        source = 2
        source_node = Node(source)
        source_node.distance = 0
        expected = {0: Node(0), 1: Node(1), 2: source_node}

        self._assertInitializeNodes(expected, number_of_nodes, source)

    def _assertInitializeNodes(self, expected, number_of_nodes, source):
        result = self.solution.initializeNodes(number_of_nodes, source)

        self.assertEqual(expected, result)

    def testExtractMinAllEqualReturnFirstNode(self):
        expected = Node(0)
        nodes = {0: expected, 1: Node(1), 2: Node(2)}
        
        result = self.solution.extractMin(nodes)

        self.assertEqual(expected, result)

    def testExtractMinFirstNodeHasShortedDistance(self):
        expected = Node(0)
        expected.distance = 0
        nodes ={0: expected, 1: Node(1), 2: Node(2)}
        
        result = self.solution.extractMin(nodes)

        self.assertEqual(expected, result)

    def testExtractMinMiddleNodeHasShortedDistance(self):
        expected = Node(1)
        expected.distance = 0
        nodes = {0: Node(0), 1: expected, 2: Node(2)}
        
        result = self.solution.extractMin(nodes)

        self.assertEqual(expected, result)

    def testExtractMinLastNodeHasShortedDistance(self):
        expected = Node(2)
        expected.distance = 0
        nodes = {0: Node(0), 1: Node(1), 2: expected}
        
        result = self.solution.extractMin(nodes)

        self.assertEqual(expected, result)

    def testRelaxNewDistanceIsLessChangesParent(self):
        flight = (1, 100)
        current = Node(0)
        current.distance = 0
        target = Node(1)
        target.distance = MORE_THAN_MAX_COST
        target.depth = 0
        target.parent = None
        nodes = {1:target, 2: Node(2)}
        max_stops = 1

        self.solution.relax(flight, current, nodes, max_stops)

        self.assertEqual(100, nodes.get(1).distance)
        self.assertEqual(current, nodes.get(1).parent)
        self.assertEqual(1, nodes.get(1).depth)

    def testRelaxNewDistanceIsMoreDoesNotChangeParent(self):
        flight = (1, 100)
        current = Node(0)
        current.distance = 0
        parent = Node(2)
        target = Node(1)
        target.distance = 50
        target.depth = 2
        target.parent = parent
        nodes = {1: target, 2: parent}
        max_stops = 0

        self.solution.relax(flight, current, nodes, max_stops)

        self.assertEqual(50, nodes.get(1).distance)
        self.assertEqual(parent, nodes.get(1).parent)
        self.assertEqual(2, nodes.get(1).depth)

    def testShortestPathsAllDestinationsWithinNumberOfStops(self):
        adjacency_lists = {0: {1: 100, 2: 500}, 1: {2: 100}}
        n = 3
        src = 0
        node_0 = Node(0)
        node_0.distance = 0
        node_1 = Node(1)
        node_1.distance = 100
        node_1.depth = 1
        node_1.parent = node_0
        node_2 = Node(2)
        node_2.distance = 200
        node_2.depth = 2
        node_2.parent = node_1
        expected = {0: node_0, 1: node_1, 2: node_2}
        max_depth = 2

        result = self.solution.shortestPaths(adjacency_lists, n, src, max_depth)

        self.assertEqual(expected, result)

    def testShortestPathsOneDestinationNotWithinNumberOfStops(self):
        adjacency_lists = {0: {1: 100, 2: 500}, 1: {2: 100}}
        n = 3
        src = 0
        node_0 = Node(0)
        node_0.distance = 0
        node_1 = Node(1)
        node_1.distance = 100
        node_1.depth = 1
        node_1.parent = node_0
        node_2 = Node(2)
        node_2.distance = 500
        node_2.depth = 1
        node_2.parent = node_0
        expected = {0: node_0, 1: node_1, 2: node_2}
        max_depth = 1

        result = self.solution.shortestPaths(adjacency_lists, n, src, max_depth)

        self.assertEqual(expected, result)

    def testFindCheapestPriceEnoughStops(self):
        n = 3
        flights = [[0,1,100],[1,2,100],[0,2,500]]
        src = 0
        dst = 2
        k = 1

        result = self.solution.findCheapestPrice(n, flights, src, dst, k)

        self.assertEqual(200, result)

    def testFindCheapestPriceNotEnoughStops(self):
        n = 3
        flights = [[0,1,100],[1,2,100],[0,2,500]]
        src = 0
        dst = 2
        k = 0

        result = self.solution.findCheapestPrice(n, flights, src, dst, k)

        self.assertEqual(500, result)

    def testFindCheapestPriceNoRouteToDestination(self):
        n = 5
        flights = [[4,1,1],[1,2,3],[0,3,2],[0,4,10],[3,1,1],[1,4,3]]
        src = 2
        dst = 1
        k = 1

        result = self.solution.findCheapestPrice(n, flights, src, dst, k)

        self.assertEqual(-1, result)

    def testFindCheapestPriceMultipleRoutesToDestination(self):
        n = 5
        flights = [[4,1,1],[1,2,3],[0,3,2],[0,4,10],[3,1,1],[1,4,3]]
        src = 0
        dst = 1
        k = 5

        result = self.solution.findCheapestPrice(n, flights, src, dst, k)

        self.assertEqual(3, result)

    def testFindCheapestPriceSomethingElse(self):
        n = 4
        flights = [[0,1,1],[0,2,5],[1,2,1],[2,3,1]]
        src = 0
        dst = 3
        k = 1

        result = self.solution.findCheapestPrice(n, flights, src, dst, k)

        self.assertEqual(6, result)