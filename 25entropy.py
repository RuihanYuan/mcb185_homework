# Import library
import math

# Function to compute shannon entropy of nucleotides
def shannon_entropy(a, c, t, g):
	total = a + c + t + g
	assert(total != 0)
	
	entropy = 0
	
	if a != 0:
		p_a = a / total
		entropy -= p_a * math.log2(p_a)
	if c != 0:
		p_c = c / total
		entropy -= p_c * math.log2(p_c)
	if t != 0:
		p_t = t / total
		entropy -= p_t * math.log2(p_t)
	if g != 0:
		p_g = g / total
		entropy -= p_g * math.log2(p_g)
		
	return entropy
	
# Test
print("Entropy:",shannon_entropy(0, 2, 4, 4))
print("Entropy:",shannon_entropy(1, 1, 1, 1))
print("Entropy:",shannon_entropy(1, 0, 10, 0))
