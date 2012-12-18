import sys, csv

output_annotations = open('orthogene_annotations_purp.csv', 'w')

output_first_line = 'Orthogene.ID\tSeqName\tHit.Desc\tGO.Group\tGO.ID\tTerm\tFPKM_all\tFPKM_rel\tlength\n'

output_annotations.write(output_first_line)

for species in ['Purp']:

	short_long_dict = {}

	orthogene_dict = {}

	#build short_id to long_id dictionary

	short_long_dict_file = species + '_dictionary.csv'

	for (long_id, short_id) in csv.reader(open(short_long_dict_file), delimiter='\t'):

		short_long_dict.update({short_id:long_id})

	#build orthogene dictionary

	for (orthogene) in csv.reader(open('orthologs_by_rbh_complete_graph_purp.csv')):

		orthogene_dict[short_long_dict[orthogene[0]]] = orthogene

	#feed in annotations
	
	for (Species, SeqName, HitDesc, GOGroup, GOID, Term, FPKM_all, FPKM_rel, length) in csv.reader(open('all_gene_annotations.csv'), delimiter = '\t'):
	    
		if SeqName in orthogene_dict:

			output_line = orthogene_dict[SeqName][0] + '\t' + str(SeqName) + '\t' + str(HitDesc) + '\t' + str(GOGroup) + '\t' + str(GOID) + '\t' + str(Term) + '\t' + str(FPKM_all) + '\t' + str(FPKM_rel) + '\t' + str(length) + '\n'

			output_annotations.write(output_line)

output_annotations.close()
