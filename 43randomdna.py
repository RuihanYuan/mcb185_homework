import random

nts = 'ACGT'
for i in range(3):
	print('>seq-', i, sep='')
	for j in range(random.randint(50, 60)):
		print(random.choice(nts), end='')
	print()