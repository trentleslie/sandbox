import sys, csv
import networkx as nx
import matplotlib.pyplot as plt

megalist = csv.reader(open('allspecies_matches_toma.csv'), delimiter = '\t')

G = nx.Graph()
G.add_edges_from(megalist)

subgraphs = nx.connected_components(G)
subgraph_number = 1

track_clustering_avg = []

output_file = open('subgraphs_info_toma.csv','w')

output_file.write('Orthoset_ID\tNumber_of_Nodes\tNumber_of_Species\tDiameter\tAvg_Clustering\tModel_Organism\tEdges\tNodes\n')

for subgraph in subgraphs:
	species_trunc = []
	for row in G.edges(subgraph):
		for item in row:
			species_trunc.append(item[:3])
	number_of_species = len(set(species_trunc))

	current_subgraph = nx.Graph()

	current_subgraph.add_edges_from(G.edges(subgraph))

	current_subgraph_number = 'IpoTo' + '%06d' % (subgraph_number)

	output_line = current_subgraph_number + '\t' + str(nx.number_of_nodes(current_subgraph)) + '\t' + str(number_of_species) + '\t' + str(nx.diameter(current_subgraph)) + '\t' + str(nx.average_clustering(current_subgraph)) + '\tTomato\t' + str(list(current_subgraph.edges()))+ '\t' + str(list(current_subgraph.nodes())) + '\n'

	output_file.write(output_line)

	current_clust_avg_list = [str(nx.average_clustering(current_subgraph))[:4]]
	current_clust_avg_string = str(nx.average_clustering(current_subgraph))[:4]
	current_clust_avg_float = nx.average_clustering(current_subgraph)

	if number_of_species==9 and nx.average_clustering(current_subgraph)<1 and nx.number_of_nodes(current_subgraph)<50:
		if len(set(track_clustering_avg) & set(current_clust_avg_list))<1:
			nx.draw(current_subgraph)
			pic_name = 'C' + str(current_clust_avg_string) + current_subgraph_number + '.png'
			plt.savefig(pic_name)
			plt.clf()
			track_clustering_avg.append(str(current_clust_avg_string))

	subgraph_number += 1

output_file.close() 

