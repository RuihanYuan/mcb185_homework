import mcb185
import gzip
import sys

fasta_path = sys.argv[1]
gff_path = sys.argv[2]

def read_fasta(fasta_file):
	sequences = {}
	for defline, seq in mcb185.read_fasta(fasta_file):
		chrom_id = defline.split()[0]
		sequences[chrom_id] = seq
	return sequences

def load_introns(gff_file):
	introns = []
	with gzip.open(gff_file, 'rt') as fp:
		for line in fp:
			parts = line.strip().split('\t')
			if parts[2] == 'intron' and parts[5] != '.':
				chrom = parts[0]
				start = int(parts[3]) - 1
				end = int(parts[4]) - 1
				score = float(parts[5])
				strand = parts[6]
				introns.append((chrom, start, end, score, strand))
	return introns

def initialize_pwm(length):
	pwm = []
	for _ in range(length):
		pwm_dict = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
		pwm.append(pwm_dict)
	return pwm

def update_pwm(pwm, sequence):
	for i in range(len(sequence)):
		nt = sequence[i]
		if nt in pwm[i]:
						pwm[i][nt] += 1

def print_pwm(pwm, ac, id, desc):
	print('AC', ac)
	print('XX')
	print('ID', id)
	print('DE', desc)
	print(f'{"PO":<8}{"A":<8}{"C":<8}{"G":<8}{"T":<8}')
	for i, counts in enumerate(pwm):
		print(f'{i+1:<8}', end='')
		for nt in ['A', 'C', 'G', 'T']:
						print(f'{counts[nt]:<8}', end='')
		print()
	print('XX')
	print('//')

chrom_sequences = read_fasta(fasta_path)
introns_info = load_introns(gff_path)

don_pwm = initialize_pwm(6)
acc_pwm = initialize_pwm(7)

for chrom, start, end, score, strand in introns_info:
	if strand == "+":
		intron_seq = chrom_sequences[chrom][start:end+1]
	else:
		intron_seq = mcb185.anti_seq(chrom_sequences[chrom][start:end+1])
	d_seq = intron_seq[:6]
	a_seq = intron_seq[-7:]
	update_pwm(don_pwm, d_seq)
	update_pwm(acc_pwm, a_seq)

print_pwm(acc_pwm, 'DEM01', 'ACC', 'splice acceptor')
print_pwm(don_pwm, 'DEM02', 'DON', 'splice donor')

