
import sys
import mcb185
import dogma

def find_proteins_in_frame(trans_seq, min_len):
	valid_proteins = []
	for orf in trans_seq.split('*'):
		if 'M' in orf:
			start = orf.find('M')
			protein = orf[start:]
			if len(protein) >= min_len:
				valid_proteins.append(protein)
	return valid_proteins

def process_sequence(seq, min_len):
	valid_proteins = []
	# Process forward frames
	for i in range(3):
		trans_seq = dogma.translate(seq[i:])
		valid_proteins.extend(find_proteins_in_frame(trans_seq, min_len))
	# Process reverse frames
	rev_seq = dogma.revcomp(seq)
	for i in range(3):
		trans_seq = dogma.translate(rev_seq[i:])
		valid_proteins.extend(find_proteins_in_frame(trans_seq, min_len))
	return valid_proteins

fasta_file = sys.argv[1]
min_len = int(sys.argv[2])
for name, seq in mcb185.read_fasta(fasta_file):
				proteins = process_sequence(seq, min_len)
				for i, protein in enumerate(proteins):
								identifier = f'{name.split()[0]}-prot-{i+1}'  
								print(f'>{identifier}\n{protein}')


