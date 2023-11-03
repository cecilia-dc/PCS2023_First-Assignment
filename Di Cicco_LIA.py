'''
Rosalind LIA exercise by Di Cicco Cecilia
'''
# Indipendent Alleles

# input values for k and N
k = 6
N = 16

def prob_calculus(k, N):
    generation = [0] * (k + 1) # list to store the number of Aa and Bb individuals along each generation

    generation[0] = 1  # we start with generation 0 at  which we have an Aa and a Bb individual

    for gen in range(1, k + 1):
        generation[gen] = generation[gen - 1] * 2 # the size of each generation is doubled

    # Probability that at least n Aa and Bb individuals are present in the k-th generatiin
    probability = 0 
    for index in range(N, generation[k] + 1):
        probability += (0.25 ** index) * (0.75 ** (generation[k] - index)) * comb(generation[k], index)

    return probability

# Function that computes the binomial coefficient
def comb(n, k):
    result = 1
    for index in range(k):
        result *= (n - index)
        result //= (index + 1)

    return result

result = prob_calculus(k, N)
print(result)
