import random

trials = 100000
r_count = 0
d_count = 0
st_count = 0

for i in range(trials):
	f_count = 0
	su_count = 0
	
	while True:
		roll = random.randint(1, 20)
		if roll == 1:
			f_count += 2
		elif roll < 10:
			f_count +=1
			#print('Failure')
		elif roll == 20:
			r_count += 1
			break																#revive ends the trial
		else:
			su_count += 1
			#print('Success')
		if f_count >= 3:
			d_count += 1
			#print('die')
			break																#die ends the trial
		if su_count >= 3:
			#print('stable')
			st_count += 1
			break																#stable ends the trial
		
#probability
p_die = d_count / trials
p_stable = st_count / trials
p_revive = r_count / trials

print('Die', 'Stable', 'Revive', sep='     ')
print(p_die, p_stable, p_revive, sep='  ')