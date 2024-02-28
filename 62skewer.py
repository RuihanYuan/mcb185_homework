import dogma

seq = 'ACGTACGTGGGGGACGTACGTCCCCC'
w = 10
g_count = seq[:w].count('G')
c_count = seq[:w].count('C')

for i in range(len(seq) - w + 1):
#start count beyond first window
	if i > 0:
		left_nt = seq[i-1]
		right_nt = seq[i+w-1]
		
		if left_nt == 'G':
			g_count -= 1
		elif left_nt == 'C':
			c_count -= 1
		
		if right_nt == 'G':
			g_count += 1
		elif right_nt == 'C':
			c_count += 1
		
		gc_comp = (g_count + c_count) / w
		gc_skew = dogma.gc_skew(seq[i:i+w])
		print(i, gc_comp, gc_skew)
	
