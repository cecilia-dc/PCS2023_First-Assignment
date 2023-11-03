'''
Rosalind TRAN exercise by Di Cicco Cecilia
'''
# Consensus and Profile

transitions = 0
transversions = 0

# Biopython
from Bio import SeqIO
file_path = 'rosalind_tran.txt'
sequences = list(SeqIO.parse(file_path, 'fasta'))

if len(sequences) != 2:
    print('The file does not contain two strings of DNA')
else:
    seq_1 = sequences[0]
    seq_2 = sequences [1]

    seq_id_1 = seq_1.id
    seq_id_2 = seq_2.id 
    seq_data1 = str(seq_1.seq)
    seq_data2 = str(seq_2.seq)
    sequence_1 = seq_data1
    sequence_2 = seq_data2

if len(sequence_1) != len(sequence_2):
    raise ValueError('To be compared, the two sequences must have the same lenght.')

nucleotide_properties = {'A': 'purine', 'G': 'purine', 'C': 'pyrimidine', 'T': 'pyrimidine', 'U': 'pyrimidine'}

for symbol1, symbol2 in zip(sequence_1, sequence_2):
    if nucleotide_properties[symbol1] == nucleotide_properties[symbol2]:
        if symbol1 != symbol2:
            transitions += 1
    else:
        transversions += 1

ratio = transitions/transversions
print(ratio)
        