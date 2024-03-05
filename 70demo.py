import mcb185
import sys
kcount = {}
k = 3
for defline, seq in mcb185.read_fasta(sys.argv[1]):
	print(defline)
	for i in range(len(seq) - k + 1):
		kmer = seq[i:i+k]
		
		if kmer not in kcount:
			kcount[kmer] = 0
		kcount[kmer] += 1

for kmer, n in kcount.items():
	print(kmer, n)

import itertools
for nts in itertools.product('ACGT', repeat=2):
	print(nts)


"""
import random
#same random thing every time
random.seed(1)

size = 10000
words = []
for i in range(size):
	token = []
	for j in range(10):
		token.append(random.choice('ACDEFGHIKLMNPQRSTVWY'))
	token = ''.join(token)
	words.append(token)
print(words)

for i in range(1000):
	if 'MYNAMEISIAN' in words:
		print('Found')
"""
"""
#make random protein
protein_legth = 300
#make string is not as efficient as make a list
#no need to rewrite the string every time as incrementing
protein = []
for i in range(protein_length):
	aa = random.choice('ACDEFGHIKLMNPQRSTVWY')
	protein.apend(aa)
protein = ''.joint(protein)
print(protein)


def kyte_doolittle(aa):
	kds = 0
	for aa in seq:
		if aa == 'A' or aa == 'a':
			kds += 1.80
		elif aa == 'C' or aa == 'c':
			kds +=  2.50
		elif aa == 'D' or aa == 'd':
			kds +=  -3.50
		elif aa == 'E' or aa == 'e':
			kds +=  -3.50
		elif aa == 'F' or aa == 'f':
			kds +=  2.80
		elif aa == 'G' or aa == 'g':
			kds +=  -0.40
		elif aa == 'H' or aa == 'h':
			kds +=  -3.20
		elif aa == 'I' or aa == 'i':
			kds +=  4.50
		elif aa == 'K' or aa == 'k':
			kds +=  -3.90
		elif aa == 'L' or aa == 'l':
			kds +=  3.80
		elif aa == 'M' or aa == 'm':
			kds +=  1.90
		elif aa == 'N'or aa == 'n':
			kds +=  -3.50
		elif aa == 'P' or aa == 'p':
			kds +=  -1.60
		elif aa == 'Q' or aa == 'q':
			kds +=  -3.50
		elif aa == 'R' or aa == 'r':
			kds +=  -4.50
		elif aa == 'S' or aa == 's':
			kds +=  -0.80
		elif aa == 'T' or aa == 't':
			kds +=  -0.70
		elif aa == 'V' or aa == 'v':
			kds +=  4.20
		elif aa == 'W' or aa == 'w':
			kds +=  -0.90
		elif aa == 'Y' or aa == 'y':
			kds +=  -1.30
		return kds / len(seq)
		
def kdh_list(Seq):
	aas = 'ACDEFGHIKLMNPQRSTVWY'
	kds = () #list with corresponding kdh values


"""

