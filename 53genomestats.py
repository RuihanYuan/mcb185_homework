import sys
import gzip

gffpath = sys.argv[1]
feature = sys.argv[2]

def mini(vals):
	mi = vals[0]
	for val in vals[1:]:
		if val < mi:
			mi = val
	return mi

def maxi(vals):
	ma = vals[0]
	for val in vals[1:]:
		if val > ma:
			ma = val
	return ma

def mean(vals):
	total = 0
	for val in vals:
		total += val
	return total / len(vals)	
		
def sd(vals):
	assert(len(vals) != 0)
	vals_mean = mean(vals)
	variance_total = 0
	for x in vals:
		variance_total += (x - vals_mean) ** 2
	variance = variance_total / len(vals)
	return variance ** 0.5

def median(vals):
	vals.sort()
	n = len(vals)
	midpt = n // 2
	for val in vals:
		if n % 2 == 0:
			return (vals[midpt] + vals[midpt - 1]) / 2
		else:
			return vals[midpt]

lengths = []
with gzip.open(gffpath, 'rt') as fp:
	for line in fp:
		if line[0] == '#':
			continue
		cols = line.split()
		if cols[2] == feature:
			beg, end = int(cols[3]), int(cols[4])
			length = end - beg + 1
			lengths.append(length)

if lengths:
	print("Count:", len(lengths))
	print("Minimum:", round(mini(lengths)))
	print("Maximum:", round(maxi(lengths)))
	print("Mean:", round(mean(lengths)))
	print("Standard Deviation:", round(sd(lengths)))
	print("Median:", round(median(lengths)))
else:
	print(f"No features of type '{feature}' found")



"""
--In class spoiler--
val = []

for x in sys.argv[1:]:
	val.append(int(x))
print(val)
val.sort()
print(val)

midpt = len(val) // 2

if len(val) % 2 == 1:
	m = val[midpt]
else:
	m = (val[midpt] + val[midpt - 1]) / 2

print(m)
"""