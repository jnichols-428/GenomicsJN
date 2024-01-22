#!/usr/bin/env python3

""" 
nuc_count.py counts nucleotides in a fasta file

Usage: python3 nuc_count.py <fasta>

<fasta> = path to a fasta file
""" 

# Import modules
import sys

# sys.arg is a list containing 2 elements: the script name and 1 command line argument
# Check that all the command line argument was given. If not, print the documentation and exit.
if (len(sys.argv) != 2):
    sys.exit(__doc__) 

# Save the input arguments as variables
fasta = sys.argv[1]

# Initialize a nucleotide string
nucleotides = ""

# Load the fasta sequence
# NOTE: this script assumes there is only *one* sequence in the fasta file
# Open the fasta file
with open(fasta) as f:
    # For each line in the file
    for line in f:
        # Skip lines starting with ">"
        if not line.startswith(">"):
            # Add each line to the nucleotide string
            nucleotides += line.rstrip()

# Make the nucleotide string all capital letters 
nucleotides = nucleotides.upper()

# Count the nucleotides and print output
num_a = nucleotides.count('A')
num_c = nucleotides.count('C')
num_g = nucleotides.count('G')
num_t = nucleotides.count('T')
num_n = nucleotides.count('N')
length = nucleotides.count('A') +  nucleotides.count('C') + nucleotides.count('G') + nucleotides.count('T') + nucleotides.count('N')


print ("Raw Counts")
print ("A: ", num_a)
print ("C: ", num_c)
print ("G: ", num_g)
print ("T: ", num_t)
print ("N: ", num_n)
print ("Length: ", length)


## Part 3
### TODO Print out the frequencies for each nucleotide in alphabetical order
print ("NT Freq")
print ("A: ", num_a/length)
print ("C: ", num_c/length)
print ("G: ", num_g/length)
print ("T: ", num_t/length)
print ("N: ", num_n/length)


## Part 5
### TODO Use overlapping windows to count the dinucleotides. See the assignment for more information on overlapping windows.
### TODO Print the frequencies for each of dinucleotides in alphabetical order
# Count the nucleotides and print output
num_aa = nucleotides.count('AA')
num_ac = nucleotides.count('AC')
num_ag = nucleotides.count('AG')
num_at = nucleotides.count('AT')
num_ca = nucleotides.count('CA')
num_cc = nucleotides.count('CC')
num_cg = nucleotides.count('CG')
num_ct = nucleotides.count('CT')
num_ga = nucleotides.count('GA')
num_gc = nucleotides.count('GC')
num_gg = nucleotides.count('GG')
num_gt = nucleotides.count('GT')
num_ta = nucleotides.count('TA')
num_tc = nucleotides.count('TC')
num_tg = nucleotides.count('TG')
num_tt = nucleotides.count('TT')
num_dint = (nucleotides.count('A') +  nucleotides.count('C') + nucleotides.count('G') + nucleotides.count('T')) - 1 

print("DiNt Freq")
freq_aa = nucleotides.count('AA')/num_dint
freq_ac = nucleotides.count('AC')/num_dint
freq_ag = nucleotides.count('AG')/num_dint
freq_at = nucleotides.count('AT')/num_dint
freq_ca = nucleotides.count('CA')/num_dint
freq_cc = nucleotides.count('CC')/num_dint
freq_cg = nucleotides.count('CG')/num_dint
freq_ct = nucleotides.count('CT')/num_dint
freq_ga = nucleotides.count('GA')/num_dint
freq_gc = nucleotides.count('GC')/num_dint
freq_gg = nucleotides.count('GG')/num_dint
freq_gt = nucleotides.count('GT')/num_dint
freq_ta = nucleotides.count('TA')/num_dint
freq_tc = nucleotides.count('TC')/num_dint
freq_tg = nucleotides.count('TG')/num_dint
freq_tt = nucleotides.count('TT')/num_dint

print ("AA ", freq_aa)
print ("AC ", freq_ac)
print ("AG ", freq_ag)
print ("AT ", freq_at)
print ("CA ", freq_ca)
print ("CC ", freq_cc)
print ("CG ", freq_cg)
print ("CT ", freq_ct)
print ("GA ". freq_ga)
print ("GC ". freq_gc)
print ("GG ". freq_gg)
print ("GT ". freq_gt)
print ("TA ". freq_ta)
print ("TC ". freq_tc)
print ("TG ". freq_tg)
print ("TT ". freq_tt)












