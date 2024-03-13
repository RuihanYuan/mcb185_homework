#translate mRNA seq into aa
import argparse

import mcb185
import dogma

parser = argparse.ArgumentParser(description='mRNA translator.')
parser.add_argument('file', type=str, help='fasta file of mRNAs')
parser.add_argument('-m', '--min', type=int, default=100, help='minimum protein length[%(default)i]')
parser.add_argument('-a', '--anti', action='store_true', help='also examine the anti-parallel strand')
arg = parser.parse_args()
#print('dusting with', arg.file, arg.min, arg.anti)

def mrna_translate(seq, min_len):
	proteins = []
	for rf in range(3):
		proteins.append(dogma.translate(seq[rf:]))
	if arg.anti:
		anti_seq = mcb185.anti_seq(seq)
		for rf in range(3):
			proteins.append(dogma.translate(seq[rf:]))
	return proteins

for defline, seq in mcb185.read_fasta(arg.file):
	proteins = mrna_translate(seq, min_len=arg.min)
	for i, aa in enumerate(proteins):
		if len(aa) >= arg.min:
			print(f">{defline}")
			print(aa)
	