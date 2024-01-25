# import library for later use

import math

# function to compute shannon entropy of nucleotides

def shannon_entropy(a, c, t, g):
    total = a + c + t + g
    
	# initialize entropy from 0
	
    entropy = 0           

	# Function to calculate -p * log2(p) for a nucleotide count
	
	def entropy_term(n_count):
		if n_count == 0:				# log2 can't take 0
			return 0
		p = n_count / total				# probability of occurence
		return -p * math.log2(p)

	entropy += entropy_term(a)
	entropy += entropy_term(c)
	entropy += entropy_term(t)
	entropy += entropy_term(g)

	return entropy

# Test the function

print("Entropy:", shannon_entropy(0, 2, 4, 4))
print("Entropy:", shannon_entropy(1, 1, 1, 1))
print("Entropy:", shannon_entropy(0, 0, 0, 10))
