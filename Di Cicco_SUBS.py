'''
Rosalind SUBS exercise by Di Cicco Cecilia
'''
# Finding a Motif in DNA

# s is the string of DNA and t is it's substring
s = "TGCCAGGTGCCAGGCTGCCAGGGAGTGCCAGGATTGCCAGGTGCCAGGTCACTGCCAGGTTACCTTCAAATGCCAGGTGCCAGGTGCCAGGTAGACTGCCAGGTGCCAGGTTGCCAGGAGACCGTGCCAGGTTGCCAGGCATCGCATGCCAGGTTGCCAGGGTACTGCCAGGTGTGCCAGGTTGCCAGGTTTGCCAGGTTTGCCAGGCCTGCCAGGTGCCAGGTGCCAGGGATTGCCAGGGTGCCAGGTTGCCAGGTTTGCCAGGATATTGCCAGGCCGGTGAATGCCAGGATTTTTGCCAGGTTGATGCCAGGTGCCAGGTTTTGCCAGGTTGCCAGGTGCCAGGGGGTAGTGGCGTGCCAGGTGGTGCCAGGTATGCCAGGCTGGTGCCAGGTGCCAGGTGCCAGGTGCCAGGATGGTGCCAGGCGCTTGCCAGGCTGCCAGGTGCCAGGTGCCAGGTTCAGTAGCCTATGCCAGGGGACTGCCAGGTGCCAGGTGCCAGGATGCCAGGCCTGGCATGCCAGGTTTGCCAGGGGCTGCCAGGGGAACTGCCTGCCAGGGAAGATGCCAGGGCATGCCAGGCCACAGATGCCAGGTGCCAGGATGCCAGGACTTTGGCTCTTTGCCAGGACTGCCAGGGTGTGCCAGGGTGCCAGGTAACTGCCAGGTGGTGGCGAATGCCAGGGCTGCCAGGGCTGCCAGGCTGCCAGGGCTTGCCAGGCACTGCCAGGGAGTGCCAGGGCCAACGCCTGCCAGGTGCCAGGATGCCAGGGGTACCTCCACTATGCCAGGTCTGCCAGGTGCCAGGCGTAATGCCAGGTAGACTGCAGGTGCCAGGCTGCCAGGTGCCAGGTTGTTGCCAGGTCTGTGGCATGCCAGGTGCCAGGATTGCCAGGTGCCAGGATGCCAGGTGCCAGGTGCCAGGGGGGTGCCAGGATGCCAGG" 
t = 'TGCCAGGTG'  

def find_substring_positions(s, t): 
    positions = []
    for i in range(len(s) - len(t) + 1):
        if s[i:i + len(t)] == t:
            positions.append(i + 1)  # 1-based index
    return positions

positions = find_substring_positions(s, t)
print(" ".join(map(str, positions)))
