
import sys
import re
import gzip

def revcomp(dna):
				rc = []
				for nt in dna[::-1]:  
								if nt == 'a': rc.append('t')
								elif nt == 'c': rc.append('g')
								elif nt == 'g': rc.append('c')
								elif nt == 't': rc.append('a')
								else: rc.append('N')
				return ''.join(rc)

def calculate_pwm(file_path):
	sequences = []
	position = []

	for i in range(14):
		nt_count = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
		position.append(nt_count)

	# Extract the sequence
	with gzip.open(file_path, 'rt') as fp:
		origin_found = False
		for line in fp:
						if re.search('ORIGIN', line): 
										origin_found = True
										continue
						if origin_found:
										if line.startswith('//'):
														break
										else:
														sequence = ''.join(line.rstrip().split()[1:])
														sequences.append(sequence)
	joined_seq = ''.join(sequences)

	# Find PWM
	with gzip.open(file_path, 'rt') as fp:
		for line in fp:
				if line.startswith('     CDS'):
						index = line.rstrip().split()[1]
						if re.search('complement\(join|join', line):
										continue
						elif re.search('complement', line): 
										end_i = index.split('..')[-1].split(')')[0]
										seq = revcomp(joined_seq[int(end_i)-5:int(end_i)+9])
						else:
										start_i = index.split('..')[0]
										seq = joined_seq[int(start_i)-10:int(start_i)+4]

						for i, nt in enumerate(seq[:14]):
										if nt == 'a': position[i]['A'] += 1
										elif nt == 'c': position[i]['C'] += 1
										elif nt == 'g': position[i]['G'] += 1
										elif nt == 't': position[i]['T'] += 1

	return position

#print PWM table
def print_pwm(position):
	print('AC IMTSU001')
	print('XX')
	print('ID ECKOZ')
	print('DE I made this up')
	print('PO      A       C       G       T')
	for i in range(14):
					line = (f'{i+1:<8}'
													f'{position[i]["A"]:<8}'
													f'{position[i]["C"]:<8}'
													f'{position[i]["G"]:<8}'
													f'{position[i]["T"]:<8}')
					print(line)
	print('XX')

file_path = sys.argv[1]
position = calculate_pwm(file_path)
print_pwm(position)
