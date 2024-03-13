import argparse
import math

import mcb185

parser = argparse.ArgumentParser(description='DNA entropy filter.')
parser.add_argument('file', type=str, help='name of fasta file')
parser.add_argument('-s', '--size', type=int, default=20, help='window size [%(default)i]')
parser.add_argument('-e', '--entropy', type=float, default=1.4,
																				help='entropy threshold [%(default).3f]')
parser.add_argument('--lower', action='store_true', help='soft mask')
arg = parser.parse_args()
print('dusting with', arg.file, arg.size, arg.entropy, arg.lower)



def entropy_cal(seq):
	nts = 'ACGT'
	entropy = 0
	for nt in nts:
		p = seq.count(nt) / len(seq)
		if p > 0:
			entropy += -p * math.log2(p)
	return entropy

def mask_seq(seq, w, threshold, soft_mask):
	seq_list = list(seq)
		
	for i in range(len(seq) - w + 1):
		window = seq[i:i+w]
		cur_en = entropy_cal(window)
		#print(f"Window: {window}, entropy: {cur_en}")
		if cur_en < threshold and soft_mask:
			for j in range(i, i + w):
				seq_list[j] = seq_list[j].lower()
	return ''.join(seq_list)

for defline, seq in mcb185.read_fasta(sys.argv[1]):
	w = arg.size
	threshold = arg.entropy
	masked_seq = mask_seq(seq, w, threshold, soft_mask=arg.lower)
	print(f">{defline}")
	for i in range(0, len(masked_seq), 60):
		print(masked_seq[i:i+60])