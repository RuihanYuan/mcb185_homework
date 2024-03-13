import json
import gzip
import sys

#read the file
def read_file(filepath):
	records = []
	with gzip.open(filepath, 'rt') as fp:
		record = {}
		pwm_found = False
		for line in fp:
			line = line.strip()
			if line.startswith('XX'): continue
			elif line.startswith('ID'):
				record['id'] = line.split()[1]
			elif line.startswith('PO'):
				pwm_found = True
				record['pwm'] = []
			elif pwm_found and line.startswith(('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')):
				parts = line.split()
				record['pwm'].append({'A': float(parts[1]),
																										'C': float(parts[2]),
																										'G': float(parts[3]),
																										'T': float(parts[4])})
			elif line.startswith('//'):
				records.append(record)
				record = {}
				pwm_found = False
	return json.dumps(records, indent=4)
	
filepath = sys.argv[1]
output = read_file(filepath)
print(output)