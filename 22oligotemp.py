
# Function to calculate oligo melting temperature
def oligo_tm(a, c, t, g):
	num_oligo = a + c + t + g
	
	if num_oligo <= 13:
		Tm = (a+t)*2 + (g+c)*4
		
	else:
		Tm = 64.9 + 41 * (g + c - 16.4) / (a + c + t + g)
		
	return Tm
	
# Test
Tm0 = oligo_tm(1, 3, 4, 5)
Tm1 = oligo_tm(10, 4, 25, 36)
Tm2 = oligo_tm(12, 13, 10, 2)

print("Tm0:", Tm0)
print("Tm1:", Tm1)
print("Tm2:", Tm2)
