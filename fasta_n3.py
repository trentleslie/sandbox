"""
BioPython Example File - Using FASTA nucleotide files

This is an example Python program to calculate GC percentages for
each gene in an nucleotide FASTA file - using the Biopython
SeqIO library.

It calculates GC percentages for each gene in a FASTA nucleotide file,
writing the output to a tab separated file for use in a spreadsheet.

It has been tested on BioPython 1.43 with Python 2.3, and is suitable
for Windows, Linux etc.

The suggested input file 'NC_005213.ffn' is available from the NCBI
from here:

ftp://ftp.ncbi.nlm.nih.gov/genomes/Bacteria/Nanoarchaeum_equitans/

See associated webpage:

http://www2.warwick.ac.uk/fac/sci/moac/currentstudents/peter_cock/python/fasta_n/

Peter Cock, MOAC, University of Warwick, UK
17 April 2007
"""

#Open a FASTA input file of gene nucleotides sequences:
input_file = open('NC_005213.ffn', 'r')

#Note - you might like to also download the complete
#genome nucleotide sequence, 'NC_005213.ffn' which is
#a single FASTA record.
#input_file = open('NC_005213.fna', 'r')

#Open an output file to record the counts in.
#tsv is short for "Tab Separated Variables",
#also known as "Tab Delimited Format".
#
#This is a universal format, you can read it
#with any text editor - Microsoft Excel is
#also a good choice.
output_file = open('nucleotide_counts.tsv','w')

#We will now write a header line to our output file.
#
#We must write \t to mean a tab, and \n to mean
#an end of line (new line) character.
#
#i.e.
#Gene (tab) A (tab) C (tab) G (tab) T (tab) Length (tab) CG%
output_file.write('Gene\tA\tC\tG\tT\tLength\tCG%\n')

#We are going to need BioPython's SeqIO library, so we
#must tell Python to load this ready for us:
from Bio import SeqIO

#Get SeqIO to read this file in "fasta" format,
#and use it to see each record in the file one-by-one
for cur_record in SeqIO.parse(input_file, "fasta") :
    #Because we used the Bio.SeqIO parser, each record
    #is SeqRecord object which includes name and seq
    #properties.
    gene_name = cur_record.name

    #Just like a string in python, a Biopython sequence
    #object has a 'count' method we can use:
    A_count = cur_record.seq.count('A')
    C_count = cur_record.seq.count('C')
    G_count = cur_record.seq.count('G')
    T_count = cur_record.seq.count('T')

    #We would also like to know the number of nucleotides
    #in this gene (which should add up to the four
    #base counts, if there are no unknown bases, N)
    length = len(cur_record.seq)

    #Now work out the CG percentage for this gene.
    #We must switch from integers into floating point
    #(non-integer) because integer division will
    #just give 0 or 1 as the answer
    cg_percentage = float(C_count + G_count) / length

    #Finally, we are going to save this information
    #as a single tab separated line in our output file.
    #
    #As before (when we wrote the header line), we must
    #write \t to mean a tab, and \n to mean an end of line
    #(new line) character.
    #
    #We are using the string formatting (or interpolation)
    # operator % so the %s means insert a string,
    #while %i means insert an integer and %f a floating
    #point (non-integer).
    #
    #The \ character means this command continues on the
    #next line
    output_line = '%s\t%i\t%i\t%i\t%i\t%i\t%f\n' % \
    (gene_name, A_count, C_count, G_count, T_count, length, cg_percentage)

    # 
    output_file.write(output_line)

#Now we have finished all the genes, we can close the output file:
output_file.close()

#and close the input file:
input_file.close()

#If you run this program and then open the output file
#'nucleotide_counts.tsv' in your spreadsheet
#(e.g. Microsoft Excel) you can do things like sort
#the genes by length of GC percentage.
#
#For example, you can see the GC% ranges from 22.8%
#up to 43.3% (to one decimal place) for 'NC_005213.ffn'
#
#You can also download the complete genome's nucleotide
#sequence, file 'NC_005213.fna'.
#
#If you run this program on that instead, you will get
#a single line output containing the data for the whole
#genome (genes and all the DNA inbetween).  The GC% for
#this is 31.6% (to one decimal place).
