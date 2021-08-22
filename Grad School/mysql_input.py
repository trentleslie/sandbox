from Bio import SeqIO

for species in ['Cocc', 'Hed', 'Indica', 'Lind', 'Lob', 'Nil', 'Pubes', 'Purp', 'Quamo', 'Arabi', 'Toma']:
  
    #Open a FASTA input file of gene nucleotides sequences:
    input_file = open(species + '.fasta', 'r')
    
    output_file = open(species + '_mysql_input.txt','w')
  
    gene_number = 1
    
    #Get SeqIO to read this file in "fasta" format,
    #and use it to see each record in the file one-by-one
    for cur_record in SeqIO.parse(input_file, "fasta") :
        #Because we used the Bio.SeqIO parser, each record
        #is SeqRecord object which includes name and seq
        #properties.
        gene_name = cur_record.name
        
        new_gene_name = species + "%06d" % (gene_number,)
    
        output_line = 'INSERT INTO BioSequence (Short_ID, Long_ID, Sequence, Seq_Type, Seq_Length, Species_ID)\nVALUES (\"%s\", \"%s\", \"%s\", \"cDNA\", %i, \"%s\");\n' % (new_gene_name, gene_name, str(cur_record.seq), len(str(cur_record.seq)), species)
        
        output_file.write(output_line)
        
        gene_number += 1
    
    #Now we have finished all the genes, we can close the output file:
    output_file.close()
     
    #and close the input file:
    input_file.close()
    
