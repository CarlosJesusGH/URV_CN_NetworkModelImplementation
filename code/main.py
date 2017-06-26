import networkx as nx
import time
from CustomNetworkCreator import *
import utils as utils
import settings as settings

# Mark start time
startTime = time.clock()
# ----------------------------------------------------------

# Remove plots directory
utils.silent_remove(settings.output_plots, True)
utils.silent_remove(settings.output_graphs, True)

# declare network building class
cnc = CustomNetworkCreator()

# Erdös-Rényi (ER)
if True:
    ns = [20, 50, 100]                          # n: The number of nodes.
    ps = [0.00, 0.01, 0.02, 0.03, 0.05, 0.1]    # p: Probability for edge creation.
    # Iterate over n's and p's
    for n in ns:
        for p in ps:
            G = cnc.erdos_renyi_network(n=n, p=p)
            iter_desc = "erdos_renyi_[n=" + str(n) + ",p=" + str(p) + "]"
            utils.save_graph_in_pajek_format(G, iter_desc)
            utils.draw_network(G, iter_desc)
            utils.draw_degree_distribution(G, iter_desc)

# Watts-Strogatz (WS)
if True:
    ns = [20, 50, 100]                      # n: The number of nodes
    k = 4                                   # k: Each node is joined with its ``k`` nearest neighbors in a ring topology
    ps = [0.0, 0.1, 0.2, 0.5, 0.9, 1.0]     # p: The probability of rewiring each edge
    # Iterate over n's and p's
    for n in ns:
        for p in ps:
            G = cnc.watts_strogatz_network(n=n, k=k, p=p)
            iter_desc = "watts_strogatz_[n=" + str(n) + ",k=" + str(k) + ",p=" + str(p) + "]"
            utils.save_graph_in_pajek_format(G, iter_desc)
            utils.draw_network(G, iter_desc)
            utils.draw_degree_distribution(G, iter_desc)

# Barabási & Albert (BA)
if True:
    ns = [50, 100, 1000]                      # n : Number of nodes
    ms = [1, 2, 4, 10]                      # m : Number of edges to attach from a new node to existing nodes
    # Iterate over n's and m's
    for n in ns:
        for m in ms:
            G = cnc.barabasi_albert_network(n=n, m=m)
            iter_desc = "barabasi_albert_[n=" + str(n) + ",m=" + str(m) + "]"
            utils.save_graph_in_pajek_format(G, iter_desc)
            utils.draw_network(G, iter_desc)
            utils.draw_degree_distribution(G, iter_desc, plot_slope=True)


# ----------------------------------------------------------
# Show execution statistics after finishing
measuredTime = time.clock() - startTime
print('Execution time = {}'.format(measuredTime))
