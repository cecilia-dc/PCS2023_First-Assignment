'''
Rosalind CONS exercise by Di Cicco Cecilia
'''
# Consensus and Profile

# Biopython
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqUtils import nt_search

sequences = list(SeqIO.parse("rosalind_cons.txt", "fasta")) # Read the sequences from the FASTA file

sequence_strings = [str(seq.seq) for seq in sequences]  # Creating a list of sequences as strings

sequence_length = len(sequences[0])  # Determining the length of the sequences

profile = {'A': [0] * sequence_length, 'C': [0] * sequence_length, 'G': [0] * sequence_length, 'T': [0] * sequence_length}  # Dictionary to store the profile matrix

# Profile matrix
for i in range(sequence_length):
    column = "".join(sequence_strings)[i::sequence_length]
    for nucleotide in profile:
        profile[nucleotide][i] = column.count(nucleotide)

# Consensus sequence from the profile matrix
consensus = "".join([max(profile, key=lambda nucleotide: profile[nucleotide][i]) for i in range(sequence_length)])

print(consensus)

for nt in 'ACGT':
    print(f"{nt}: {' '.join(map(str, profile[nucleotide]))}")