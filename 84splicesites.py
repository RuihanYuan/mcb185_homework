
import sys
import gzip

import mcb185

#parse gff file
def parse_gff(gff_file):
	introns = []
	with gzip.open(gff_file, 'rt') as fp:
		for line in fp:
			if line.strip() and not line.startswith('#'):
				cols = line.strip().split('\t')
				if cols[1] != 'RNASeq_splice':	continue
				chrom = cols[0]
				start = int(cols[3])
				end = int(cols[4])
				strand = cols[6]
				introns.append((chrom, start, end, strand))
				#print(f"Intron found: {chrom}, {start}, {end}, {strand}")
	return introns
	
#parse fa file
def parse_fa(fa_file):
	seqs = {}
	for defline, seq in mcb185.read_fasta(fa_file):
		line = defline.strip().split()
		if line:
			chrom = line[0]
			seqs[chrom] = seq
			print(f"Sequence read for chromosome: {chrom}")
	return seqs


#TRANSFAC format 
def transfac_format(pwm_data):
	transfac_format = (
	f"AC {pwm_data['AC']}\n"
	"XX\n"
	f"ID {pwm_data['ID']}\n"
	"XX\n"
	f"DE {pwm_data['DE']}\n"
	f'{"PO":<8}{"A":<8}{"C":<8}{"G":<8}{"T":<8}\n'
	)
	for i, counts in enumerate(pwm_data['pwm'], start=1):
		transfac_format += (
		f'{i:<8}'
		f'{counts["A"]:<8}'
		f'{counts["C"]:<8}'
		f'{counts["G"]:<8}'
		f'{counts["T"]:<8}\n'
		)
	
	transfac_format += "XX\n//\n"
	return transfac_format

#calculate PWM
def pwm_cal(up_seq):
	pwm = []
	for seq in up_seq:
		while len(pwm) < len(seq):
			pwm.append({'A': 0, 'C': 0, 'G': 0, 'T': 0})
		for i, nt in enumerate(seq):
			if nt in pwm[i]:
				pwm[i][nt] += 1
	return pwm

gff_file = sys.argv[1]
fa_file = sys.argv[2]

introns = parse_gff(gff_file)
sequences = parse_fa(fa_file)
#print("Chromosomes available in sequences dictionary:", sequences.keys())

#to hold sequences
d_sites = []
a_sites = []

#length of region
d_length = 6
a_length = 7

for chrom, start, end, strand in introns:
	#print(f"Accessing sequence for chromosome: '{chrom}'")
	if strand == '+':
		d_seq = sequences[chrom][start-d_length:start]
		a_seq = sequences[chrom][end:end+a_length]
	#intron_seq = sequences[chrom][start-1:end]
	else:
		d_seq = mcb185.anti_seq(sequences[chrom][end:end+d_length])
		a_seq = mcb185.anti_seq(sequences[chrom][start-a_length:start])
		
	d_sites.append(d_seq)
	a_sites.append(a_seq)
	
d_pwm = pwm_cal(d_sites)
a_pwm = pwm_cal(a_sites)

pwm_donor = {
	'AC': 'DONOR1',
	'ID': 'DON',
	'DE': 'splice donor',
	'pwm': d_pwm,
}

pwm_acceptor = {
	'AC': 'ACCEPTOR1',
	'ID': 'ACC',
	'DE': 'splice acceptor',
	'pwm': a_pwm,
}

print(transfac_format(pwm_acceptor))
print(transfac_format(pwm_donor))


