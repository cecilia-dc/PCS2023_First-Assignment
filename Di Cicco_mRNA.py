'''
Rosalind mRNA exercise by Di Cicco Cecilia
'''
# Inferring mRNA from Protein 

# Codon table
rna_codon_table = {
    "F": 2, "L": 6, "I": 3, "M": 1, "V": 4, "S": 6, "P": 4, "T": 4, "A": 4, "Y": 2, "H": 2, "Q": 2, "N": 2, "K": 2,
    "D": 2, "E": 2, "C": 2, "W": 1, "R": 6, "G": 4, "Stop": 3
}

# Calculate the total possible RNA strings
def rna_possibilities_calculus(protein_seq, codon_table):
    possibilities = 1  # Initialize the count to 1 for the stop codon
    for symbol in protein_seq:
        if symbol not in codon_table:
            raise ValueError(f'Unknown amino acid symbol: {symbol}')
        possibilities = (possibilities * codon_table[symbol]) % 1000000
        
        # Since there is one stop codon, multiply by the number of ways to generate a stop codon
    possibilities = (possibilities * codon_table["Stop"]) % 1000000
    return possibilities

protein_seq = 'MFHVDWTTCPDAEEVNITRTAANKMNEDTYFIQQTASRPIPRAQMWDGLAGSEKTWSVLFLRNTFHMAFNDMFKKPDNTDMMPEADAHLAFLFYNPFGYDSNKTISLPLRHHIHRMAVDREGLEKTQIPYVKHDKDACHFYLVVYALIKKCQECFQLHPPAQVMVLMSPETRKCVLRQIERLDVTDTHCYCCSRSQTYQKVHDEYSTGKYDLMSMERDVGAVPRSYIVTYRWIHWADFVVKPTFQVQWIVTIYDGERLFDKHRDDAPSDKSHVGHESQHYEHAMWADMISGAWYFSPYNFVAAGSAQNLDETMMAAYGFRQDDWYRWAVDEKEQKQKFRDCDHMFEYQLGVDRSGHNIPKVRTSWIDEAGFYKMWCGPFDDQWSDPECMKPQSWWRQPMDISWSASLYPPGQEDNMQFVDKYADVSMDENTGYAKDLVNPIRHFNHAFDSFQEGPLYLANPGCHCNKDVVEFCGWETCHRMREPSNSWWCSFHKCMQQFQQYFEAFDSKNFFPMFAPSRTPESAVIPWGTNDKKCTEDQPASTMDKSFDADSKSNTEAQWHDKPNLPNKGMSVQAGDIGLFNNYLKTVRVTYVQCKMGLRIPKYIPMPFGAVWKTKKMPHPETKNIKNECSTFTNCKCTNICEYSTYKSMANNSYFMSSMECAHYESYQVEPKGSDINTPSPFALWHWPYTDWEEDPLQKDNVGSHVRAWSYYYNSVCDFCCSEIVRFAIAKAVIGSRGCYYCNQPYDCAVTFIHCWMVTAWYVWYYDRRHHCFVFLACMPPAYTWLQYALWIKAMIVGYKIISYLIQTCIWMCSMMKPYDQVGPMRLILVIEADSEGWYETCAVPRQRIGLNPDVFSMRTIHMACIGIHTWGYEPEPHMFFDHESWYLQCYRYPKKGIYWVQDLMGIQGTQMLYPSHMSVLAAGARFSCMTGTNYLHFDVTDHGWGWFLYYKAKFYKLWWDICGGPPHFNVLSEDYCQLIGPMFIWEKMDCFKRYYG'

rna_possibilities = rna_possibilities_calculus(protein_seq, rna_codon_table)
print(rna_possibilities)