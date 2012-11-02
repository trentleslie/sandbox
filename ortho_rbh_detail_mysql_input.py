import sys, csv
import networkx as nx
import matplotlib.pyplot as plt

megalist = csv.reader(open('allspecies_matches.csv'), delimiter = '\t')

G = nx.Graph()
G.add_edges_from(megalist)

subgraphs = nx.connected_components(G)

output_file = open('subgraphs_detail_input_mysql.txt','w')

subgraph_number = 1

for subgraph in subgraphs:
	
	current_subgraph = nx.Graph()

	current_subgraph.add_edges_from(G.edges(subgraph))

	current_subgraph_number = 'Ipo' + '%06d' % (subgraph_number)

	for node in list(current_subgraph.nodes()):

		output_line = 'INSERT INTO BioSequence_has_Ortholog_RBH (BioSequence_Short_ID, Ortholog_RBH_Ortho_ID)\nVALUES (\"%s\", \"%s\");\n' % (node, current_subgraph_number)
		output_file.write(output_line)

	subgraph_number += 1


megalist = csv.reader(open('allspecies_matches_arabi.csv'), delimiter = '\t')

G = nx.Graph()
G.add_edges_from(megalist)

subgraphs = nx.connected_components(G)

subgraph_number = 1

for subgraph in subgraphs:
	
	current_subgraph = nx.Graph()

	current_subgraph.add_edges_from(G.edges(subgraph))

	current_subgraph_number = 'IpoAr' + '%06d' % (subgraph_number)

	for node in list(current_subgraph.nodes()):

		output_line = 'INSERT INTO BioSequence_has_Ortholog_RBH (BioSequence_Short_ID, Ortholog_RBH_Ortho_ID)\nVALUES (\"%s\", \"%s\");\n' % (node, current_subgraph_number)
		output_file.write(output_line)

	subgraph_number += 1



megalist = csv.reader(open('allspecies_matches_toma.csv'), delimiter = '\t')

G = nx.Graph()
G.add_edges_from(megalist)

subgraphs = nx.connected_components(G)

subgraph_number = 1

for subgraph in subgraphs:
	
	current_subgraph = nx.Graph()

	current_subgraph.add_edges_from(G.edges(subgraph))

	current_subgraph_number = 'IpoTo' + '%06d' % (subgraph_number)

	for node in list(current_subgraph.nodes()):

		output_line = 'INSERT INTO BioSequence_has_Ortholog_RBH (BioSequence_Short_ID, Ortholog_RBH_Ortho_ID)\nVALUES (\"%s\", \"%s\");\n' % (node, current_subgraph_number)
		output_file.write(output_line)

	subgraph_number += 1


output_file.close() 

