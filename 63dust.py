import mcb185
import sys
import math

def entropy_cal(seq):
	nts = 'ACGT'
	entropy = 0
	for nt in nts:
		p = seq.count(nt) / len(seq)
		if p > 0:
			entropy += -p * math.log2(p)
	return entropy

def mask_seq(seq, w, threshold):
	#convert to list
	seq_list = [nt for nt in seq]
	for i in range(len(seq) - w + 1):
		window = ''.join(seq_list[i:i+w])
		cur_en = entropy_cal(window)
		print(f"Window: {window}, entropy: {cur_en}")
		if cur_en < threshold:
			for j in range(i, i + w):
				seq_list[j] = 'N'
	return ''.join(seq_list)

for defline, seq in mcb185.read_fasta(sys.argv[1]):
	w = int(sys.argv[2])
	threshold = float(sys.argv[3])
	masked_seq = mask_seq(seq, w, threshold)
	print(f">{defline}")
	print(masked_seq)