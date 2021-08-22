from Bio import SeqIO

for species in ['Cocc', 'Hed', 'Indica', 'Lind', 'Lob', 'Nil', 'Pubes', 'Purp', 'Quamo']:
  
    #Open a FASTA input file of gene nucleotides sequences:
    input_file = open(species + '.fasta', 'r')
    
    output_file = open(species + '_dictionary.csv','w')
    
    fasta_file = open(species + '_12.fasta', 'w')
    
    gene_number = 1
    
    #Get SeqIO to read this file in "fasta" format,
    #and use it to see each record in the file one-by-one
    for cur_record in SeqIO.parse(input_file, "fasta") :
        #Because we used the Bio.SeqIO parser, each record
        #is SeqRecord object which includes name and seq
        #properties.
        gene_name = cur_record.name
        
        new_gene_name = species + "%06d" % (gene_number,)
    
        output_line = '%s\t%s\n' % (gene_name, new_gene_name)
        
        output_file.write(output_line)
        
        fasta_line = '>' + new_gene_name + '\n' + str(cur_record.seq) + '\n'
        
        fasta_file.write(fasta_line)
        
        gene_number += 1
    
    #Now we have finished all the genes, we can close the output file:
    output_file.close()
    
    fasta_file.close()
    
    #and close the input file:
    input_file.close()
    
