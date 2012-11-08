#this script is pretty useless
#it takes a list of csv files (named for kegg pathways) with genes in those pathways
#in the csv files, and creates a new csv file where the kegg info is listed by gene
#(flipping the relationship from gene-by-kegg to kegg-by-gene)
#
#python kegg_info_flip.py [inputlist.csv] [outputfile.csv]

import sys, csv

def organize_kegg(input_list, output_csv):

	kegg_list = []

	kegg_dict = {}

	output = csv.writer(open(output_csv, 'wb'), delimiter='\t')

	for ath_kegg in csv.reader(open(input_list), delimiter='\t'):

		input_csv = str(ath_kegg[0]) + '.csv'

		for ath_gene in csv.reader(open(input_csv), delimiter='\t'):

			kegg_list_update = [ath_gene[0], ath_kegg[0]]
			kegg_list.append(kegg_list_update)

	for item in kegg_list:

		if item[0] in kegg_dict:
			kegg_update = str(kegg_dict[item[0]]) + " " + str(item[1])
			kegg_dict[item[0]] = kegg_update
		if item[0] not in kegg_dict:
			kegg_dict[item[0]] = item[1]

	for item in kegg_dict:
		output.writerow([item, kegg_dict[item]])



input_list = sys.argv[1]
output_file = sys.argv[2]

organize_kegg(input_list, output_file)


