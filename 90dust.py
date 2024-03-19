
import argparse
import math
import sys

import mcb185

parser = argparse.ArgumentParser(description='DNA entropy filter.')
parser.add_argument('file', type=str, help='name of fasta file')
parser.add_argument('-s', '--size', type=int, default=20,
																			help='window size [%(default)i]')
parser.add_argument('-e', '--entropy', type=float, default=1.4,
																			help='entropy threshold [%(default).3f]')
parser.add_argument('--lower', action='store_true', help='soft mask')
arg = parser.parse_args()
print('dusting with', arg.file, arg.size, arg.entropy, arg.lower)

def entropy_cal(seq):
	nts = 'ACGT'
	entropy = 0
	seq_length = len(seq)
	for nt in nts:
		nt_count = 0
		for char in seq:
			if char == nt:
				nt_count += 1
		p = nt_count / seq_length
		if p > 0:
			entropy += -p * math.log2(p)
	return entropy
	
def to_lower(nt):
	if nt == 'A': return 'a'
	if nt == 'C': return 'c'
	if nt == 'G': return 'g'
	if nt == 'T': return 't'
	return nt


def mask_seq(seq, w, threshold, soft_mask):
	seq_list = list(seq)
	
	for i in range(len(seq) - w + 1):
		window = seq[i:i+w]
		cur_en = entropy_cal(window)
		if cur_en < threshold:
			for j in range(i, i + w):
				if soft_mask:
						seq_list[j] = to_lower(seq_list[j])
				else:
						seq_list[j] = 'N'
	return ''.join(seq_list)

for defline, seq in mcb185.read_fasta(arg.file):
	w = arg.size
	threshold = arg.entropy
	masked_seq = mask_seq(seq, w, threshold, soft_mask=arg.lower)
	print(f">{defline}")
	for i in range(0, len(masked_seq), 60):
		print(masked_seq[i:i+60])
