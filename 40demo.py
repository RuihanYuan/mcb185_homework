import random

for i in range(5):
	print(random.random())	#0<=x<1
	
for i in range(50):
	print(random.choice('ACGT'), end='')
print()

for i in range(50):
	r = random.random()
	if r < 0.7: print(random.choice('AT'), end='')
	else:							print(random.choice('CG'), end='')
print()

for i in range(3):
	print(random.randint(1, 6))	#generate number between 1-6 (inclusive)
	
for i in range(5):
	print(random.gauss(0.0, 1.0))	#mean, sd
	
print('a\tb\tcat\tdogma')

i = 1
pi = 3.14159
print('normal string {i} {pi}')
print(f'formatted string {i} {pi:.3f}')
print(f'tau {pi + pi}')

import sys
print('logging', file=sys.stderr)
"""
limit = 4
#full matrix
for i in range(limit):
	for j in range(limit):
		print(i, j)

#half matrix with diagonal
for i in range(limit):
	for j in range(i, limit):
		print(i, j)
		
#half matrix without diagonal
for i in range(limit):
	for j in range(i+1, limit):
		print(i, j)
		"""
#full matrix with +/-
nts = 'ACGT'
#print header
for nt in nts:
	print(nt, end=' ')
print()
for nt1 in nts:
	print(nt1)
limit = len(nts)
for i in range(limit):
	for j in range(limit):
		if i == j:	print('+', end=' ')
		else:						print('-', end=' ')
	print()