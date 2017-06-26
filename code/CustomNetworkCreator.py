import networkx as nx
import itertools
import random

class CustomNetworkCreator:

    def erdos_renyi_network(self, n, p):
        # Initialize graph
        G = nx.Graph()

        # Initialize nodes
        nodes = range(n)
        # print("Nodes:");
        # for i in nodes: print(i, end = ' ')
        # Add nodes to graph
        # G.add_nodes_from(nodes)
        for node in nodes:
            G.add_node(node)

        # Initialize edges
        # combinations(iterable, r): Return r length subsequences of elements from the input iterable.
        # Elements are treated as unique based on their position, not on their value. So if the input elements are unique, there will be no repeat values in each combination.
        edges = itertools.combinations(range(n), 2)
        # print("\nEdges:"); print(edges)
        # Add edges to graph
        for edge in edges:
            if random.random() < p:
                # *args: unpack a tuple into arguments of a function
                # it is the same than doing G.add_edge(e[0],e[1])
                G.add_edge(*edge)
        return G
        # return nx.erdos_renyi_graph(n, p)

    def watts_strogatz_network(self, n, k, p):
        # First create the nodes, then connects every node to k neighbors, and finally rewire edges in each node according to a probability p.

        # Initialize graph
        G = nx.Graph()

        # Initialize nodes
        nodes = list(range(n))
        #print("Nodes:"); print(nodes)

        # connect each node to k/2 neighbors
        for j in range(1, k // 2 + 1):
            # print("Targets_____")
            targets = nodes[j:] + nodes[0:j]  # first j nodes are now last in list
            # print(targets)
            print(list(zip(nodes, targets)))
            # zip: returns a list of tuples, where the i-th tuple contains
            # the i-th element from each of the argument sequences or iterables
            for edge in zip(nodes, targets):
                # *args: unpack a tuple into arguments of a function
                # it is the same than doing G.add_edge(e[0],e[1])
                G.add_edge(*edge)

        # rewire edges from each node
        # loop over all nodes in order (label) and neighbors in order (distance)
        # no self loops or multiple edges allowed
        for j in range(1, k // 2 + 1):  # outer loop is neighbors
            targets = nodes[j:] + nodes[0:j]  # first j nodes are now last in list
            # inner loop in node order
            for u, v in zip(nodes, targets):
                if random.random() < p:
                    w = random.choice(nodes)
                    # Enforce no self-loops or multiple edges
                    while w == u or G.has_edge(u, w):
                        w = random.choice(nodes)
                        if G.degree(u) >= n - 1:
                            break  # skip this rewiring
                    else:
                        G.remove_edge(u, v)
                        G.add_edge(u, w)

        return G


    def barabasi_albert_network(self, n, m):
        #First create a small graph with size m, and then every step it adds one new node and connects it to m new nodes according to a random selection from existing nodes. This random selection gives priority to nodes with higher grade by using and array where node number is repeated as many times as its grade value.

        # Add m initial nodes (m0 in barabasi-speak)
        # G = empty_graph(m)
        G = nx.Graph()

        # Initialize m0 nodes
        m0 = range(m)
        # Add nodes to graph
        # G.add_nodes_from(nodes)
        for node in m0:
            G.add_node(node)

        # print("Target Nodes:");
        # print(list(range(m)))
        # Target nodes for new edges
        targets = list(range(m))
        # List of existing nodes, with nodes repeated once for each adjacent edge
        repeated_nodes = []
        # Start adding the other n-m nodes. The first node is m.
        source = m
        while source < n:
            # print("Source_____")
            # print(list(zip([source] * m, targets)))
            # Add edges to m nodes from the source. (The nodes will be automatically added if they are not already in the graph)
            G.add_edges_from(zip([source] * m, targets))
            # Add one node to the list for each new edge just created.
            repeated_nodes.extend(targets)
            # And the new node "source" has m edges to add to the list.
            repeated_nodes.extend([source] * m)
            # print("Repeated nodes:"); print(repeated_nodes)
            # Now choose m unique nodes from the existing nodes
            # Pick uniformly from repeated_nodes (preferential attachement)
            targets = self._random_subset(repeated_nodes, m)
            source += 1
        return G


    def _random_subset(self, seq, m):
        """ Return m unique elements from seq.

        This differs from random.sample which can return repeated
        elements if seq holds repeated elements.
        """
        targets = set()
        while len(targets) < m:
            x = random.choice(seq)
            targets.add(x)
        return targets
