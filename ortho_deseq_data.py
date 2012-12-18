import sys, csv

output_unmatched_dict = open('unmatched_shortid_counts_no_count_data_for_these_shortids.txt', 'w')

output_deseq_counts = open('counts_for_deseq.csv', 'w')

#['Cocc', 'Hed', 'Indi', 'Lind', 'Lob', 'Nil', 'Pubes', 'Purp']:

short_counts_dict = {}

ortho_short_dict = {}

#build short_id to counts dictionary

for (counts, short_id) in csv.reader(open("shortid_counts_all.csv")):

	short_counts_dict.update({short_id:counts})

#build ortho to short_id dictionary
	
for (OrthoID, Number_of_Nodes, Number_of_Cliques, Gene_List) in csv.reader(open("orthologs.csv"), delimiter="\t"):
	    
	ortho_short_dict.update({OrthoID:Gene_List.split(",")})

#build ortho to short_id:counts dictionary and output those orhtologs that don't have complete count data

ortho_short_counts_dict = {}

for ortho in ortho_short_dict:
	orthogene_dict = []
	orthogenes = sorted(ortho_short_dict[ortho])
	for orthogene in orthogenes:
		if orthogene in short_counts_dict:
			orthogene_dict_entry = short_counts_dict[orthogene]
			orthogene_dict.append(orthogene_dict_entry)
		else:
			output_unmatched_dict_line = ortho + "," + orthogene + "\n"
			output_unmatched_dict.write(output_unmatched_dict_line)
	if len(orthogene_dict)==8:
		ortho_short_counts_dict[ortho] = orthogene_dict

for item in ortho_short_counts_dict:
	output_deseq_counts_line = item + "," + str(ortho_short_counts_dict[item]) + "\n"
	output_deseq_counts.write(output_deseq_counts_line)

output_deseq_counts.close()

output_unmatched_dict.close()
