#this script takes a list of desired sequence names and the reference
#fasta file to create a custom fasta file and raw primer3 input
#
#to run:
#python pull_at_from_html.py [input.html] [output.txt]
#txt]

import sys, csv, re

#custom fasta file from list
def scan_file(input_file, output_file):

	output_file_write = open(output_file,'w')

	for line in open(input_file):  

		regex = re.compile("AT\dG\d\d\d\d\d")
		regex_results = regex.findall(line)
		final_regex_results = list(set(regex_results))

		for item in final_regex_results:

			output_string = item + "\n"
			output_file_write.write(output_string)		

	output_file_write.close()

input_file = sys.argv[1]
output_file = sys.argv[2]

scan_file(input_file, output_file)
