#co-author: Pearce Pelia
import random

iteration = 10000
total_3d6 = 0
total_3d6r1 = 0
total_3d6x2 = 0
total_4d6d1 = 0


#3D6
for i in range(iteration):
	for d6 in range(3):
		total_3d6 += random.randint(1, 6)


#36dr1
for j in range(iteration):
	for r1 in range(3):
		roll = random.randint(1, 6)
		if roll == 1:
			roll = random.randint(1, 6)
		total_3d6r1 += roll
	
#3d6x2
for k in range(iteration):
	for x2 in range(3):
		d1 = random.randint(1, 6)
		d2 = random.randint(1, 6)
		if d1 > d2:
			total_3d6x2 += d1
		else:
			total_3d6x2 += d2
			
#4d6d1
for h in range(iteration):
	for d4 in range(4):
		d1 = random.randint(1, 6)
		d2 = random.randint(1, 6)
		d3 = random.randint(1, 6)
		d4 = random.randint(1, 6)
		min_d = d1
		if d2 < min_d:
			min_d = d2
		if d3 < min_d:
			min_d = d3
		if d4 < min_d:
			min_d = d4
	total_4d6d1 += (d1 + d2 + d3 + d4 - min_d)
		
#calculate average
avg_3d6 = total_3d6 / iteration
avg_3d6r1 = total_3d6r1 / iteration
avg_3d6x2 = total_3d6x2 / iteration
avg_4d6d1 = total_4d6d1 / iteration

#print results
print(f'3D6: {avg_3d6:.3f}')
print(f'3D6r1: {avg_3d6r1:.3f}')
print(f'3D6x2: {avg_3d6x2:.3f}')
print(f'4D6D1: {avg_4d6d1:.3f}')
	