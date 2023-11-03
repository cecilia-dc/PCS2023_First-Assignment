'''
Rosalind LCSM exercise by Di Cicco Cecilia
'''
# Finding a Shared Motif

# Biopython
from Bio import SeqIO # importing FASTA record with multiple sequences
sequences = list(SeqIO.parse("rosalind_lcsm.txt", "fasta"))

# Defining a function that finds the longest common substring
def longest_common_substring(strings):
    shortest_string = min(strings, key=len)
    max_length = len(shortest_string)
    
    for length in range(max_length, 0, -1):
        for start in range(max_length - length + 1):
            substring = shortest_string[start:start + length]
            if all(substring in s for s in strings):
                return substring
            
common_substring = longest_common_substring([str(seq.seq) for seq in sequences])
print(common_substring)