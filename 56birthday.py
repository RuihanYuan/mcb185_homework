#coauthor: Henry

import random
import sys

trials = int(sys.argv[1])
days = int(sys.argv[2])
people = int(sys.argv[3])

def bday_paradox(trials, days, people):
	shared_bday = 0																							#initialize count
	for i in range(trials):															#10-14: for a total num of trials perform stimulation
		bdays = []
		for j in range(people):														#for given num of students
			bday = random.randint(1, days)
			bdays.append(bday)
		bdays.sort()
	
		shared_found = False																	#default is False
		for i in range(len(bdays) - 1):						#comparing the prev with the next so index - 1
			if bdays[i] == bdays[i + 1]:
				shared_found = True																#break if found same bday
				break
		if shared_found:
			shared_bday += 1																				#increment count if any being found
	prob = shared_bday / trials
	return prob
	
p = bday_paradox(trials, days, people)
print("Birthday paradox probability:", p)
