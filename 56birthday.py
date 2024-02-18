#coauthor: Henry

import random
import sys

trials = int(sys.argv[1])
days = int(sys.argv[2])
people = int(sys.argv[3])

#12-15: for a total num of trials perform stimulation
def bday_paradox(trials, days, people):
	#initialize count
	shared_bday = 0
	for i in range(trials):
		bdays = []
		#for given num of students
		for j in range(people):
			bday = random.randint(1, days)
			bdays.append(bday)
		bdays.sort()
		
	#default is False
		shared_found = False
		#comparing the prev with the next so index - 1
		for i in range(len(bdays) - 1):
			if bdays[i] == bdays[i + 1]:
			#break if found same bday
				shared_found = True
				break
		#increment count if any being found
		if shared_found:
			shared_bday += 1
	prob = shared_bday / trials
	return prob
	
p = bday_paradox(trials, days, people)
print("Birthday paradox probability:", p)
