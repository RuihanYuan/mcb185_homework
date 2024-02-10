import random
trials = 100

print('DC', 'norm', 'adv', 'dis', sep='  ')
for dc in range(5, 16, 5):
	norm = 0
	adv = 0
	dis = 0
	for i in range(trials):
		r1 = random.randint(1, 20)
		r2 = random.randint(1, 20)
	
		#normal
		if r1 >= dc:
			norm += 1
			
		#advantage
		larger_roll = r1
		if r2 >= r1:
			larger_roll = r2
		if larger_roll >= dc:
			adv += 1
			
		#disadvantage
		smaller_roll = r1
		if r1 >= r2:
			smaller_roll = r2
		if smaller_roll >= dc:
			dis += 1
			
		p_norm = norm / trials
		p_adv = adv / trials
		p_dis = dis / trials
	print(dc, p_norm, p_adv, p_dis, sep='  ')
	
"""
In-class spoiler

for dc in range(5, 16, 5):
	n = 0
	a = 0
	d = 0
	for i in range(trials):
		r1 = random.randint(1, 20)
		r2 = random.randint(1, 20)
		if r1 >= dc:			#normal
			n += 1
		if r1 >= r2:			#when roll1 > roll2 and roll1 > dc: adv
			if r1 >= dc:
				a += 1
		else:										#when roll2 > roll1 and roll2 > dc: adv
			if r2 >= dc:
				a += 1
			if r1 >= dc:		#when roll2 > roll1 and roll1 > dc: disadv
				d += 1
	norm = n / trials
	adv = a / trials
	dis = d / trials
	print(dc, norm, adv, dis, sep="  ")
	"""