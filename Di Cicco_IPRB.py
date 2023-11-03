'''
Rosalind IPRB exercise by Di Cicco Cecilia
'''
# Mendel's First Law

k = 28 # AA homozygous dominant individuals
m = 19 # Aa heterozygous individuals
n = 16 # aa homozygous recessive individuals
total = k + m + n # total number of individuals

# We want to calculate the probability that two randomly selected individuals will produce an offspring with a dominant allele
dom_k = 1   # by pairing an homoziguous dominant individual with any other individual the offspring will always have a dominant allele
dom_mm = 0.75 # by using the Punnett square --> Aa x Aa = Aa, Aa, Aa, aa
dom_mn = 0.5 # Aa x aa = Aa, Aa, aa, aa
dom_nn = 0 #aa x aa = aa, aa, aa, aa (no dominant allele is present)

# Probabilities calculus analyzing k with k,m,n
individual_k = k/total
kk = individual_k * (k - 1)/(total - 1) * dom_k
km = individual_k * m/(total - 1) * dom_k
kn = individual_k * n/(total - 1) * dom_k

# Probabilities calculus analyzing m with k,m,n
individual_m = m/total
mk = individual_m * k/(total - 1) * dom_k #k dominance over m
mm = individual_m * (m - 1)/(total - 1) * dom_mm
mn = individual_m * n/(total - 1) * dom_mn

# Probabilities calculus analyzing n with k,m,n
individual_n = n/total
nk = individual_n * k/(total - 1) * dom_k # k dominance over n
nm = individual_n * m/(total - 1) * dom_mn
nn = individual_n * (n - 1)/(total - 1) * dom_nn # no dominance between two n individuals

# Addition of all probabilities
total_probability = kk + km + kn + mk + mm + mn + nk + nm + nn
print(total_probability)