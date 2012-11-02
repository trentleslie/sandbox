import sys, csv

# number below which to discard results
E_CUTOFF = 1e-3

def load_csv_to_dict(filename):
    """
    Load the CSV file into a dictionary, tying query sequences to subject
    sequences.
    """
    d = {}

    current_query_name, best_expect = None, None
    matches = []
    
    for (query_name, subject_name, expect, score) in csv.reader(open(filename), delimiter='\t'):
        # fix the names that start with a 'gi|XXXXXXX|'
        query_name = demangle_name(query_name)
        subject_name = demangle_name(subject_name)

        # convert the e-value into a floating point number
        expect = float(expect)
        
        #if the current query_name matches the prior one and if the current query's
        #e-value is equal to the prior query's e-value and less than the cutoff,
        #append the subject name to the matches list.
        #As long as the query_name stays the same, the for loop will continue and
        #this conditional statement will continue to add matches of equal (i.e. best)
        #e-value until the query_name no longer matches, where it goes to the else and
        #attaches the matches list to the query_name's dictionary entry
        if query_name == current_query_name:
            if expect == best_expect and expect < E_CUTOFF:
                matches.append(subject_name)
        #if the current query_name is different than the prior one, then do this stuff
        else:
            # new query ==> store matches, reset
            #if the matches list exists now, attach the matches to the current query_name
            #in the d dictionary
            if matches:
                d[current_query_name] = matches

            # store the new match?
            #empty matches list
            matches = []
            #if the current query_name's e-value makes the cutoff, append the subject name
            #to the matches list
            if expect < E_CUTOFF:
                matches.append(subject_name)

            #update current_query_name and best_expect to this iteration's values
            current_query_name, best_expect = query_name, expect
            
    if matches:
        d[current_query_name] = matches

    return d

def demangle_name(name):
    """
    This functions strips off the 'gi|XXXXX|' name encoding that NCBI uses.

    Note that NCBI does this automatically for subject sequences.
    """
    if name.startswith('gi|'):
        name = name.split('|')
        name = name[2:]
        name = "|".join(name)

    return name

###

def csv_trim(filename, species1, species2):
    
    output_file = open(species1 + '_to_' + species2 + '_rbh.csv','w')
    
    for (Query_id, Subject_id, percent_identity, alignment_length, mismatches, gap_openings, q_start, q_end, s_start, s_end, e_value, bit_score) in csv.reader(open(filename), delimiter='\t'):
        
        output_line = '%s\t%s\t%s\t%s\n' % (Query_id, Subject_id, e_value, bit_score)
        
        output_file.write(output_line) 
        
    output_file.close()    

# This is the code that's run when you actually type 'find-reciprocal.py'
# at the command line; the above are function definitions, that define
# reusable blocks or chunks of code.
    
def rbh_test(filename1, filename2, species1, species2):
    
    d1 = load_csv_to_dict(filename1)
    d2 = load_csv_to_dict(filename2)

    output = csv.writer(open(species1 + '_' + species2 + '_matches.csv', 'wb'), delimiter='\t')

    for name in d1:      #goes through first column in first csv file one row at a time
                      #d1[name] calls the "definition" of the name to create a list of the putative orthologs
        matches = d1[name]                  # 'matches' is a list
        for name2 in matches:   #this begins the nested loop for the matches (name2)
            matches2 = d2.get(name2)  #for whatever reason, they used the get method to use the dictionary instead of brackets as in the out loop - they both return equivalent values
            #this conditional statement confirms the list is not empty and, if it's not, tests if the current scaffold in d1 is the reciprocal best hit
            if matches2 and name in matches2: # so is 'matches2'
                output.writerow([name, name2])
    
for species1 in ['Cocc', 'Hed', 'Indi', 'Lind', 'Lob', 'Nil', 'Pubes', 'Purp', 'Quamo']:
    for species2 in ['Cocc', 'Hed', 'Indi', 'Lind', 'Lob', 'Nil', 'Pubes', 'Purp', 'Quamo']:
        if ['Cocc', 'Hed', 'Indi', 'Lind', 'Lob', 'Nil', 'Pubes', 'Purp', 'Quamo'].index(species2) > ['Cocc', 'Hed', 'Indi', 'Lind', 'Lob', 'Nil', 'Pubes', 'Purp', 'Quamo'].index(species1):
            
            filename1 = species1 + '_to_' + species2 + '.csv'
            filename2 = species2 + '_to_' + species1 + '.csv'
            
            csv_trim(filename1, species1, species2)
            csv_trim(filename2, species2, species1)
            
            rbhfilename1 = species1 + '_to_' + species2 + '_rbh.csv'
            rbhfilename2 = species2 + '_to_' + species1 + '_rbh.csv'
            
            rbh_test(rbhfilename1, rbhfilename2, species1, species2)
            
        
                    
