'''
Rosalind GC exercise by Di Cicco Cecilia
'''
# Computing GC content

from Bio import SeqIO  # importing FASTA record with multiple sequences

def calculate_gc_content(sequence):
    gc_count = sequence.count('C') + sequence.count('G') # counting the number of GC-bases by counting C's and G's in the sequence
    total_bases = len(sequence)
    gc_percentage = gc_count/total_bases * 100 # the percentage of GC-content is given by the number of GC bases whe counted divided by the total number of bases (ATGC) * 100
    if total_bases > 0:
        return gc_percentage
    else:
        return 0


def find_sequence_with_highest_gc_content(records):
    max_gc_content = 0 # the GC content is a number
    max_gc_sequence_id = "" # id of a sequence is a string

    for record in records:
        gc_content = calculate_gc_content(record.seq)
        if gc_content > max_gc_content:
            max_gc_content = gc_content
            max_gc_sequence_id = record.id

    return max_gc_sequence_id, max_gc_content

fasta_file = "rosalind_gc.txt"

records = list(SeqIO.parse(fasta_file, "fasta"))
max_gc_sequence_id, max_gc_content = find_sequence_with_highest_gc_content(records)

print(max_gc_sequence_id) # gives the id of the sequence with the maximum GC-content
print(f"{max_gc_content:.6f}%") # gives the percentage of GC bases of the sequence identified