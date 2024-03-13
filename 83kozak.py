import gzip
import sys
import re

import mcb185

def parse_gb(gb_file):
	start_pos = []
	with gzip.open(gb_file, 'rt') as fp:
		for line in fp:
			line = line.strip()
			if line.startswith('CDS'):
				match = re.search(r'(\d+)', line)	#find first number in line
				if match:
					start = int(match.group(1)) - 1
					start_pos.append(start)
	return start_pos
	
def initiation_seq(seq, start_pos, length):
	consensus = []
	for start in start_pos:
		if start >= length:
			ini_seq = seq[start-length:start]
			consensus.append(ini_seq)
	return consensus
	
def pwm_cal(up_seq):
	pwm = []
	for i in range(len(up_seq[0])):
		pwm.append({'A': 0, 'C': 0, 'G': 0, 'T': 0})
	for seq in up_seq:
		for i, nt in enumerate(seq):
			if nt in pwm[i]:
				pwm[i][nt] += 1
	return pwm

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
	
	transfac_format += "XX\n"
	return transfac_format

gb_file = sys.argv[1]
length = int(sys.argv[2])
fa_file = sys.argv[3]

for defline, seq in mcb185.read_fasta(fa_file):
	start_pos = parse_gb(gb_file)
	up_seq = initiation_seq(seq, start_pos, length)
	print('seq found:')
	for us in up_seq:
		print(us)

pwm = pwm_cal(up_seq)
for pos, counts in enumerate(pwm, start=1):
	print(f'position {pos}: {counts}')

pwm_data = {
	"AC": "IMTSU001",
	"ID": "ECKOZ",
	"DE": "I made this up",
	"pwm": pwm,
}

transfac_op = transfac_format(pwm_data)
print(transfac_op)

