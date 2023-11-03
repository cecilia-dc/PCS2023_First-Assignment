'''
Rosalind FIB exercise by Di Cicco Cecilia
'''
# Rabbits and Recurrence Relations

adult_rabbits = 0
children_rabbits = 1
 # children rabbits need 1 month to become adults and reproduce
 # at month 1 we have a pair of children rabbits (offspring)
 # at month 2 we have a pair of grown rabbits that have become adult and reproduce the month later and give k rabbit pairs of children_rabbits

count = 1
new_adults = 0

n = 28 # number of months
k = 3 # number of rabbit pairs that every pair of reproduction-age rabbits produces

while (count < n):
    new_adults = adult_rabbits + children_rabbits 
    children_rabbits = adult_rabbits * k # each pair of adult rabbits produces k children rabbit pairs
    adult_rabbits = new_adults
    count = count + 1

total_rabbits = adult_rabbits + children_rabbits # total number of rabbits is the sum of both adult and children rabbits

print(total_rabbits)