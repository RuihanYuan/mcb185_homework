#using Monte Carlo to estimate pi
import random

pi = 0
r_in = 0
n = 0
while True:
	x = random.random()
	y = random.random()
	dis = (x**2 + y**2)**0.5
	if dis < 1:
		r_in += 1
	n += 1
	pi = 4 * (r_in / n)
	print('pi:', pi)