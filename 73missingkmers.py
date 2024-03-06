# coauthor: Anisha, Varsha
import sys
import mcb185
import itertools

#reverse compliment function
def rev_comp(seq):
	comp = {'A':'T', 'C':'G', 'G':'C', 'T':'A'}
	rev_comp = ""
	for i in range(len(seq) -1, -1, -1):
		rev_comp += comp[seq[i]]
	return rev_comp
	
#print(rev_comp("ACTG"))

#initializing conditions
k = 1
found = False

#process all kmers
for defline, seq in mcb185.read_fasta(sys.argv[1]):
#continue til missing kmers found
	while not found:
		kcount = {}
		#reverse and forward strand
		for strand in [seq, rev_comp(seq)]:
			for i in range(len(strand) -k +1):
				kmer = strand[i:i+k]
				if kmer not in kcount:
					kcount[kmer] = 1
				else:
					kcount[kmer] += 1
		
		#generate all possible kmers given k
		all_kmer = []
		for nts in itertools.product('ACGT', repeat=k):
			kmer_list = list(nts)
			kmer = ''.join(kmer_list)
			all_kmer.append(kmer)
			
		#identify kmers that are possible but were not found
		missing_kmer = []
		for kmer in all_kmer:
			if kmer not in kcount:
				missing_kmer.append(kmer)
		
		#print the missing kmers
		if missing_kmer:
			for kmer in sorted(missing_kmer):
				print(kmer)
			found = True
			
		#if no missing kmers found
		else:
			k += 1
			if k > len(seq):
				print("No missing kmers found.")
				break