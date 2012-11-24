#this script takes a query list of genes and the list of edges for graph generation
#(both in csv) and exports gml files for cytoscape
#the gml files are the entire network and the independent subgraphs
#query input is single-column csv
#edges input is double-column csv representing nodes connected by edges
#
#python split_coexp_network.py [query_list.csv] [network_edges.csv] [root_output_filename]

import sys, csv
import networkx as nx
import matplotlib.pyplot as plt

def subgraph_gml_maker(input_query, input_edges, output_file):

	query_list = []

	for entry in csv.reader(open(input_query), delimiter='\t'):
		query_list.append(str.upper(str(entry[0])))

	megalist = csv.reader(open(input_edges), delimiter = '\t')

	G = nx.Graph()
	G.add_edges_from(megalist)

	for node in G.nodes():
		if str.upper(str(node)) in query_list:
			G.node[node]['query']=1
		if str.upper(str(node)) not in query_list:
			G.node[node]['query']=0

	output_filename = output_file + "_whole_network.gml"

	nx.write_gml(G, output_filename)

	subgraphs = nx.connected_components(G)
	subgraph_number = 1

	for subgraph in subgraphs:

		current_subgraph = nx.Graph()
		current_subgraph.add_edges_from(G.edges(subgraph))

		current_node_number = current_subgraph.number_of_nodes()
		current_node_number = '%06d' % (current_node_number)
		current_subgraph_number = '%06d' % (subgraph_number)
		current_output_filename = output_file + "_" + str(current_node_number) + "_nodes_" + current_subgraph_number + ".gml"

		for node in current_subgraph.nodes():
			if str.upper(str(node)) in query_list:
				current_subgraph.node[node]['query']=1
			if str.upper(str(node)) not in query_list:
				current_subgraph.node[node]['query']=0

		for node in current_subgraph.nodes():
			if str.upper(str(node)) in query_list:
				nx.write_gml(current_subgraph, current_output_filename)

		subgraph_number += 1


def all_neighbors(graph, node):
    """ Returns all of the neighbors of a node in the graph.

    If the graph is directed returns predecessors as well as successors.

    Parameters
    ----------
    graph : NetworkX graph
        Graph to find neighbors.

    node : node
        The node whose neighbors will be returned.

    Returns
    -------
    neighbors : iterator
        Iterator of neighbors
    """
    if graph.is_directed():
        values = itertools.chain.from_iterable([graph.predecessors_iter(node),
                                                graph.successors_iter(node)])
    else:
        values = graph.neighbors_iter(node)

    return values


def subgraph_by_query_gml_maker(input_query, input_edges, output_file):

	query_list = []

	for entry in csv.reader(open(input_query), delimiter='\t'):
		query_list.append(str.upper(str(entry[0])))

	megalist = csv.reader(open(input_edges), delimiter = '\t')

	G = nx.Graph()
	G.add_edges_from(megalist)

	for node in G.nodes():
		if str.upper(str(node)) in query_list:
			G.node[node]['query']=1
		if str.upper(str(node)) not in query_list:
			G.node[node]['query']=0

	root_subgraph_nodes = []

	for root_node in query_list:
		if str.upper(str(root_node)) in G.nodes():
			for node1 in all_neighbors(G, root_node):
				for node2 in all_neighbors(G, node1):
					for node3 in all_neighbors(G, node2):
						for node4  in all_neighbors(G, node3):
							if node4 not in root_subgraph_nodes:
								root_subgraph_nodes.append(str.upper(str(node4)))

	H = G.subgraph(root_subgraph_nodes)

	subgraphs = nx.connected_components(H)
	subgraph_number = 1

	for subgraph in subgraphs:

		current_subgraph = nx.Graph()
		current_subgraph.add_edges_from(H.edges(subgraph))

		current_node_number = current_subgraph.number_of_nodes()
		current_node_number = '%06d' % (current_node_number)
		current_subgraph_number = '%06d' % (subgraph_number)
		current_output_filename = output_file + "_neighbors_" + str(current_node_number) + "_nodes_" + current_subgraph_number + ".gml"

		for node in current_subgraph.nodes():
			if str.upper(str(node)) in query_list:
				current_subgraph.node[node]['query']=1
			if str.upper(str(node)) not in query_list:
				current_subgraph.node[node]['query']=0

		for node in current_subgraph.nodes():
			if str.upper(str(node)) in query_list:
				nx.write_gml(current_subgraph, current_output_filename)

		subgraph_number += 1


input_query = sys.argv[1]
input_list = sys.argv[2]
output_file = sys.argv[3]

subgraph_gml_maker(input_query, input_list, output_file)
subgraph_by_query_gml_maker(input_query, input_list, output_file)







