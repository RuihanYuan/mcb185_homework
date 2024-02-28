#coauthor: Henry
import sys
import mcb185
import dogma

def kd_values(seq):
	return [dogma.kyte_doolittle(aa) for aa in seq]

def ave_kd(seq, start, length):
	region = seq[start:start+length]
	kd_val = kd_values(region)
	total = 0.0
	for val in kd_val:
		total += val
	return total / length if length > 0 else 0.0

def find_transmembrane_proteins(sequences):
	tm_proteins = []
	for name, seq in sequences:
# Check for signal peptide in the first 30 aa
		for i in range(23):  # 8 amino acids long signal peptide, index start with 0
			if ave_kd(seq, i, 8) >= 2.5 and 'P' not in seq[i:i+8]:
				# Check for transmembrane region in the rest of the sequence
				for j in range(30, len(seq) - 11 + 1):
					if ave_kd(seq, j, 11) >= 2.0 and 'P' not in seq[j:j+11]:
						tm_proteins.append(name)
						break  # Stop checking this sequence once a transmembrane region is found
				break  # Stop checking signal peptides once a valid one is found
	return tm_proteins

#input filepath from command line
fasta_file = sys.argv[1]
sequences = mcb185.read_fasta(fasta_file)

tm_proteins = find_transmembrane_proteins(sequences)
for name in tm_proteins:
		print(f'>{name}')
