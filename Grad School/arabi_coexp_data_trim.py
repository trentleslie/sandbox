import sys, os, csv

def coex_trim(output_csv):

	MR_cutoff = 30

	dirList=os.listdir(os.getcwd())

	final_match_list = []

	filecount = 0
	per_done = 0

	print "Trimming is %i percent done." %per_done

	for filename in dirList:

		if os.stat(filename)[6]!=0:

			match_list=[]

			for line in open(filename):
				current_entry=[filename, str.rsplit(line)[0], float(str.rsplit(line)[1]), float(str.rsplit(line)[2])]
				match_list.append(current_entry)

			MR_max = float(max(match_list, key=lambda x: x[2])[2])

			for item in match_list:
				if item[2]<MR_cutoff or item[2]>MR_max-MR_cutoff:
					final_match_list.append(item)

		filecount+=1
		if int((float(filecount)/float(len(dirList)))*100)>per_done:
			per_done = int((float(filecount)/float(len(dirList)))*100)
			print "Trimming is %i percent done." %per_done

	output = csv.writer(open(output_csv, 'wb'), delimiter='\t')

	for line in final_match_list:
		output.writerow(line)


output_file = sys.argv[1]
coex_trim(output_file)

