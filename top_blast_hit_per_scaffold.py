#this script takes raw blast output (blastall -m 8) with multiple blast hits per
#query and reduces it to the top evalue blast hit per query
#
#python top_blast_hit_per_scaffold.py [rawblastinput.csv] [tophitblastoutput.csv]

import sys, csv

def topblasthit(inputcsv, outputcsv):

	outdict = {}

	hitcount = 0

	output = csv.writer(open(outputcsv, 'wb'), delimiter='\t')

	for (Query_id, Subject_id, percent_identity, alignment_length, mismatches, gap_openings, q_start, q_end, s_start, s_end, e_value, bit_score) in csv.reader(open(inputcsv), delimiter='\t'):

		Subject_id = Subject_id[:9]

		current_list = []
		current_list.append(Subject_id)
		current_list.append(percent_identity)
		current_list.append(alignment_length)
		current_list.append(mismatches)
		current_list.append(gap_openings)
		current_list.append(q_start)
		current_list.append(q_end)
		current_list.append(s_start)
		current_list.append(s_end)
		current_list.append(e_value)
		current_list.append(bit_score)

		if Query_id in outdict:
			if Subject_id not in outdict[Query_id][0] and float(e_value) == float(outdict[Query_id][9]):
					outdict[Query_id][0] = outdict[Query_id][0] + " " + Subject_id
					hitcount+=1
			if float(e_value) < float(outdict[Query_id][9]):
				outdict[Query_id]=current_list
		else:
			outdict.update({Query_id:current_list})
			hitcount+=1

	print "There are " + str(hitcount) + " top blast hit genes."

	for item in outdict:
		Subject_id = outdict[item][0]
		percent_identity = outdict[item][1]
		alignment_length = outdict[item][2]
		mismatches = outdict[item][3]
		gap_openings = outdict[item][4]
		q_start = outdict[item][5]
		q_end = outdict[item][6]
		s_start = outdict[item][7]
		s_end = outdict[item][8]
		e_value = outdict[item][9]
		bit_score = outdict[item][10]
		output.writerow([item, Subject_id, percent_identity, alignment_length, mismatches, gap_openings, q_start, q_end, s_start, s_end, e_value, bit_score])


input_file = sys.argv[1]
output_file = sys.argv[2]

topblasthit(input_file, output_file)
