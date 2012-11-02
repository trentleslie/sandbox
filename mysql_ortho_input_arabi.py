import sys, csv
import networkx as nx
import matplotlib.pyplot as plt

megalist = csv.reader(open('allspecies_matches_arabi.csv'), delimiter = '\t')

G = nx.Graph()
G.add_edges_from(megalist)

subgraphs = nx.connected_components(G)
subgraph_number = 1

track_clustering_avg = []

output_file = open('subgraphs_info_arabi_mysql.txt','w')

for subgraph in subgraphs:
	species_trunc = []
	for row in G.edges(subgraph):
		for item in row:
			species_trunc.append(item[:3])
	number_of_species = len(set(species_trunc))

	current_subgraph = nx.Graph()

	current_subgraph.add_edges_from(G.edges(subgraph))

	current_subgraph_number = 'IpoAr' + '%06d' % (subgraph_number)

        output_line = 'INSERT INTO Ortholog_RBH (Ortho_ID, Number_of_Nodes, Number_of_Species, Diameter, Average_Clustering, Model_Organism, Ortho_Edges, Ortho_Set)\nVALUES (\"\
%s\", %i, %i, %i, %f, \"Arabidopsis\", \"%s\", \"%s\");\n' % (current_subgraph_number, nx.number_of_nodes(current_subgraph), number_of_species, nx.diameter(current_subgraph), nx.average_clustering(current_subgraph), str(list(current_subgraph.edges())), str(list(current_subgraph.nodes())))

	output_file.write(output_line)

	subgraph_number += 1

output_file.close() 

