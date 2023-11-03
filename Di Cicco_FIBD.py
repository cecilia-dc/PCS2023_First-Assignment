'''
Rosalind FIBD exercise by Di Cicco Cecilia
'''
# Mortal Fibonacci Rabbits

n = 99   # number of monts
m = 20   # life expectancy of a rabbit

def rabbit_population(n, m):
    # list to store the population for each age
    population = [0] * m
    population[0] = 1  # we start with a pair of children rabbits (offspring) that will have to wait a month to become adults and be able to reproduce
    
    for generation in range(1, n):
        new_population = [0] * m
        for age in range(1, m):  # after m months the rabbith dies
            new_population[age] = population[age - 1]
        new_population[0] = sum(population[1:])
        population = new_population

    total_population = sum(population)

    return total_population

result = rabbit_population(n, m)
print(result)