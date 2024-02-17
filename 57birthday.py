#coauthor: Varsha, Anisha

import random
import sys

trials = int(sys.argv[1])
days = int(sys.argv[2])
people = int(sys.argv[3])

def bday_calendar(trials, days, people):
	shared_bday_trials = 0																	#how many trials have shared bday
	for i in range(trials):
		calendar = []																									#initially, 0 people  having bday on each day
		for j in range(days):
			calendar.append(0)
		
		for k in range(people):
			bday = random.randint(0, days - 1)
			calendar[bday] += 1																	#after assign a date, increment the count on calendar
			
		shared_bday = False
		for day_count in calendar:											#check if any of the date has more than 1 person
			if day_count > 1:
				shared_bday = True
				break
			
		if shared_bday:
			shared_bday_trials += 1
				
	prob = shared_bday_trials / trials
	return prob
	
p = bday_calendar(trials, days, people)
print("Bday paradox(using calendar list):", p)
