import sys
import json

import mcb185

k = int(sys.argv[2])
#kcount = {}
klocation = {}

for defline, seq in mcb185.read_fasta(sys.argv[1]):
	words = defline.split()
	chrom = words[0]
	for i in range(len(seq) -k +1):
		kmer = seq[i:i+k]
		if kmer not in klocation:
			klocation[kmer] = {} #set to object
		if chrom not in klocation[kmer]:
			klocation[kmer][chrom] = []
		klocation[kmer][chrom].append(i)
		#if want chrom first: exchange the place of chrom with kmer: klocation[chrom][kmer]

print(json.dumps(klocation, indent=4))
#print(kcount)

{
	
	}

"""
#list
print(sys.argv)

#2nd letter of the first argument
print(sys.argv[1][2])

matrix = [
	[1, 2, 3],
	[4, 5, 6, 7, [8, 9]],
	]
	
print(matrix)
#1st value of the second list of the matrix
print(matrix[1][0])
"""

"""
person = {
	'name': 'Ian Korf',
	'age': 57,
	'weight': 163.8,
	'marries': True,
	'pets': [
		'Hesper', 'Mouserat', 'Librat'],
		'mentees': {
		'Claire': 'undergrad',
		'Dell': 'undergrad',}
	}

print(json.dumps(person, indent=4))

print(person['pets'][0])
print(person['mentees']['Claire'])

#[]:list
#{}:dictionary or object
"""