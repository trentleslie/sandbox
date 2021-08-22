import sys, csv

for species1 in ['Arabi', 'Toma']:

	dictionary1 = species1 + '_dictionary.csv'

	species1dict = {}

	for (long_id, short_id) in csv.reader(open(dictionary1), delimiter='\t'):
        
		species1dict.update({long_id:short_id})
		
	for species2 in ['Cocc', 'Hed', 'Indi', 'Lind', 'Lob', 'Nil', 'Pubes', 'Purp', 'Quamo']:
            
		dictionary2 = species2 + '_dictionary.csv'

		species2dict = {}

		for (long_id, short_id) in csv.reader(open(dictionary2), delimiter='\t'):
        
			species2dict.update({long_id:short_id})

		filename1 = species1 + '_to_' + species2 + '.csv'
		filename2 = species2 + '_to_' + species1 + '.csv'

		unmatched_keys1 = open(species1 + '_' + species2 + 'key_errors.csv', 'w')
		output_file1 = open(species1 + '_to_' + species2 + '_fixed.csv', 'w')
	    
	    	for (Query_id, Subject_id, percent_identity, alignment_length, mismatches, gap_openings, q_start, q_end, s_start, s_end, e_value, bit_score) in csv.reader(open(filename1), delimiter='\t'):

			if Query_id in species1dict and Subject_id in species2dict:		

				output_line = '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n' % (species1dict[Query_id], species2dict[Subject_id], percent_identity, alignment_length, mismatches, gap_openings, q_start, q_end, s_start, s_end, e_value, bit_score)
		
				output_file1.write(output_line) 
			else:
				output_line = Query_id + '\t' + Subject_id + '\n'

				unmatched_keys1.write(output_line)
		
		unmatched_keys1.close()
	    	output_file1.close()  

		unmatched_keys2 = open(species2 + '_' + species1 + 'key_errors.csv', 'w')
		output_file2 = open(species2 + '_to_' + species1 + '_fixed.csv','w')
	    
	    	for (Query_id, Subject_id, percent_identity, alignment_length, mismatches, gap_openings, q_start, q_end, s_start, s_end, e_value, bit_score) in csv.reader(open(filename2), delimiter='\t'):
		
			if Query_id in species2dict and Subject_id in species1dict:		

				output_line = '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n' % (species2dict[Query_id], species1dict[Subject_id], percent_identity, alignment_length, mismatches, gap_openings, q_start, q_end, s_start, s_end, e_value, bit_score)
		
				output_file2.write(output_line) 

			else:
				output_line = Query_id + '\t' + Subject_id + '\n'

				unmatched_keys2.write(output_line)

		
		unmatched_keys2.close()
	    	output_file2.close()    

