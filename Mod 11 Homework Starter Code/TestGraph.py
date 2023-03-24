import unittest
from Graph import Graph, AdjacencySetGraph as ASG, EdgeSetGraph as ESG
from FlightMap import FlightMap
from SnowMap import SnowMap

class TestGraph(unittest.TestCase):
    def test_Graph_notimplemented(self):
        # These methods should only be implemented by child classes
        with self.assertRaises(NotImplementedError):
            g = Graph(set(), set())

        with self.assertRaises(NotImplementedError):
            Graph.add_vertex(1, 1)

        with self.assertRaises(NotImplementedError):
            Graph.remove_vertex(1, 1)

        with self.assertRaises(NotImplementedError):
            Graph.add_edge(1, 1, 2)

        with self.assertRaises(NotImplementedError):
            Graph.remove_edge(1, 1, 2)

        with self.assertRaises(NotImplementedError):
            Graph.neighbors(1, 1)

        with self.assertRaises(NotImplementedError):
            Graph.weight(1, 1, 2)

    def test_Graph_Hierarchy(self):
        for Graph_DS in ASG, ESG:
            g = Graph_DS()
            self.assertIsInstance(g, Graph)

    def test_Graph_nbrs(self):
        for Graph_DS in ASG, ESG:
            V = {1, 2, 3}
            E = {(1, 2), (2, 3)}
            g = Graph_DS(V, E)

            nbrs = set()
            for n in g.neighbors(2):
                nbrs.add(n)
            self.assertEqual(nbrs, {1, 3})

            nbrs = set()
            for n in g.neighbors(1):
                nbrs.add(n)
            self.assertEqual(nbrs, {2})

            nbrs = set()
            for n in g.neighbors(3):
                nbrs.add(n)
            self.assertEqual(nbrs, {2})

    def test_Graph_weight(self):
        for Graph_DS in ASG, ESG:
            V = {1, 2, 3}
            E = {(1, 2, 1.2), (2, 3, 3.2)}
            G = Graph_DS(V, E)

            self.assertEqual(G.weight(1, 2), 1.2)
            self.assertEqual(G.weight(2, 1), 1.2)
            self.assertEqual(G.weight(2, 3), 3.2)
            self.assertEqual(G.weight(3, 2), 3.2)

    def test_Graph_searches(self):
        for Graph_DS in ASG, ESG:
            V = {1, 2, 3}
            E = {(1, 2), (2, 3)}
            g = Graph_DS(V, E)

            self.assertEqual(g.bfs(1), {1:None, 2:1, 3:2})
            self.assertEqual(g.bfs(2), {2:None, 1:2, 3:2})
            self.assertEqual(g.dfs(1), {1:None, 2:1, 3:2})
            self.assertEqual(g.dfs(2), {2:None, 1:2, 3:2})

    def test_Graph_dijkstra(self):
        for Graph_DS in ASG, ESG:
            V = {1,2,3}
            E = {(1,2, 4.6), (2, 3, 9.2), (1, 3, 3.1)}
            G = Graph_DS(V, E)
            tree, D = G.dijkstra(1)
            self.assertDictEqual(tree, {1:None, 3:1, 2:1})
            self.assertDictEqual(D, {1:0, 3:3.1, 2:4.6})

            # Adding an edge creates a shortcut to vertex 2.
            G.add_edge(3, 2, 1.1)
            tree, D = G.dijkstra(1)
            self.assertDictEqual(tree, {1:None, 3:1, 2:3})
            self.assertDictEqual(D, {1:0, 3:3.1, 2:4.2})

    def test_Graph_primm(self):
        for Graph_DS in ASG, ESG:
            V = {1,2,3,4,5}
            E = {(1, 2, 1), (2, 3, 1), (1, 3, 2), (3, 4, 1), (3, 5, 3), (4, 5, 2)}
            G = Graph_DS(V, E)

            tree = G.primm(1)
            msp = {1: None, 2: 1, 3: 2, 4: 3, 5: 4} # minimum spanning tree
            self.assertDictEqual(tree, msp)

class TestFlightMap(unittest.TestCase):
    def test_reachable(self):
        cities = {'BOS', 'BDL', 'HND', 'JFK', 'MIA', 'LAX', 'DFW'}
        flights = {('BOS', 'HND'), ('BOS', 'BDL'), ('BOS', 'JFK'), ('BOS', 'MIA'), ('JFK', 'LAX'), ('JFK', 'MIA'), ('LAX', 'DFW')}
        fm = FlightMap(cities, flights)
        reach = {'MIA', 'JFK', 'BOS', 'BDL', 'HND'}
        self.assertEqual(fm.reachable('BOS', 1), reach)

class TestSnowMap(unittest.TestCase):
    def test_plow_from(self):
        cities={"Hartford", "Waterbury", "Danbury", "Greenwich", "Norwalk", "Bridgeport","New Haven", "New London", "Mystic"}
        roads={("Hartford", "Waterbury", 31), ("Hartford", "New Haven", 39),("Hartford", "New London", 51), ("Hartford", "Mystic", 53), ("Waterbury", "Danbury", 28),("New Haven", "Bridgeport", 19), ("New Haven", "New London", 48),("New London", "Mystic", 9), ("Danbury", "Greenwich", 40), ("Danbury", "Norwalk", 22),("Danbury", "Bridgeport", 29), ("Bridgeport", "Norwalk", 15), ("Norwalk", "Greenwich", 15)}
        sm = SnowMap(cities, roads)

        tree, D = sm.plow_from("Hartford")

        D_correct = {'Hartford': 0, 'Waterbury': 31, 'New Haven': 39, 'New London': 51, 'Mystic': 53, 'Bridgeport': 58, 'Danbury': 59, 'Norwalk': 73, 'Greenwich': 88}

        self.assertDictEqual(D, D_correct)

unittest.main()
