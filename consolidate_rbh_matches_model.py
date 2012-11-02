import sys, csv

output1 = csv.writer(open('allspecies_matches_arabi.csv', 'wb'), delimiter='\t')

for species in ['Cocc', 'Hed', 'Indi', 'Lind', 'Lob', 'Nil', 'Pubes', 'Purp', 'Quamo']:
            
	filename = 'Arabi_' + species + '_matches.csv'
		    
	for (vertex1, vertex2) in csv.reader(open(filename), delimiter='\t'):
		    output1.writerow([vertex1, vertex2])

for (vertex1, vertex2) in csv.reader(open('allspecies_matches.csv'), delimiter='\t'):
	output1.writerow([vertex1, vertex2])
                

output2 = csv.writer(open('allspecies_matches_toma.csv', 'wb'), delimiter='\t')

for species in ['Cocc', 'Hed', 'Indi', 'Lind', 'Lob', 'Nil', 'Pubes', 'Purp', 'Quamo']:
            
	filename = 'Toma_' + species + '_matches.csv'
            
	for (vertex1, vertex2) in csv.reader(open(filename), delimiter='\t'):
            output2.writerow([vertex1, vertex2])

for (vertex1, vertex2) in csv.reader(open('allspecies_matches.csv'), delimiter='\t'):
	output2.writerow([vertex1, vertex2])
   
