import utils_latex
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
from networkx.drawing.nx_pydot import graphviz_layout
import os, errno, shutil
import warnings
import settings as settings
import pickle
import collections as coll
import math as math
from sklearn import linear_model as sklearn_linear_model

# Filter <MatplotlibDeprecationWarning> warnings when plotting with networkx
# warnings.filterwarnings("ignore", category=UserWarning)


def save_graph_in_pajek_format(G, file_name):
    # Print graph details
    print(file_name); print(G.nodes(), G.edges())
    # Build the containing directory in case it doesn't exist
    output_file = settings.output_graphs + file_name + '_graph.net'
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    # Write network to file
    nx.write_pajek(G, output_file)
    return

def draw_degree_distribution(G, file_name, plot_slope=False):
    # Get degree sequence from network
    degree_sequence = sorted(nx.degree(G).values(), reverse=True)  # degree sequence

    # Build output path from file_name
    output_path = settings.output_plots + file_name

    fig = plt.figure(figsize=(12, 6))
    ax = plt.subplot(121)
    min_degree = min(degree_sequence)
    max_degree = max(degree_sequence)
    bins_lin = np.linspace(min_degree, max_degree, num=settings.bins_lin_num, endpoint=True)

    lin_ordered_counter = coll.OrderedDict(coll.Counter(degree_sequence))
    pdf_lin = list(lin_ordered_counter.keys())
    pdf_lin_weights = list(lin_ordered_counter.values())
    pdf_lin_weights = [x/sum(pdf_lin_weights) for x in pdf_lin_weights]

    pdf_lin_hist = plt.hist(pdf_lin, bins=bins_lin, weights=pdf_lin_weights, edgecolor='black', alpha=0.5, color='b')
    pdf_lin_hist = pdf_lin_hist[0]
    plt.title("PDF lin-lin"); plt.xlabel("degree"); plt.ylabel("pdf")

    # -------------------------------------------
    # PDF log-log scale
    ax = plt.subplot(122)
    pdf_log = np.log10(pdf_lin)
    # Check that np.log10 result is not equal to infinity
    if ~math.isinf(pdf_log[-1]):
        pdf_log = pdf_log[0:-1]
        pdf_lin_weights = pdf_lin_weights[0:-1]
    if len(pdf_log) > 0:
        bins_log = np.linspace(min(pdf_log), max(pdf_log), num=settings.bins_log_num, endpoint=True)
        pdf_log_hist = plt.hist(pdf_log, bins=bins_log, weights=pdf_lin_weights, align='left', edgecolor='black', alpha=0.5, color='b')
        pdf_log_hist = pdf_log_hist[0]

        if plot_slope:
            # Make linear regression to get slope
            regr_x = bins_log[0:-1]
            regr_y = pdf_log_hist
            # Stack values to use numpy.linalg
            A = np.vstack([regr_x, np.ones(len(regr_x))]).T
            # Simple linear regression using least-squares
            m, c = np.linalg.lstsq(A, regr_y)[0]
            # Plot slope
            plt.scatter(regr_x, regr_y, color='black')
            plt.scatter(regr_x, m*regr_x + c, color='blue')
            plt.plot(regr_x, m*regr_x + c, color='red', linewidth=3, label="Fitted line [m=" + str(m) + "]")
            plt.legend()

        # Change the Y axis to log and change the labels on X axis
        # ax.set_yscale('log')  # I removed the log axis to fit the linear regression line
        x_labels_log = ['{:.1f}'.format(x) for x in 10**(bins_log)]
        plt.xticks(bins_log, x_labels_log)
        plt.title("PDF log-log"); plt.xlabel("degree"); plt.ylabel("pdf")

    # ------------------------------------
    # Build the containing directory in case it doesn't exist
    output_file = output_path + '_deg_dist.png'
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    # Save the new created file
    plt.savefig(output_file)
    return None


def draw_network(G, file_name):
    # If not going to show or save simply return
    if not settings.show_figures and not settings.save_figures:
        return None
    # Otherwise keep going
    plt.figure()
    nx.draw_networkx(G, with_labels=True, node_size=300)
    # Save and show if TRUE
    if settings.save_figures:
        # Build output file path
        output_path = settings.output_plots + file_name + '.png'
        # Build the containing directory in case it doesn't exist
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        # Save the new created file
        plt.savefig(output_path)
    if settings.show_figures:
        plt.show()
    return None


def print_graph_properties(G):
    # some properties
    print("node degree clustering")
    for v in nx.nodes(G):
        print('%s %d %f' % (v, nx.degree(G, v), nx.clustering(G, v)))


def silent_remove(path, isDir):
    try:
        if(isDir):
            shutil.rmtree(path=path)
        else:
            os.remove(path=path)
    except OSError as e:  # this would be "except OSError, e:" before Python 2.6
        if e.errno != errno.ENOENT:  # errno.ENOENT = no such file or directory
            raise  # re-raise exception if a different error occurred
