import sys, csv

output = csv.writer(open('allspecies_matches.csv', 'wb'), delimiter='\t')

for species1 in ['Cocc', 'Hed', 'Indica', 'Lind', 'Lob', 'Nil', 'Pubes', 'Purp', 'Quamo']:
    for species2 in ['Cocc', 'Hed', 'Indica', 'Lind', 'Lob', 'Nil', 'Pubes', 'Purp', 'Quamo']:
        if ['Cocc', 'Hed', 'Indica', 'Lind', 'Lob', 'Nil', 'Pubes', 'Purp', 'Quamo'].index(species2) > ['Cocc', 'Hed', 'Indica', 'Lind', 'Lob', 'Nil', 'Pubes', 'Purp', 'Quamo'].index(species1):
            
            filename = species1 + '_' + species2 + '_matches.csv'
            
            for (vertex1, vertex2) in csv.reader(open(filename), delimiter='\t'):
                output.writerow([vertex1, vertex2])
                
                
           