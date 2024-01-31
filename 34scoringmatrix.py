# define nucleotide sequence
sequence = 'ACGT'

# 3 spaces, 1 for the first row nt and 
# 2 to align with the width of +1 / -1
head_row = "   "

for nt in sequence:
	# increment by the nucleotide and the add spaces to math the width
	head_row += nt + "  "
print(head_row)

# print the matrix
for row_nt in sequence:
	row = row_nt
	# +1 for nt match -1 for mismatch
	for col_nt in sequence:
		if row_nt == col_nt:
			row += ' +1'
		else:
			row += ' -1'
	print(row)