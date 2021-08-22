import sys, csv

#Expression and Blast data for Cocc and Hed

output_unmatched_dict = open('unmatched_short_med_dict_keys-no_EXP_data.txt', 'w')

output_unmatched_counts_dict = open('unmatched_med_short_dict_keys-RPKM_not_tied_to_short_or_long_id.txt', 'w')

output_shortid_counts = open('shortid_counts_all.csv', 'w')

for species in ['Cocc', 'Hed', 'Indi', 'Lind', 'Lob', 'Nil', 'Pubes', 'Purp']:

	short_long_dict = {}

	long_med_dict = {}

	short_med_dict = {}

	med_short_dict = {}

	short_counts_dict = {}

	#build short_id to long_id dictionary

	short_long_dict_file = species + '_dictionary.csv'

	for (long_id, short_id) in csv.reader(open(short_long_dict_file), delimiter='\t'):

		short_long_dict.update({short_id:long_id})

	#build long_id to med_id dictionary

	long_med_dict_file = species + '_EXP.csv'
	
	for (GO, Type, Term, BlastHit, Seq, Length, Score, eValue, Seq2, EXP_CAT) in csv.reader(open(long_med_dict_file)):
	    
		long_med_dict.update({Seq:Seq2})

	#build med_id to short_id (and vice versa) dictionaries and output those that don't have EXP data

	for value in short_long_dict:
		if short_long_dict[value] in long_med_dict:
			short_med_dict.update({value: long_med_dict[short_long_dict[value]]})
			med_short_dict.update({long_med_dict[short_long_dict[value]]:value})
		else:
			output_unmatched_dict_line = short_long_dict[value] + "\n"
			output_unmatched_dict.write(output_unmatched_dict_line)

	#UPDATE input for ipobase RPKM info

	RPKM_file = species + '_RPKM.csv'

	for (RPKM, new_seqname, length, Count) in csv.reader(open(RPKM_file), delimiter=','):
		if new_seqname in med_short_dict:
			output_line_counts = str(Count) + "," + str(med_short_dict[new_seqname]) + "\n"
			output_shortid_counts.write(output_line_counts)
		else:
			output_unmatched_counts_dict_line = new_seqname + "\n"
			output_unmatched_counts_dict.write(output_unmatched_counts_dict_line)

output_shortid_counts.close()

output_unmatched_dict.close()

output_unmatched_counts_dict.close()
