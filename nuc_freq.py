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

